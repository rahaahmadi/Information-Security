from socket import socket
from tqdm import tqdm


def detect_open_ports(ip, start, end):
    open_ports = []
    port_detecting_progress = tqdm(range(start, end + 1))
    for port in port_detecting_progress:
        sock = socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            # print('port open--> ', port)
        sock.close()
    [print('\nport open--> ' + str(port)) for port in open_ports]
    with open('result_detect_open_ports.txt', 'a') as file:
        file.write('\nhost {} open ports from {} to {}:'.upper().format(ip, start, end))
        [file.write('\nport open--> ' + str(port)) for port in open_ports]
        if not open_ports:
            file.write('\nno open ports was founded!'.upper())
        file.write('\n----------------------------------------------------\n')

if __name__ == '__main__':
    ip = input('Enter ip address: ')
    start = int(input('Enter the start port: '))
    end=int(input('Enter the end port: '))
    detect_open_ports(ip, start, end)

