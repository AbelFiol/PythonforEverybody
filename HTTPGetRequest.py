import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket.
mysock.connect(('data.pr4e.org', 80))  # Connect to the server.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # Prepare the GET request.
mysock.send(cmd)  # Send the request.

while True:
    data = mysock.recv(512)  # Receive data from the server in chunks.
    if len(data) < 1:  # Break if no data is received.
        break
    print(data.decode(), end='')  # Decode and print the received data.

mysock.close()  # Close the connection.