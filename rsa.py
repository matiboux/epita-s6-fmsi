# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:33:33 2021

@author: Matiboux
"""

import math

class RSA:

	"""
	Constructor of the RSA ciphering object

	# @param pub_key the public key
	# @param priv_key the private key
	"""
	def __init__(self, pub_key, priv_key = None):
		self.pub_key = pub_key
		self.priv_key = priv_key

	"""
	Encrypt a message using the public key

	@param m integer encoding of the message
	"""
	def encrypt(self, m):
		return pow(m, self.pub_key[1], self.pub_key[0])  # (m ** e) % n

	"""
	Decrypt a message using the private key

	@param m integer encoding of the encrypted message
	"""
	def decrypt(self, m):
		return pow(m, self.priv_key[1], self.priv_key[0])  # (m ** d) % n

	"""
	Generate RSA ciphering keys and object

	Involved prime numbers need to be distinct.
	Returns an object containing a couple of public and private keys.

	@param p prime number
	@param q prime number
	"""
	@classmethod
	def generate(cls, p, q):
		(pub_key, priv_key) = cls.generate_keys(p, q)
		return cls(pub_key, priv_key)

	"""
	Generate RSA ciphering keys

	Involved prime numbers need to be distinct.
	Returns a couple of public and private keys.

	@param p a prime number
	@param q a prime number
	"""
	@staticmethod
	def generate_keys(p, q):
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
