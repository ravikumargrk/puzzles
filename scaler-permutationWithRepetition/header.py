import itertools as it

def grid(nums, dim):
    """ creates a grid (x1, x2, ..., xn)
        \nwhere n=dim (dimension)
    """
    # base case
    iters = tuple([nums for i in range(dim)])
    return [t for t in it.product(*iters)]

# splits N into parts each part >=1 
# example split(10, 2) = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]
def split(N, parts):
    max_nums = N - parts + 1
    nums = [i for i in range(1, max_nums+1)]
    result = [t for t in grid(nums, parts) if sum(t)==N]
    return result

