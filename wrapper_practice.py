import time

def timer(func):
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        res = func(*args, **kwargs)
        print(time.time_ns() - t0, 'ns')
        return res
    return wrapper

@timer
def test_func(n):
    for i in range(n):
        continue
    return None

def cache(func):
    memo = dict()
    def wrapper(*args, **kwargs):
        nonlocal memo
        m = tuple(tuple([i]) for i in args) + tuple(tuple([k]) for k in kwargs)
        if m in memo:
            print("hit")
            return memo[m]
        res = func(*args, **kwargs)
        memo[m] = res
        return res
    return wrapper

@cache
def one_up(n):
    return n+1
    
if __name__ == "__main__":
    print(one_up(1))
    print(one_up(1))
    print(one_up(1))
    print(one_up(10))
    print()
    