# Pollard's Rho algorithm to decrypt rsa.

import math
import time
from rsa import RSA

def f(x):
    return x * x + 1

"""
Pollard's rho algorithm

@param n the RSA ciphering modulus
"""
def rho_pollard(n, x1 = 2):
    x = x1
    y = f(x) % n
    p = 1
    start_time = time.perf_counter()

    while p == 1:
        x = f(x) % n
        y = f(f(y)) % n
        p = math.gcd(abs(x - y), n)
        if(time.perf_counter() - start_time > 20):
            return -1

    if p == n:
        return -1
    else:
        return p

def crack_primes(n):
    p = rho_pollard(n)

    if p == -1:
        return None

    q = n // p
    return (p, q)

def crack_msg(msg, n):
    primes = crack_primes(n)

    if not primes:
        print("Could not crack message with Pollard's rho algorithm")
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

    print(10 * '*', "Cracking with Pollard's rho algorithm", 10 * '*')
    cracked_msg = crack_msg(encrypted_msg, r.n)
    print("Got:", cracked_msg)
    print("Success!" if cracked_msg == original_msg else "Failure.")
