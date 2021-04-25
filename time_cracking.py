import matplotlib.pyplot as plt
import numpy as np
import genPrime as prim
import rho_pollard as rho
import fermat as ferm
from rsa import RSA
import time
def time_pollard(func):
    era = prim.erathosthene(1000)
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
    #time_pollard(rho.crack_primes)
    #time_pollard(ferm.crack_primes)
