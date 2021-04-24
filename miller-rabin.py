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

if __name__ == "__main__":
    p = 7027512885733530016359556978643093231582954207841332111905808642699557153626390237775609216963153402372191506145964908096508381886619583684719784160767227108414535388896003633023991038274164443178033663767963330924673697484404710797497413899890903302350063
    
    print(MillerRabin(p))
    print(MillerRabin(7*p))
    print(MillerRabin(3*p))