# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:55:53 2021

@author: Bastien
"""

import math
from rsa import RSA

def factorisation_fermat(n):
    
    if (n % 2 == 0):
        return - 1
    
    A = math.ceil(math.sqrt(n))
    Bsq = A*A - n
    
    sq = math.sqrt(Bsq)
    
    while sq * sq != Bsq:
        A = A + 1
        Bsq = A * A - n
        sq = math.sqrt(Bsq)
        
    return (int)(A - sq)


def crack_primes(n):
    p = factorisation_fermat(n)

    if p == -1:
        return None

    q = n // p
    return (p, q)

def crack_msg(msg, n):
    primes = crack_primes(n)

    if not primes:
        print("Could not crack message with  Fermat factorisation algorithm")
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

    print(10 * '*', "Cracking with Fermat factorisation", 10 * '*')
    cracked_msg = crack_msg(encrypted_msg, r.n)
    print("Got:", cracked_msg)
    print("Success!" if cracked_msg == original_msg else "Failure.")
