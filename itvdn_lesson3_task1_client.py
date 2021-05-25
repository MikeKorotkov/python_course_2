import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('', 8888))

    message = int(input('Enter your first number: '))
    sock.send(bytes(str(int(message)), 'ascii'))

    message2 = int(input('Enter your second number: : '))
    sock.send(bytes(str(int(message2)), 'ascii'))

    message3 = str(input('Enter "close" to finish processing or press "Enter" to continue: '))
    sock.send(bytearray(message3, 'utf-8'))

    sock.close()