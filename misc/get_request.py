import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'www.pythonprogramming.com'
port = 80

server_ip = socket.gethostbyname(server)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)
# s.recv(##)  The number is the buffer.

# Returns when complete
# print result

# Returns and buffers
while (len(result) > 0):
    print (result)
    result = s.recv(4096)
