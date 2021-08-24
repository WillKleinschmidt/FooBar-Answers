import numpy as np

def solution(i):

    # Making string of primes using Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    
    p = 105000 
    A = [1] * p # A: 0 = non-primes, 1 = primes
    A[0] = 0
    A[1] = 0
    for n in range(0, int(np.sqrt(p))):
        if(A[n] == 1):
            for m in range(n**2, p):
                if((m-n**2)%n == 0):
                    A[m] = 0
    P = []
    for n in range(0, p):
        if(A[n] == 1):
            P.append(n)
            
    id_list = ""
    j = 0;
    while len(id_list) < 10005:
        id_list = id_list + str(P[j])
        j = j + 1
    return id_list[i:i+5]
