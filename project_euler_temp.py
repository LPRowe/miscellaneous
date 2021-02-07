# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:19:13 2020

@author: rowe1
"""
import functools

def gen_primes(n):
    primes = [False, False, True] + [True]*(n-3)
    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if primes[i]:
            j = i*i
            while j < len(primes):
                primes[j] = False
                j += i
    return [i for i,p in enumerate(primes) if p]

def product(subarr):
    return functools.reduce(lambda x, y: x*y, subarr)

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

def find_divisors(n, primes):
    res = []
    while n != 1:
        for p in primes:
            if not (n % p):
                res.append(p)
                n = n // p
                break
        else:
            print('fail')
            break
    return res

def total_divisors(divisors):
    c = collections.Counter(divisors)
    return functools.reduce(lambda x, y: x * (y+1), list(c.values()), 1)
    
def triangle_number(n):
    return n * (n + 1) // 2

def read_file():
    with open("temp_data.txt", "r") as f:
        lines = f.readlines()
    return lines

@functools.lru_cache(None)
def collatz_length(n):
    if n == 1:
        return 1
    if n & 1:
        return 1 + collatz_length(3*n + 1)
    else:
        return 1 + collatz_length(n // 2)

@functools.lru_cache(None)
def lattice_paths(i, j, n):
    if i == n or j == n:
        return 1
    return lattice_paths(i+1, j, n) + lattice_paths(i, j+1, n)

def word_len(string):
    return len(''.join(string))

def number_letter_counts():
    ones = word_len(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    tens = word_len(['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'])
    ten = word_len(['ten'])
    teens = word_len(['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])
    ands = word_len(['and'])
    hundreds = word_len(['hundred'])
    thousands = word_len(['onethousand'])
    return 91 * ones + 10 * ten + 100 * tens + 10 * teens + 891 * ands + 900 * hundreds + 1 * thousands

def max_path_sum_i():
    # LOAD PYRAMID
    pyramid = read_file()
    for i in range(len(pyramid)):
        pyramid[i] = pyramid[i].strip('\n')
        pyramid[i] = pyramid[i].split(' ')
        pyramid[i] = [int(j) for j in pyramid[i]]
        
    # SOLVER
    @functools.lru_cache(None)
    def pyramid_path(i, j):
        if i == 0:
            return pyramid[0][0]
        if j == len(pyramid[i]) - 1:
            return pyramid[i][j] + pyramid_path(i-1, j-1)
        elif j == 0:
            return pyramid[i][j] + pyramid_path(i-1, j)
        return pyramid[i][j] + max(pyramid_path(i-1, j), pyramid_path(i-1, j-1))    
        
    i = len(pyramid) - 1
    res = 0
    for j in range(0, len(pyramid[i])):
        res = max(res, pyramid_path(i,j))
    return res

def counting_sundays():
    
    month = [31, 28, 31, 30,
             31, 30, 31, 31,
             30, 31, 30, 31]
    
    def leap_day(year):
        if not year % 400:
            return 1
        elif not year % 100:
            return 0
        else:
            return 1 if not year % 4 else 0
    
    def days_past(m, d, y):
        
        yd = 0
        for year in range(1900, y):
            yd += 365 + leap_day(year)
        
        md = sum(month[:m-1])
        if leap_day(y) and m >= 3:
            md += 1
    
        return yd + md + d - 1
    
    def update_date(m, d, y):
        if m == 12:
            return 1, 1, y+1
        else:
            return m+1, 1, y
    
    m, d, y = 1, 1, 1901
    res = 0
    while y < 2001:
        if days_past(m, d, y) % 7 == 6:
            res += 1
        m, d, y = update_date(m, d, y)
    return res

def sum_of_divisors(a, primes):
    if a == 0:
        print("0 has no divisors")
        return 0
    
    a_naught = a
    prime_divisors = collections.defaultdict(int)
    prime_divisors[1] = 1
    while a != 1:
        for p in primes:
            if a % p == 0:
                prime_divisors[p] += 1
                a = a // p
                break
        else:
            print('fail')
            break
    
    divisors = set()
    p = list(prime_divisors)
    def helper(i, total):
        
        if i == len(p):
            divisors.add(total)
            return None
        
        for j in range(prime_divisors[p[i]] + 1):
            helper(i+1, total * (p[i] ** j))
            
    helper(0, 1)
    
    return sum(divisors) - a_naught

def amicable_numbers(n):
    primes = gen_primes(2 * n)
    
    seen = set()
    res = 0
    for a in range(2, n):
        if a in seen:
            continue
        
        b = sum_of_divisors(a, primes)
        if b != 0 and b != a:
            c = sum_of_divisors(b, primes)
            if c == a:
                res += a + b if b < n else a
                seen |= {a, b}
    
    return res

def names_scores():
    data = read_file()[0].split(',')
    data = [i.strip('"') for i in data]
    data.sort()
    
    score = dict(zip(string.ascii_uppercase, range(1, 27)))
    name_score = lambda name: sum(score[letter] for letter in list(name))
    res = sum(i * name_score(name) for i,name in enumerate(data, 1))
    return res
    

def nonabundant_sums():
    primes = gen_primes(2 * 28123)
    
    def is_abundant(n):
        return n < sum_of_divisors(n, primes)
    
    abundant_nums = [n for n in range(1, 28124) if is_abundant(n)]
    abundant_set = set(abundant_nums)
    
    total = 0
    for i in range(1, 28124):
        total += i
        for a in abundant_nums:
            b = i - a
            if b < 12:
                break
            if b in abundant_set:
                total -= i
                break
    return total

def lexicographic_permutations():
    
    nums = list(range(10))
    perms = []
    
    def helper(nums, perm):
        
        if not nums:
            perms.append(perm)
            return None
        
        for i in range(len(nums)):
            helper(nums[:i] + nums[i+1:], perm*10 + nums[i])
    
    helper(nums, 0)
    
    perms.sort()
    
    return perms


def one_thou_digit_fib_num():
    
    fib = {1 : 1,
           2 : 1}
    
    def nth_fib(n):
        if n in fib:
            return fib[n]
        fib[n] = nth_fib(n-1) + nth_fib(n-2)
        return fib[n]
    

def quadratic_primes():
    
    P = 10**7
    primes = gen_primes(P)
    prime_set = set(primes)
    
    def formula(a, b):
        return lambda n: (n**2) + (a*n) + b
    
    def is_prime(n):
        return n in prime_set
    
    def prime_streak(f):
        n = 0
        while is_prime(f(n)):
            n += 1
        return n
    
    best = 0
    res = (0, 0)
    N = 1000
    for a in range(-N, N+1):
        for b in range(-N, N+1):
            f = formula(a, b)
            s = prime_streak(f)
            if s > best:
                best = s
                res = (a, b)
    
    return res, best


def number_spiral_diagonals(N):
    
    
    def gen_spiral(N):
        
        arr = [[0 for _ in range(N)] for _ in range(N)]
        i = j = N // 2
        
        d = (-1, 0) # start facing up
        turn_right = {(-1, 0): (0, 1), # up -> right
                      (0, 1): (1, 0), # right -> down
                      (1, 0): (0, -1), # down -> left
                      (0, -1): (-1, 0)} # left -> up
        
        for n in range(1, (N**2) + 1):
            arr[i][j] = n
            
            # consider turning right (if possible)
            d2 = turn_right[d]
            i2, j2 = i + d2[0], j + d2[1]
            if arr[i2][j2] == 0:
                i, j = i2, j2
                d = d2
            else:
                i, j = i + d[0], j + d[1]
        
        return arr
    
    arr = gen_spiral(N)
    
    def sum_diagonal(arr, N):
        res = 0
        i = j = 0
        while i < N:
            res += arr[i][j]
            i += 1
            j += 1
        
        i = N-1
        j = 0
        while j < N:
            res += arr[i][j]
            i -= 1
            j += 1
        
        res -= arr[N//2][N//2]
        
        return res
    
    return sum_diagonal(arr, N)

def distinct_powers(N):
    
    nums = set()
    
    for a in range(2, N+1):
        for b in range(2, N+1):
            nums.add(a ** b)
    
    return len(nums)

def digit_nth_powers(n):
    
    res = set()
    digits = list(range(10))
    
    def helper(i, number, total):
        nonlocal n
        
        if i > 1 and number == total:
            res.add(number)
        
        if i == n+1:
            return None
        
        for d in digits:
            if i or d:
                helper(i+1, number*10 + d, total + d**n)
    
    helper(0, 0, 0)
    res -= set([1])
    return sum(res), res

def coin_sums():
    
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    @functools.lru_cache(None)
    def helper(total, j):
        if total <= 0:
            return total == 0
        
        if j == len(coins):
            return 0
        
        return helper(total - coins[j], j) + helper(total, j+1)
        
    
    return helper(target, 0)

def pandigital_products():
    
    digits = list(range(1, 10))
    
    res = set()
    
    def helper(digits, a, b, c):

        if not digits:
            if a and b and c and (a * b == c):
                res.add(c)
            return None
        
        if len(digits) > 5:
            for i in range(len(digits)):
                helper(digits[:i]+digits[i+1:], a, b, c*10 + digits[i])
        else:
            for i in range(len(digits)):
                helper(digits[:i]+digits[i+1:], a*10 + digits[i], b, c)
                helper(digits[:i]+digits[i+1:], a, b*10 + digits[i], c)
                helper(digits[:i]+digits[i+1:], a, b, c*10 + digits[i])
    
    helper(digits, 0, 0, 0)
    
    return res, sum(res)

def digit_factorials():
    
    digits = list(range(10))
    fact = [math.factorial(i) for i in digits]
    
    numbers = set()
    
    def helper(i, number, total):
        
        if i > 1 and number == total:
            numbers.add(number)
        
        if i == 7:
            return None
    
        for d in digits:
            if d or i:
                helper(i+1, number*10 + d, total + fact[d])
    
    helper(0, 0, 0)
    
    return numbers, sum(numbers)

def circular_primes(N):
    
    primes = gen_primes(N + 1)
    
    res = set()
    
    def circular(p):
        if p in res:
            return True
        
        p = str(p)
        L = len(p)
        for _ in range(L):
            p = p[-1] + p[:-1]
            if int(p) not in primes:
                return False
        
        return True
    
    for p in primes:
        if circular(p):
            res.add(p)
    
    return res, len(res)


def double_base_palindromes(N):
    
    max_len = len(bin(N)) - 2
    
    bin_palindromes = set()
    
    def helper(string, L):
        
        if len(string) == L // 2:
            if L&1:
                bin_palindromes.add(string + '0' + string[::-1])
                bin_palindromes.add(string + '1' + string[::-1])
            else:
                bin_palindromes.add(string + string[::-1])
            return None
        
        if string:
            helper(string + '0', L)
        helper(string + '1', L)

    for L in range(1, max_len + 1):
        helper('', L)
    
    def is_palindrome(binary_string):
        num = str(int(binary_string, 2))
        return num == num[::-1]
    
    res = [int(p,2) for p in bin_palindromes if is_palindrome(p)]
    
    print(bin_palindromes)
    print(res)
    return sum(res)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.tail = False
        
class Trie(object):
    def __init__(self, primes):
        self.root = Node(None)
        self.primes = primes
        self.build()
    
    def build(self):
        for p in self.primes:
            self.insert(str(p))
        
    def insert(self, string):
        curr = self.root
        for char in string:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.tail = True
        
    def is_in(self, string):
        curr = self.root
        for char in string:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.tail
        
    def find_fwd_primes(self):
        
        def helper(string, node):
            if not node.children:
                res.add(string)
                return None
            
            if len(string) > 1:
                res.add(string)
            
            for child in node.children:
                if node.children[child].tail:
                    helper(string + child, node.children[child])
        
        res = set()
        helper('', self.root)
        return res
    
    def is_rev_prime(self, prime_num):
        for i in range(1, len(prime_num)):
            if not self.is_in(prime_num[i:]):
                return False
        return True

def trunc_primes():
    N = 10**7
    primes = set(gen_primes(N))
    tree = Trie(primes)
    fwd_primes = tree.find_fwd_primes()
    res = [p for p in fwd_primes if tree.is_rev_prime(p)]
    return res, sum([int(i) for i in res])

def pandigital_multiples():
    
    pandigitals = set()
    
    def gen_candidates(nums, total):
        
        if not nums:
            pandigitals.add(total)
            return None
        
        for i in range(len(nums)):
            gen_candidates(nums[:i] + nums[i+1:], total * 10 + nums[i])
    
    gen_candidates(list(range(1, 9)), 9)
    
    res = 918273645
    
    for n in range(50000, 100000):
        p = str(n)
        mult = 2
        while len(p) < 9:
            p += str(mult * n)
            mult += 1
        else:
            if (len(p) == 9):
                p = int(p)
                if p in pandigitals:
                    print(mult - 1, n, p, res)
                    res = max(res, int(p))
    
    return res
            

def integer_right_triangles():
    
    p = 120
    
    def find_abc(p):
        res = set()
        min_c = math.ceil(p / 3)
        max_c = p // 2
        for c in range(min_c, max_c + 1):
            rem = p - c
            for a in range(1, rem):
                b = p - c - a
                if a**2 + b**2 == c**2:
                    res.add(tuple(sorted([a,b,c])))
        return res, len(res)
    
    res = (0, 0)
    
    for p in range(3, 1001):
        res = max(find_abc(p), res, key = lambda r: r[1])
    
    return res

def champernownes_constant():
    
    d = []
    N = 10**6
    
    n = 1
    while len(d) < N:
        d.extend(list(str(n)))
        n += 1
    
    prod = [10**i for i in range(7)]
    
    res = 1
    for i in prod:
        res *= int(d[i-1])
    
    return res

def pandigital_prime(primes):
    
    target = set(range(1, 10))
    
    def is_pandigital(prime):
        
        nums = set()
        while prime:
            r = prime % 10
            if r in nums:
                return False
            nums.add(prime % 10)
            prime = prime // 10
        return nums == target
    
    for i in range(len(primes) - 1, -1, -1):
        target = set(range(1, len(str(primes[i]))+1))
        if is_pandigital(primes[i]):
            return primes[i]

def coded_triangle_numbers():
    
    data = read_file()[0]
    data = data.split(',')
    data = [word.strip('"') for word in data]
    print(data)
    
    mapping = dict(zip(string.ascii_uppercase, range(1, 27)))
    word_score = [sum(mapping[letter] for letter in word) for word in data]
    print(word_score)
    print(max(word_score))
    
    triangles = [-1]
    n = 1
    while triangles[-1] < 192:
        triangles.append(n * (n + 1) // 2)
        n += 1
    triangles = set(triangles)
    
    return sum(score in triangles for score in word_score)        

def substring_divisibility():
    
    pandigitals = []
    
    def divisible(n):
        if len(n) < 4: return True
        L = len(n)
        d = dict(zip(range(4, 11), [2, 3, 5, 7, 11, 13, 17]))
        n = int(n[-3:])
        return n / d[L] == n // d[L]
    
    def gen_pandigitals(nums, number):
        
        if not nums:
            if divisible(number):
                pandigitals.append(str(number))
            return None
        
        if not divisible(number):
            return None
        
        for i,num in enumerate(nums):
            if (num != '0') or number:
                gen_pandigitals(nums[:i]+nums[i+1:], number + num)
    
    
    numbers = list(range(10))
    numbers = [str(n) for n in numbers]
    gen_pandigitals(numbers, '')
    return pandigitals, sum(int(p) for p in pandigitals)

def pentagon_numbers():
    
    def f(n):
        return n * (3 * n - 1) // 2
    
    N = 10**4
    nums = [f(i) for i in range(1, N)]
    p_set = set(nums)
    
    for i in range(len(nums) - 1):
        for j in range(i):
            if nums[i] - nums[j] in p_set:
                if nums[i] + nums[j] in p_set:
                    return nums[i], nums[j]

def tri_pen_hex():
    
    tri = lambda n: n * (n + 1) // 2
    pen = lambda n: n * (3 * n - 1) // 2
    hexa = lambda n: n * (2 * n - 1)
    
    t, p, h = [1], [1], [1]
    t_set, p_set, h_set = set(t), set(p), set(h)
    
    while True:
        #update triangular numbers
        t.append(tri(len(t) + 1))
        #t_set.add(t[-1])
        
        while p[-1] < t[-1]:
            p.append(pen(len(p) + 1))
            p_set.add(p[-1])
        
        while h[-1] < t[-1]:
            h.append(hexa(len(h) + 1))
            h_set.add(h[-1])
        
        if t[-1] > 40755:
            if t[-1] in p_set and t[-1] in h_set:
                return t[-1]
    
def goldbach_other_conjecture(N, primes, squares):
    
    for n in range(5, N, 2):
        if n not in primes:
            flag = False
            p = bisect.bisect_right(primes, n)
            s = bisect.bisect_right(squares, 1 + (n // 2))
            for i in range(p):
                for j in range(s):
                    if n == primes[i] + 2 * squares[j]:
                        flag = True
                        break
                if flag:
                    break
            else:
                return n
                
def distinct_prime_factors(n, primes, N):
    
    def count_prime_factors(num):
        start = num
        count = set()
        while num != 1:
            if num in pf:
                pf[start] = count | pf[num]
                return len(pf[start])
            
            if num in prime_set:
                pf[start] = count | {num}
                return len(pf[start])
            
            for p in primes:
                if num / p == num // p:
                    count.add(p)
                    num = num // p
                    if len(count) > n:
                        pf[start] = count
                        return pf[start]
        
        pf[start] = count
        return len(pf[start])
    
    prime_set = set(primes)
    
    pf = {}
    low = 112112
    #low = 1000
    
    for i in range(low, N, n):
        if count_prime_factors(i) == n:
            print("checking", i)
            j = i - 1
            k = i + 1
            while count_prime_factors(j) == n:
                j -= 1
            j += 1
            
            while count_prime_factors(k) == n:
                k += 1
            k -= 1
            
            if k - j + 1 >= n:
                return j, k
    
    return "not found"

def self_powers(n):
    
    last_ten = ''
    total = 0
    for i in range(1, 1001):
        total += i**i
        string = str(total)[-10:]
        last_ten = string
    
    return last_ten

def prime_perms(primes):
    
    groups = collections.defaultdict(list)
    for p in primes:
        s = str(p)
        if len(s) == 4:
            groups[''.join(sorted(s))].append(p)
    
    for g in list(groups):
        if len(groups[g]) > 2:
            groups[g].sort()
        else:
            del groups[g]
    
    res = []
    
    for g in groups:
        for i in range(1, len(groups[g]) - 1):
            if groups[g][i] - groups[g][i-1] == groups[g][i+1] - groups[g][i]:
                res.append(groups[g][i-1:i+2])
    
    return res

def consec_prime_sum(N, primes):
    
    prime_set = set(primes)
    
    longest = 2
    res = 2
    for i in range(len(primes)):
        total = primes[i]
        j = i + 1
        while total < N and j < len(primes):
            total += primes[j]
            if total in prime_set:
                if j - i + 1 > longest:
                    longest = j - i + 1
                    res = total
            j += 1
            
    return res

class Union_Find(object):
    def __init__(self):
        self.group_id = 0
        self.groups = {}
        self.node_id = {}
    
    def union(self, a, b):
        A, B = a in self.node_id, b in self.node_id
        if A and B and self.node_id[a] != self.node_id[b]:
            self.merge(a, b)
        elif A or B:
            self.add(a, b)
        else:
            self.create(a,b)
    
    def merge(self, a, b):
        obs, targ = sorted((self.node_id[a], self.node_id[b]), key = lambda id: len(self.groups[id]))
        for node in self.groups[obs]:
            self.node_id[node] = targ
        self.groups[targ] |= self.groups[obs]
        del self.groups[obs]
    
    def add(self, a, b, A):
        a, b = (a, b) if A else (b, a)
        targ = self.node_id[a]
        self.node_id[b] = targ
        self.groups[targ] |= {b}
        
    def create(self, a, b):
        self.groups[self.group_id] = {a, b}
        self.node_id[a] = self.node_id[b] = self.group_id
        self.group_id += 1

def prime_digit_replacements(primes, N):
    
    @functools.lru_cache(None)
    def combinations(length):
        res = []
        for r in range(1, length + 1):
            res.extend(list(itertools.combinations(range(length), r)))
        return res
    
    def combos(number):
        length = len(number)
        for c in combinations(length):
            c = set(c)
            count = []
            for i in range(1 if 0 in c else 0, 10):
                n = 0
                for j in range(length):
                    n = n * 10 + i if j in c else n * 10 + int(number[j])
                if n in prime_set:
                    count.append(n)
            #print(count)
            if len(count) == N + 1:
                return True, count
        return False, False
    
    prime_set = set(primes)
    
    for p in primes:
        if p >= 10**6:
            b, g = combos(str(p))
            if b:
                return g
    
    
if __name__ == "__main__":
    import functools, collections, string, math, bisect, itertools
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
    