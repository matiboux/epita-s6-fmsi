# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:33:33 2021

@author: Matiboux
"""

import math

"""
Generate RSA ciphering keys

Involved prime numbers need to be distinct.
Output is a couple of public, private keys.

@param p prime number
@param q prime number
"""
def generate_keys_rsa(p, q):

	n = p * q
	phi = (p - 1) * (q - 1)

	# Find an integer matching the predicate
	def findint(x, predicate):

		def rfind(x):
			if predicate(x): return x
			return rfind(x + 1)
		
		return rfind(x)
	
	# Compute the inverse of x modulo phi
	def inverse(x, phi):
		val = 1
		while (x * val) % phi != 1: val += 1
		return val
	
	e = findint(2, lambda x : math.gcd(x, phi) == 1)
	d = inverse(e, phi)
	return ((n, e), (n, d))

"""
RSA encryption

@param m integer encoding of clear message
@param n
@param d public exponent
"""
def encrypt_rsa(m, n, e):
	return pow(m, e, n)  # (m ** e) % n

"""
RSA decryption

@param m integer encoding of encrypted message
@param n
@param d private exponent
"""
def decrypt_rsa(m, n, d):
	return pow(m, d, n)  # (m ** d) % n
