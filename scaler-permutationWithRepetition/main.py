# Suppose there are 20 different types of coupons and suppose that each time 
# one obtains a coupon it is equally likely to be any one of the types. 
# Compute the expected number of different types that are contained in the set for 10 coupons.

from header import split
import math

# number of ways to permute objects in a sample
# containing "sample_size" number of "sample_types" different types of objects 
# selected from infinite number of "max_types" different types of objects
def N(max_types, sample_size, sample_types):
    select = math.comb(max_types, sample_types)
    perms = 0
    for t in split(sample_size, sample_types):
        p = 1
        for e in t:
            p = p * math.factorial(e)
        perms += math.factorial(10)/p 
    return select*perms

n_sample = (20**10)
probs = [(r, N(20, 10, r)/n_sample) for r in range(1,11)]

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