# -*- coding: utf-8 -*-

def is_prime(n):

    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5) 
    f = 5

    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6

    return True

def erathosthene(n):

    res = [True] * n
    res_p = []
    res[0] = False
    res[1] = False
    for i in range(4, n, 2):
        res[i] = False

    if n < 2:
        return []

    res_p.append(2)
    i = 3

    while i * i <= n:
        if res[i]:
            res_p.append(i)
            for j in range(i * i, n, 2 * i):
                res[j] = False
        i += 1

    for j in range(i, n):
        if res[j]:
            res_p.append(j)

    return res_p

if __name__ == "__main__":
    table = erathosthene(1000)
    count = 0

    for n in table:
        assert(is_prime(n))
