# -*- coding: utf-8 -*-

import math
from rsa import RSA

"""
Pollard's p-1 algorithm

@param n the RSA ciphering modulus
@param b the limit for iterating
"""
def p_minus_one(n, b):

    a = 2
    
    for j in range(2, b + 1):
        a = pow(a, j, n)
        d = math.gcd(a - 1, n)
        
    if d > 1 and d < n:
        return d
    else:
        return -1
    
def crack_primes(n):
    i = 2
    r = p_minus_one(n, i)
    
    while r == -1:
        r = p_minus_one(n, i)
        i += 1
        
        if (i > 2 ** 12):
            return None

    p = r
    q = n // r
    return (p, q)
        
def crack_msg(msg, n):
    primes = crack_primes(n)
    
    if primes == None:
        print("Could not crack message with Pollard's p-1 algorithm")
        return None
    
    (p, q) = primes
    r = RSA.generate(p, q)
    
    return r.decrypt(msg)

if __name__ == "__main__":
    original_msg = "Hello, world! This is my very secret message."
    print("Encrypting:", original_msg)

    r = RSA.generate(661, 673)
    encrypted_msg = r.encrypt(original_msg)
    # print("Encrypted data:", encrypted_msg)

    print(10 * '*', "Cracking with Pollard's p-1 algorithm", 10 * '*')
    cracked_msg = crack_msg(encrypted_msg, r.n)
    print("Got:", cracked_msg)
    print("Success!" if cracked_msg == original_msg else "Failure.")
