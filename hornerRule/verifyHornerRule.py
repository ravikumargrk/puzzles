# T. Cormen | Page#80 | 2.3 Correctness of Horner's rule

import random
import time

N = 10000 # degree of polynomial
x = 3     # where to evaluate 

# randomly generate polynomial
coeff = [random.randint(1, 100) for _ in range(N)] 

# naive evaluation of polynomial
def naive_poly(coeff, x):
    t0 = time.time()
    s = 0
    for i in range(len(coeff)):
        s += coeff[i]*(x**i)
    dt = time.time() - t0
    return dt, s

# horner's evaluation of polynomial
def horner(coeff, x):
    t0 = time.time()
    s = 0
    for c in coeff[::-1]:
        s = s*x + c
    dt = time.time() - t0
    return dt, s
  
horner_t, horner_s = horner(coeff, x)
naive_t, naive_s = naive_poly(coeff, x)

print('Error  : ', naive_s-horner_s)
print('time taken by horner : ', round(horner_t, 3))
print('time taken by naive  : ', round(naive_t, 3))

