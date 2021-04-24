# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import math

def n_minus_one(n, B):

    a = 2
    
    for j in range(2, B + 1):
        a = pow(a, j, n)
        d = math.gcd(a - 1, n)
        
    if d > 1 and d < n:
        return d
    else:
        return -1
