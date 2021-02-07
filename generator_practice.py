class Square_Generator:
    def __init__(self, n):
        self.n = n
        self.i = -1
        
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.i == self.n:
            raise StopIteration()
        self.i += 1
        return self.i**2
    
def square_generator(n):
    for i in range(n+1):
        yield(i**2)

s = (i**2 for i in range(6))
    
if __name__ == "__main__":
    g = s
    for _ in range(10):
        try:
            print(next(g))
        except:
            break