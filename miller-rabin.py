# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 00:05:00 2021

@author: Bastien
"""

import random


def MillerRabin(p, limit = 40):
      
    petits_premiers = [2,3,5,7,11,13,17,19]
    
    if (p in petits_premiers):
        return True
    
    if (p%2 == 0):
        return False
    
    s = 0
    d = p - 1
    
    while d % 2 == 0:
        s += 1
        d //= 2
    
    for i in range(limit):
        a = random.randint(2, p - 1)
        x = pow(a, d, p)
        
        if x == 1 or x == p - 1:
            continue
        
        for r in range(s-1):
            x = pow(x, 2, p)
            
            if x == 1:
                return False
            if x == p - 1:
                continue
            
        return False
    
    return True

def generate_prime(bit):
    n = random.randint(2**(bit-1), 2**bit) | 1
    s = 2 * n
    
    while not MillerRabin(n):
        
        for i in range(2, s, 2):
            if (MillerRabin(n + i)):
                return n + i
         #si l'incrément rate on génère un nouveau nombre    
        n = random.randint(2**(bit-1), 2**bit)
    
    return n

if __name__ == "__main__":
    p = generate_prime(64)    
    print(p)