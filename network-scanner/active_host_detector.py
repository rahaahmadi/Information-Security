import socket
import ipaddress
from ping import ping

def detect_active_hosts(network, steps):
    print('Scanning in Progress...')
    active_hosts = []
    for index in range(steps + 1):
        ip = str((network + index))
        host = socket.gethostbyname(ip)
        is_active  = ping(host, 1)
        if is_active:
            print(ip + ' --> ' + 'Live')
            active_hosts.append(ip)
    with open('result_detect_active_hosts.txt', 'a') as file:
        file.write('\nactive hosts in range [{} - {}]:'.upper().format(network, str((network + index))))
        [file.write('\n' + host + ' --> ' + 'Live') for host in active_hosts]
        if not active_hosts:
            file.write('\nno active host was founded!'.upper())
        file.write('\n----------------------------------------------------------\n')


if __name__ == '__main__':
    network = ipaddress.ip_address(input('Enter the Network Address: '))
    startingPoint = int(input('Enter the Starting Number: '))
    network += startingPoint
    steps = int(input('Enter the Last Number: ')) - startingPoint
    detect_active_hosts(network, steps)
