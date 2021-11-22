import random
def isPrime(x) :
    for i in range(2,x):
        if(x%i) == 0 :
            prime = False
        else :
            prime = True
    return prime

def gcd(a,b) :
    while b!= 0 :
        b = a%b
        a = b
    return a

def multiplicative_inverse(e, phi):
    m0 = phi
    y = 0
    x = 1

    if phi == 1 :
        return 0
    while(e>1):
        q = e//phi
        t = phi
        phi = e%phi
        e = t
        t = y
        y = x - q*y
        x = t
        if (x<0) :
            x = x + m0
        return x






   
def generate_keypair(p, q):
    if not (isPrime(p) and isPrime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = p*q
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    print("e =  ",e)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    print("d = ",d)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))




public,private = generate_keypair(13,17)

