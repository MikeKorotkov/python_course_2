import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('', 8888))

    message = str(input('Enter your message: '))
    sock.send(bytearray(message, 'utf-8'))


    sock.close()
