# Suppose there are 20 different types of coupons and suppose that each time 
# one obtains a coupon it is equally likely to be any one of the types. 
# Compute the expected number of different types that are contained in the set for 10 coupons.

def getComb(terms, nums):
    new = []
    for t in terms:
        for i in nums:
            new.append(t+[i])
    return new
    
def getAll(dim):
    nums = range(1, 10-dim+2)
    if dim == 1:
        return [[i] for i in range(1,11)]
    else:
        terms = [[i] for i in range(1,11)]
        for i in range(dim-1):
            terms = getComb(terms, nums)
    return terms

def getComb10(r):
    terms = getAll(r)
    terms10 = []
    for t in terms:
        if sum(t) == 10:
            terms10.append(t)
    return terms10

import math

def P(r):
    pre = math.comb(20, r)*math.factorial(10)/(20**10)
    s = 0
    for t in getComb10(r):
        p = 1
        for e in t:
            p = p * math.factorial(e)
        s += 1/p 
    return pre*s

# print(getComb10(10))

probs = [(r,P(r)) for r in range(1,11)]

print('r\tP(r)')
exp = 0
for r, p in probs:
    exp += r*p
    print('{}\t{}'.format(r, p))

print('\nExpectation = ', exp)

# OUPUT:
# @ravikumargrk ➜ /workspaces/puzzles (main) $ python main.py 
# r       P(r)
# 1       1.953125e-12
# 2       1.8962890624999996e-08
# 3       6.2321484375e-06
# 4       0.00038727826171874966
# 5       0.007726260937499996
# 6       0.06221070843749998
# 7       0.2243477249999999
# 8       0.37200515625
# 9       0.2678437125
# 10      0.0654729075

# Expectation =  8.02526121523242