"""
This program finds a set of 5 or less pyramidal numbers that sum to x for all x in range [1, N].  

A pyramidal number is defined as: f(num) = (num**3 - num) / 6

Typical SOLVE_ALL runtimes are of 1.4 seconds for N = 10 ** 6
                                   15 seconds for N = 10 ** 7
                                  180 seconds for N = 10 ** 8
"""

import bisect
import time
import matplotlib
import matplotlib.pyplot as plt

def timer(func):
    """Returns runtime of func in ms"""
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        res = func(*args, **kwargs)
        tf = time.time_ns()
        print(f"{func.__name__}: {int((tf - t0)*(1e-6))} ms")
        return res
    return wrapper

@timer
def pyramidal_nums(n):
    """
    Returns a list of all pyramidal numbers less than or equal to n
    A pyramidal number is defined as: f(num) = (num**3 - num) / 6
    """
    res = [1]
    for i in range(3, n):
        p = (i**3 - i) // 6
        if p < n:
            res.append(p)
        else:
            return res

@timer
def waring_pyramidal_nums(N, shortest = False):
    """
    Finds sets of 5 or less pyramidal numbers that sum to x for x in range [1, N].
    Returns None
    Fills memo where sum(memo[x]) equals x and memo[x] contains 5 or less pyramidal numbers
    memo: List[List[p1, p2, p3, p4, p5], ..., List[p1, p2, p3, p4, p5]]
    
    i.e. memo = [[], [1], [1,1], [1,1,1], [4], [1,4], ..., [p1, p2, p3, p4, p5]]
                 0    1     2       3      4     5                  N
                 
    Note: When shortest is true, the function will find the minimum such pyramidal numbers that sum to x.
          memo[x] will be of length 4 if 4 is the smallest number of pyramidal numbers that can form x.
          
          When shortest is false, the time complexity is greatly reduced, but some x that can be expressed
          with 4 pyramidal numbers will be expressed with 5 pyramidal numbers instead.
    """
    global memo, nums
    
    for num in nums:
        memo[num].append(num)
    print("ones", len(nums))
    
    # Find all numbers that can be created by summing 2 pyramidal numbers together
    pairs = set()
    for i in range(len(nums)):
        for j in range(i+1):
            p = nums[i] + nums[j]
            if p > N: break
            if not memo[p]:
                memo[p] = [nums[j], nums[i]]
                pairs.add(p)
    print("pairs", len(pairs))
    
    # Find all numbers that can be created by summing 3, 4, or 5 pyramidal numbers together
    if shortest:
        triplets = set()
        for p in pairs:
            for i in range(len(nums)):
                t = nums[i] + p
                if t > N: break
                if not memo[t]:
                    memo[t] = memo[p] + [nums[i]]
                    triplets.add(t)
        print("trips", len(triplets))
        
        quadruplets = set()
        for t in triplets:
            for i in range(len(nums)):
                q = nums[i] + t
                if q > N: break
                if not memo[q]:
                    memo[q] = memo[t] + [nums[i]]
                    quadruplets.add(q)
        print("quads", len(quadruplets))
        
        quintuplets = set()
        for quad in quadruplets:
            for i in range(len(nums)):
                q = nums[i] + quad
                if q > N: break
                if not memo[q]:
                    memo[q] = memo[quad] + [nums[i]]
                    quintuplets.add(q)
        print("quints", len(quintuplets))
        total = len(nums) + len(pairs) + len(triplets) + len(quadruplets) + len(quintuplets)
    else:
        triplets = 0
        for p in pairs:
            for i in range(len(nums)):
                t = nums[i] + p
                if t > N: break
                if not memo[t]:
                    memo[t] = memo[p] + [nums[i]]
                    triplets += 1
        print("trips", triplets)
        
        quadruplets = 0
        pair_list = list(pairs)
        for i in range(len(pair_list)):
            for j in range(i+1):
                q = pair_list[i] + pair_list[j]
                if q > N: break
                if not memo[q]:
                    memo[q] = memo[pair_list[j]] + memo[pair_list[i]]
                    quadruplets += 1
        print("quads", quadruplets)
        
        quintuplets = 0
        for num in range(1, len(memo)):
            if not memo[num]:
                for j in range(bisect.bisect_left(nums, num)):
                    if memo[num - nums[j]]:
                        memo[num] = memo[num - nums[j]] + [nums[j]]
                        if len(memo[num]) == 5:
                            quintuplets += 1
                        else:
                            quadruplets += 1
                        break
        print("quads", quadruplets)
        print("quints", quintuplets)
        total = len(nums) + len(pairs) + triplets + quadruplets + quintuplets
    
    print('\nFound:',total,'/',N)
    
