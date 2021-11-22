'''Simple RSA implementation without using any packages.  only defining bunch of functions to do so.'''
import random


'''
Using Euclid's Algorithm to find the gcd of two numbers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of a number in modulo phi
'''
def multiplicative_inverse(e,r):
    for i in range(r):
        if((e*i)%r == 1):
            return i
'''
function to check if a number is prime
'''

def check_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)):
        if num % n == 0:
            return False
    return True

'''public and private key generation'''

def key_gen_rsa(p, q):
    if not (check_prime(p) and check_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    phi = (p-1) * (q-1)

    #we have to choose  an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #check if e and phi are coprime or not
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    
    return ((e,n),(d,n))

'''encryption'''

def encrypt(pk, plaintext):

    key, n = pk
    
    cipher_text = [(ord(char) ** key) % n for char in plaintext]
    
    return cipher_text


'''decryption'''

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    
    return ''.join(plain)
    

if __name__ == '__main__':
    print ("RSA Encryption Algorithm")
    p = int(input("Enter a prime number : "))
    q = int(input("Enter another prime numbe : "))
    public, private = key_gen_rsa(p, q)
    print ("Your public key is ", public ," and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print ("Your encrypted message is: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("After decrypting Your message is:")
    print (decrypt(public, encrypted_msg))
