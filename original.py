import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# отключение тайм-айута подключения
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Waiting for a connection..')
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        print('Waiting for a request.. ')
        request = client_socket.recv(4096)
        print('Request accepted. Trying to send a reply..')
        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
            print('Reply sent.')