def inspect_range(i, j):
    """
    prints n, sum(memo[n]), memo[n] for n in range [i, j]
    """
    print()
    print("A few example solutions:\n------------------------")
    print("x".ljust(len(str(i))),"total".ljust(len(str(i))),"memo[x]")
    for x in range(max(0, i), min(len(memo), j+1)):
        print(x, sum(memo[x]), memo[x])
        
def plot_runtimes(low, high):
    global memo, nums
    matplotlib.rc("font", size = 7)
    size = [10**p for p in range(low, high+1)]
    runtimes = [0]*len(size) # ms
    for i, N in enumerate(size):
        nums = pyramidal_nums(N)
        memo = [[] for _ in range(N+1)]
        t0 = time.time_ns()
        waring_pyramidal_nums(N, direct = False)
        tf = time.time_ns()
        runtimes[i] = (tf - t0)*(10**-6)
        print("Finishing",N,int(tf - t0)*(10**-6))
    
    size.append(10**8)
    runtimes.append(181463)
    
    plt.close('all')
    plt.figure()
    plt.loglog(size, runtimes)
    plt.xlabel("N")
    plt.ylabel("Runtime [ms]")
    plt.title("Runtime versus Solution Range")
    
    return size, runtimes
        
def record(name):
    """
    Save the solutions for memo[x] = p1 + p2 + p3 + p4 + p5
    Each line in file "{name}" will appear as:
        x,p1,p2,p3,p4,p5
        x,p1,p2,p3
        x,p1,p2,p3,p4
    """
    global memo
    with open(name, 'w') as fd:
        while memo:
            if len(memo) % 10000 == 0:
                print(len(memo))
            fd.write(str(len(memo)))
            for item in memo.pop():
                fd.write(f",{item}")
            fd.write("\n")

@timer        
def solve_single(x):
    global memo, nums
    
    def helper(target, path):
        nonlocal P, res
        if res or target < 0 or len(path) == 5:
            return None
        if target in P:
            res = path + [target]
            return None
        j = min(len(nums) - 1, bisect.bisect_left(nums, target))
        for i in range(j, -1, -1):
            helper(target - nums[i], path + [nums[i]])
            
    res = []
    P = set(nums)
    helper(x, [])
    return res
    
if __name__ == "__main__":
    SOLVE_ALL = False       # Find solutions for x in range [1, N]
    SAVE = False            # Save solutions in the format x,p1,p2,p3,p4,p5
    N = 10**6
    
    PLOT_RUNTIMES = False   # Plot a loglog comparison of runtimes vs N
    A, B = 1, 7             # Plots runtimes for N = [10**a, ..., 10**b] inclusive
    
    SOLVE_RANGE = True      # Find solutions for x in range [a, b] where 1 <= a <= b <= N
    START, SIZE = 10**20, 5 # sove for range [START, START + SIZE]
    
    if SOLVE_ALL:
        nums = pyramidal_nums(N)                    # All pyramidal numbers in the range [1, N]
        memo = [[] for _ in range(N+1)]             # Solutions: memo[x] = [p1, p2, p3] and p1 + p2 + p3 = x
        waring_pyramidal_nums(N, shortest = False)  # shortest = True (slow to run) but gets the shortest solution for each x
        inspect_range(N//2, min(N+1, N//2 + 5))
        if SAVE: record(f"{N}_waring_pyramid.txt")
        
    elif PLOT_RUNTIMES:
        # Plot runtime vs N for N in range [10**a, 10**b]
        A, B = 1, 7
        size, runtimes = plot_runtimes(A, B)
    
    if SOLVE_RANGE:
        # Find a solution for x = p1 + p2 + p3 + p4 + p5 for x <= 10**20
        nums = pyramidal_nums(START + SIZE)
        for x in range(START, START + SIZE + 1):
            ans = solve_single(x)
            print(x, ans,'\n')