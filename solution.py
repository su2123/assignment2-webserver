# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)
  print("The server is ready to receive")
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read().splitlines()
        #Send one HTTP header line into socket.
        #Fill in start
        response_code = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(response_code.encode())
        connectionSocket.send("\r\n".encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        response_code = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(response_code.encode())
        connectionSocket.send("\r\n".encode())

        response = """
        <html>
          <head>
              <h1>404 Not Found</h1>
          </head>
        </html>
        """
        connectionSocket.send(response.encode())
        connectionSocket.send("\r\n".encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)