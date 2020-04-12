
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
#for more info look here: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
#will also be explained in class
def get_d(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p*q
    z = (p-1)*(q-1)
    e = 0
    while(gcd(e, z)!=1):
        e = random.randrange(1, z)
    d = get_d(e, z)
    return ((e, n), (d, n))

    

def encrypt(pk, plaintext):
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    d = pk[0]
    n = pk[1]
    cipher = pow(ord(plaintext), d, n)
    return cipher

def decrypt(pk, ciphertext):
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    e = pk[0]
    n = pk[1]
    plain = chr(pow(ciphertext, e, n))
    return ''.join(str(plain))
    