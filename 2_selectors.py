import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # отключение тайм-айута подключения
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # Регистрация объекта. fileobj - объект, events - ожидаемое событие(READ), data - связанная информация
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    # Регистрация объекта. fileobj - объект, events - ожидаемое событие(READ), data - связанная функция
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_massege)


def send_massege(client_socket):
        request = client_socket.recv(4096)

        if request:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
        else:
            selector.unregister(client_socket)
            client_socket.close()

    

def event_loop():
    while True:

        events = selector.select() # (key, events)
        
        # SelectorKey
        # fileobj
        # event
        # data

        for key, _ in events():
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()