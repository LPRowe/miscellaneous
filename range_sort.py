import heapq
import random
import time

def merge(bins, N):
    res = []
    h = [(b[-1], i) for i, b in enumerate(bins)]
    for _ in range(N):
        val, i = heapq.heappop(h)
        res.append(val)
        if bins[i]:
            heapq.heappush(h, (bins[i].pop(), i))
    print(len(bins))
    return res

def time_it(func):
    def wrap(*args, **kwargs):
        t0 = time.time_ns()
        res = func(arr)
        tf = time.time_ns()
        print(func.__name__, int((tf - t0) * 1e-6), 'ms')
        return res
    return wrap

@time_it
def range_sort(arr):
    bins = []
    for i in range(len(arr)):
        for j in range(len(bins)):
            if bins[j][-1] >= arr[i]:
                bins[j].append(arr[i])
                break
        else:
            bins.append([arr[i]])
    
    return merge(bins, len(arr))

@time_it
def tim_sort(arr):
    return sorted(arr)

if __name__ == "__main__":
    N = 30
    arr = [random.randint(0, 10*N) for _ in range(N)]
    
    print(range_sort(arr))
    
    print(tim_sort(arr))
    
    

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @functools.lru_cache(None)
        def helper(i, total):
            if i == len(nums):
                return int(total == target)
            return helper(i+1, total + nums[i]) + helper(i+1, total - nums[i])
        
        return helper(0, 0)
            