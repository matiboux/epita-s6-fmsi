# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:33:33 2021

@author: Matiboux
"""

import math

class RSA:

	"""
	Constructor of the RSA ciphering object

	@param pub_key the public key
	@param priv_key the private key
	"""
	def __init__(self, pub_key, priv_key = None):
		assert(type(pub_key) is tuple)
		if priv_key:
			assert(type(pub_key) is tuple)
			assert(pub_key[0] == priv_key[0])

		self.n = pub_key[0]
		self.e = pub_key[1]
		self.d = priv_key[1]

	"""
	Return the RSA public key
	"""
	def pub_key(self):
		return (self.n, self.e)

	"""
	Return the RSA private key
	"""
	def priv_key(self):
		return (self.n, self.d)

	"""
	Encrypt a message using the public key

	@param m integer encoding of the message
	"""
	def encrypt(self, m):
		# (m ** e) % n
		return pow(m, self.e, self.n)

	"""
	Decrypt a message using the private key

	@param m integer encoding of the encrypted message
	"""
	def decrypt(self, m):
		# (m ** d) % n
		return pow(m, self.d, self.n)

	"""
	Generate RSA ciphering keys and object

	Involved prime numbers need to be distinct.
	Returns an object containing a couple of public and private keys.

	@param p prime number
	@param q prime number
	"""
	@classmethod
	def generate(cls, p, q):
		# Generate RSA ciphering keys
		(pub_key, priv_key) = cls.generate_keys(p, q)
		# Instantiate an object
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

		# Compute the public and private exponents
		e = findint(2, lambda x : math.gcd(x, phi) == 1)
		d = inverse(e, phi)

		return ((n, e), (n, d))
