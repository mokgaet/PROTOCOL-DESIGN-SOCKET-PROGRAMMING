# PROTOCOL-DESIGN-SOCKET-PROGRAMMING
CSC3002F |Networks Assessment in Python

INTRODUCTION
We are tasked with implementing a client-server file sharing application that will allow clients to send and receive files. The application should
consist of two sockets, the client-side socket, and the server-side socket. The two sockets should be able to communicate by establishing a
connection. This is accomplished when the server receives a connection request on its specific server port from the client. If any more
connection requests arrive, the server accepts them in the similar way creating a new port for each new connection. Thus, at any instant, the
server must be able to communicate simultaneously with many clients and to wait on the same time for incoming requests on its specific server
port.

AIM
The aim of this assignment is to implement a client-server file sharing application that makes use of TCP sockets. The application must govern
privacy/confidentiality.

HOW TO RUN/EXECUTE THE PROGRAMS
1. Run the serve first [ the server has to be online all the time so that when clients try to reach must succeed in doing that)
2. Then run the client 



Implematation Explaination
Server
A server is responsible for listening for incoming connections from clients and responding to their request. When the socket receives a
connection request from the client, a connection is established. After performing the requests from user, the program prints out messages to
communicate to users that a specific request has been done.
Every feature of the server program was implemented under the main function. The socket function creates a new socket, and the bind ()
function binds the socket to an IP address and a port number. On the while loop, the accept () method is to allow the server-side socket to
accept a connection request from user. The recv () method takes in a specific number of bytes that can be accepted by the server at a time, and
it decodes the information received from the client to the specified format.

Cilent
The client is responsible for connecting to the server to send requests.
Functionalities & screenshots of chat application and features
1. Enabling the client to upload files on the server.
2. Enabling the client to query the server for a list of available files.
3. Error handling when an unknown request is made.

   Approached technique used behind the above-mentioned client functionalities and features is the use of TCP sockets.
1. Get the host information.
2. Create a socket.
3. Connect the socket within the host (establish connection with the server group)
4. Use functions such as send () and recv() functions for communicate between the client and server.
- For the downloading functionality, the user sends a filename that they would like to download & through implementation I
used send () function to send encoded filename requested by the user to the server. Then the recv() function is used by the
server to receiver the filename then decoded so that it can be able to retrieve the file from its storage .
- For the sending functionality, the server uses recv() to receive a filename and file data from the client. Then the send () function
is used by the client to receive confirmation messages that the file is uploaded on the server file storage.
- For the listing of files available on the server functionality, the server uses the send () function to transfer a list of files available
on the server file storage. Then the client uses the recv() function to receive that list then loop through the list to display them
to the user.
5. Close the socket file descriptor.

In Closing:
When designing and implementing the client-server file sharing application using TCP sockets it is important to define a protocol such as
message formats and types which will be used for communication between the client and the server.
In conclusion, the TCP file sharing application is a convenient tool for file transferring/sharing over a network. Its key features include fast
transferring speed/ efficient transmission of files and secure protocol.
Overall, the TCP file sharing application provides end-to-communication, flow control and congestion control which makes the transmission
speed fast and most importantly the benefits it provides makes the tool valuable for file sharing, and from our group we highly recommend TCP
file sharing protocol.
