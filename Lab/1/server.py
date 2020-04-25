"""
s = socket.socket('NETWROK LAYER PROTOCOL', 'TRANSPORT LAYER PROTOCOL')

s.bind(HOST(IP), PORT)

s.listen()

s.accept()

s.recv()

s.connect('HOST INFORMATION')


"""

import socket
import threading

PORT = 7447

MESSAGE_LENGTH_SIZE = 64

ENCODING = 'utf-8'

def main():
    address = socket.gethostbyname(socket.gethostname())

    HOST_INFORMATION = (address, PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(HOST_INFORMATION)

    print("[SERVER STARTS] server is starting...")
    start(s)

def start(server):
    server.listen()

    while True:
        conn, address = server.accept()

        t = threading.Thread(target=client_handler, args=(conn, address))

        t.start()

def client_handler(conn, address):
    print('[NEW CONNECTION] connected from {}'.format(address))

    connected = True
    while connected:
        message_length = int(conn.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING))
        
        msg = conn.recv(message_length).decode(ENCODING)

        print('[MESSAGE RECIEVED] {}'.format(msg))

        if msg == 'DISCONNECT':
            connected = False
    
    conn.close()


if __name__ == '__main__':
    main()
