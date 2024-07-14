""" MMKMOK001  CLIENT CODE Assignment 1"""
from socket import *

"""constant declaration """
IP = gethostbyname(gethostname())
PORT = 1237
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1050


def main():
    """ Creating a TCP client  socket. """
    client = socket(AF_INET, SOCK_STREAM)

    """ Connecting to the server. """
    client.connect((IP, PORT))

    request = input("Do you want to UPLOAD [U] or DOWNLOAD [D] or LIST AVAILIBLE FILE [L]  ?")
    # client.send(request.encode()) # send the user request to the server

    
    if request == "U":  # sending to the server
        client.send(request.encode(FORMAT))  # send request to the server

        """get the filename from the user"""
        file_name = input("Enter the filename: ") # the file entered must be in the same folder as the client program
       # file_name = "File.txt"
        """ open and read the file data. """
        file = open(file_name, "r")
        data = file.read()

        """ Send the filename to the server. """
        client.send(file_name.encode(FORMAT))
        message = client.recv(SIZE).decode(FORMAT) # decodes message of [SERVER]: File data received from the server
        print(message) #print confirmation message from the server

        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
        message = client.recv(SIZE).decode(FORMAT) # decodes message of [RECV] Receiving the file data from the server
        print(message)  #print confirmation message from the server

        """ Closing the file. """
        file.close()

        """ Closing the connection from the server. """
        client.close()

    elif request == "D":  # retrieve = downloading from the server

        client.send(request.encode(FORMAT))  # send request to the server

        """get the filename from the user"""
        file_name = input("Enter the filename: ")
        """ Send the filename to the server. """
        client.send(file_name.encode(FORMAT))

        # name = client.recv(SIZE).decode(FORMAT)  # receive filename
        # client.send(b"Yes")  # >>>>>done
        data = client.recv(SIZE).decode(FORMAT)  # data variable receives a respond from the server >>>> done

        file = open(file_name, "w")
        file.write(data)
        print("[Client] Done downloading")

        file.close()

    elif request == "L":
        client.send(request.encode(FORMAT))  # send request to the server
        data = client.recv(1024).decode(FORMAT)  # receive & decode list from the server

        print("[Client] Available files on the File Storage server:")
        for x in data:  # print out the filename from a list
            print(" * " + x)

        client.close()  # close the client sockets

    else:  # Invalid request
        print("[Invalid Request] Connection not initiated ")
        # print("Next time make sure you follow instructions!!")

        client.close()
        exit(0)  # a clean exit without any errors


if __name__ == "__main__":
    main()
