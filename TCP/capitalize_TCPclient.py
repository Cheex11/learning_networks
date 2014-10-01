import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    # When it connects it will...
    message = raw_input('-> ')
    while message != 'q':
        s.send(message)
        # Listening from data for the server...
        data = s.recv(1024)
        # Prints message received from server...
        print 'Received from server: ' + str(data)
        message = raw_input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
