# -*- coding: utf-8 -*-

import math

class RSA:

	"""
	Constructor of the RSA ciphering object

	@param pub_key the public key
	@param priv_key the private key
	"""
	def __init__(self, pub_key, priv_key = None):
		assert(isinstance(pub_key, tuple))

		self.n = pub_key[0]
		self.e = pub_key[1]
		self.d = None

		if priv_key:
			assert(isinstance(pub_key, tuple))
			assert(pub_key[0] == priv_key[0])

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
	Encrypt an integer using the public key

	@param m integer
	"""
	def encrypt_int(self, m):
		# (m ** e) % n
		return pow(m, self.e, self.n)

	"""
	Encrypt a message using the public key

	@param m the message
	"""
	def encrypt(self, m, encoding = "utf-8"):
		if self.e is None:
			return None  # Not capable of encrypting

		# Convert the string into an array of bytes
		bstr = bytes(m, encoding)

		# Encrypt each byte of the string individually
		E = []
		for c in bstr:
			E.append(self.encrypt_int(c))

		return E

	"""
	Decrypt an integer using the private key

	@param m encrypted integer
	"""
	def decrypt_int(self, m):
		# (m ** d) % n
		return pow(m, self.d, self.n)

	"""
	Decrypt an array of integers using the private key

	@param m an array of encrypted integers
	"""
	def decrypt(self, m, encoding = "utf-8"):
		if self.d is None:
			return None  # Not capable of decrypting

		s = ""
		for v in m:
			# Decrypt each integer
			c = self.decrypt_int(v)
			s += chr(c)

		return s

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
