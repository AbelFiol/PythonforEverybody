import socket
import ssl

# Create an SSL context.
context = ssl.create_default_context()

# Create a socket and wrap it with SSL.
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = context.wrap_socket(mysocket, server_hostname='data.pr4e.org')
ssl_socket.connect(('data.pr4e.org', 443))

# Send the correct HTTPS GET request.
cmd = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\nConnection: close\r\n\r\n'.encode()
ssl_socket.send(cmd)

# Receive and print the response.
while True:
    data = ssl_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

# Close the SSL-wrapped socket.
ssl_socket.close()