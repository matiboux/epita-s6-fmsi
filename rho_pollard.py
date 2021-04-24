# Pollard's Rho algorithm to decrypt rsa.

import math
from rsa import RSA

def f(x):
    return x * x + 1

def rho_pollard(n):
    x = 2
    y = 2
    p = 1

    while p == 1:
        x = f(x)
        y = f(f(y))
        p = math.gcd(abs(x - y), n)

    if p == n:
        return -1
    else:
        return p

def crack_primes(n):
    p = rho_pollard(n)

    if p == -1:
        print("Could not crack message with Rho Pollard")
        return None

    q = n // p
    return (p, q)

def crack_msg(msg, n):
    primes = crack_primes(n)

    if not primes:
        return None

    p, q = primes
    r = RSA.generate(p, q)

    return r.decrypt(msg)

if __name__ == "__main__":
    r = RSA.generate(661, 673)

    msg_enc = r.encrypt("426916")
    msg_dec = crack_msg(msg_enc, r.n)

    print(msg_dec)
