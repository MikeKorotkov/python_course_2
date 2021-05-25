import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)

serv_message = str('Your result is: ')
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        result2 = client.recv(1024)
        result3 = client.recv(1024)
        client.close()
        decoded_res1 = result.decode('ascii')
        decoded_res2 = result2.decode('ascii')
        add_res = int(decoded_res1) * int(decoded_res2)
        print(serv_message, add_res)
        decoded_res3 = result3.decode('utf-8')
        if decoded_res3 == 'close':
            sock.close()
            break
