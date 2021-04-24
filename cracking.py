# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import math
import rsa


def n_minus_one(n, B):

    a = 2
    
    for j in range(2, B + 1):
        a = pow(a, j, n)
        d = math.gcd(a - 1, n)
        
    if d > 1 and d < n:
        return d
    else:
        return -1
    
def crack_primes(n):
    i = 2
    r = n_minus_one(n, i)
    
    while r == -1:
        r = n_minus_one(n, i)
        i += 1
        
        if (i > 2**16):
            return None
    p = r
    q = n // r
    return (p, q)
        
def crack_msg(msg, n):
    primes = crack_primes(n)
    
    if primes == None:
        print("Could not crack message")
        return None
    
    p,q = primes
    r = rsa.RSA.generate(p,q)
    
    return r.decrypt(msg)    
 

def message_to_int(a_string):
    
    a_byte_array = bytearray(a_string, "utf8")
    
    return int.from_bytes(a_byte_array, byteorder='big')

def int_to_message(msg):
    
    byte  = msg.to_bytes((msg.bit_length() + 7) // 8, byteorder='big')
    return byte.decode("utf-8")

if __name__ == "__main__":
    original = "hello world!!"
    message = message_to_int(original)

    r = rsa.RSA.generate(661, 673)
    m = r.encrypt(message)
    
    print(10 *"*" + "Cracking" + 10 * "*")
    msg = crack_msg(m, r.n)
    print("got:", int_to_message(msg))
    print("original:", original)