
def quad(x):
    return (-1 + math.sqrt(1 + 4 * x)) / 2


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import math
    
    n = 1000
    n2 = 2*n
    j = [quad(n2 + i*i + i) for i in range(n)]
    a = [k - int(k) for k in j]
    
    slope = lambda dx, dy: dy / dx
    
    m = [slope(1, a[i] - a[i-1] if a[i] < a[i-1] else a[i-1] + 1 - a[i]) for i in range(1, len(a))]
    m = [k if k > 0 else -k for k in m]
    
    
    plt.close('all')
    plt.figure()
    plt.semilogy(m)
    plt.ylabel("slope")
    plt.xlabel("i")
    
    
    