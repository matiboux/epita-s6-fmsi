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

if __name__ == "__main__":
    r = RSA.generate(661, 673)
    print(r.pub_key)
    print(r.priv_key)

    n = r.pub_key[0]

    p = rho_pollard(n)
    q = n // p
    r_cracked = RSA.generate(p, q)

    msg_enc = r.encrypt(426916)
    msg_dec = r_cracked.decrypt(msg_enc)

    print(msg_dec)

