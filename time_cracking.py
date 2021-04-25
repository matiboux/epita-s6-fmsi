# import matplotlib.pyplot as plt
# import numpy as np
import genPrime as prim
import rho_pollard as rho
import fermat as ferm
import miller_rabin as mil
from rsa import RSA
import time

def time_crack(func, max_prime):
    era = prim.erathosthene(max_prime)
    sucess = 0
    failed = 0
    time_array = []
    prime_array = []

    for i in range(1,len(era),6):
        start_time = time.perf_counter()
        r = RSA.generate(era[i-1],era[i])
        n = r.n
        cracked = func(n)
        
        if(not cracked):
            print("Couldn't crack p = " + str(era[i-1]) + " q = " +str(era[i]))
            failed += 1
        else:
            time_used =   round(time.perf_counter() - start_time,4)
            prime_array.append(n)
            time_array.append(time_used)

            p,q = cracked
            print("p = " + str(p) + " q = " + str(q) + " --- %s seconds ---" % time_used)
            sucess += 1

    print("Sucess rate: " + str(sucess) + "/" + str(failed))
    print(time_array)
    print(prime_array)
    return time_array, prime_array

if __name__ == "__main__":
    time_crack(rho.crack_primes,10000)
    # time_crack(ferm.crack_primes,1000)
    # p = mil.generate_prime(32)
    # q = mil.generate_prime(32)
    # print("p = " + str(p) + " q = " + str(q) )
    # n = p*q
    # start_time = time.perf_counter()
    # cracked = ferm.crack_primes(n)
    # time_used =   round(time.perf_counter() - start_time,4)
    # p,q = cracked
    # print("p = " + str(p) + " q = " + str(q) + " --- %s seconds ---" % time_used)
