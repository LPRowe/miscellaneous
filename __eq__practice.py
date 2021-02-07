class Counter:
    def __init__(self, arr):
        self.count = {}
        for num in arr:
            self.count[num] = self.count.get(num, 0) + 1
            
    def values(self):
        return list(self.count.values())
    
    def keys(self):
        return list(self.count.keys())
            
    def __eq__(self, other):
        return self.values() == other.values() and self.keys() == other.keys()
    
    
if __name__ == "__main__":
    a = list(range(7)) + [6]
    b = a[:]
    c = a[:]
    c.pop()
    d = a[:]
    d[3] = 8
    print(a)
    print(b)
    print(c)
    print(d)
    
    A = Counter(a)
    
    
"ab"
"acb"
""
""
"a"
""
""
"A"