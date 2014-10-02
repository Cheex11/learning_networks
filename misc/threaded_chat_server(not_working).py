import socket
import thread
import time

HOST = "127.0.0.1"
PORT = 4004

def accept(conn):
    def threaded():
        while True:
            conn.send("Please enter your name: ")
            try:
                name = conn.recv(1024).strip()
            except socket.error:
                continue
            if name in users:
                conn.send("Name entered is already in use.\n")
            elif name:
                conn.setblocking(False)
                users[name] = conn
                broadcast(name, "+++ %s arrived +++" % name)
                break
    thread.start_new_thread(threaded, ())

def broadcast(name, message):
    print message
    for to_name, conn in users.items():
        if to_name != name:
            try:
                conn.send(message + "\n")
            except socket.error:
                pass

# Set up the server socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(False)
server.bind((HOST, PORT))
server.listen(1)
print "Listening on %s" % ("%s:%s" % server.getsockname())

# Main event loop.
users = {}
while True:
    try:
        # Accept new connections.
        while True:
            try:
                conn, addr = server.accept()
            except socket.error:
                break
            accept(conn)
        # Read from connections.
        for name, conn in users.items():
            try:
                message = conn.recv(1024)
            except socket.error:
                continue
            if not message:
                # Empty string is given on disconnect.
                del users[name]
                broadcast(name, "--- %s leaves ---" % name)
            else:
                broadcast(name, "%s> %s" % (name, message.strip()))
        time.sleep(30)
    except (SystemExit, KeyboardInterrupt):
        break
