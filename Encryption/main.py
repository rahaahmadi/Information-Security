import os
import pbkdf2
import binascii
import secrets
import pyaes


def generate_key(initial_key):
    salt = os.urandom(16)
    key = pbkdf2.PBKDF2(initial_key, salt).read(32)
    print('Algorithm key is:', binascii.hexlify(key))
    write_to_file('key.txt', 'wb', key)
    return key

def encrypt(plaintext, key):
    iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted text is:', binascii.hexlify(ciphertext))
    write_to_file('IV.txt', 'w', str(iv))
    write_to_file('ciphertext.txt', 'wb', ciphertext)
    return iv, ciphertext

def decrypt(ciphertext, key, iv):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted text is:', decrypted)
    return decrypted


def write_to_file(path, mode, text):
    with open(path, mode) as f:
        return f.write(text)    

def read_file(path, mode):
    with open(path, mode) as f:
        return f.read()


if __name__ == '__main__':

    initial_key = 'AUT*ICTSec*2022'
    key = read_file('key.txt', 'rb')

    while True:
        option = input('Enter Your Command: (G, E, D, exit, help)\n> ')
        if option == 'help':
            print('G: Generate Key\n E: Encrypt text\n D: Decrypt text')
        if option == 'G':
            key = generate_key(initial_key)
        elif option == 'E':
            plaintext = read_file('plaintext.txt', 'r')
            encrypt(plaintext, key)
        elif option == 'D':
            iv = int(read_file('IV.txt', 'r'))
            ciphertext = read_file('ciphertext.txt', 'rb')
            decrypt(ciphertext, key, iv)
        elif option == 'exit':
            break     
