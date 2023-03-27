import platform
import os

def ping(host, count=1):

    count_param = '-c {} '.format(count) if platform.system().lower() != 'windows' else '-n {} '.format(count)
    command = 'ping {}{}'.format(count_param, host)
    print('> ' + command + '\n...')
    ping_result = os.popen(command).read()
    with open('result_ping.txt', 'a') as file:
        file.write('\n> {}'.upper().format(command))
        file.write('\n{}'.format(ping_result.replace('\n\n', '\n')))
        file.write('------------------------------------------------------------------------------------\n')

    print(ping_result)
    if '1 packets transmitted, 1 packets received, 0.0% packet loss' in ping_result:
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    host=input('HOST : ')
    count=int(input('COUNT: '))
    ping(host, count)
