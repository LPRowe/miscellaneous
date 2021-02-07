import random

class Heap:
    def __init__(self, arr = []):
        self.arr = []
        self.heapify(arr)
        
    def heapify(self, arr):
        for item in arr:
            self.push(item)
        
    def _less_than(self, a, b):
        """
        returns True if a is less than b
        Custom comparison is used because sometimes item is (x1, x2, x3, x4) but we only
        want to use (x1, x2) when deciding if item a <= item b
        """
        return a[0] < b[0]
        
    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    
    def push(self, item):
        self.arr.append(item)
        self.bubble_up()
        
    def bubble_up(self):
        j = len(self.arr)-1
        i = max(0, (j-1) // 2)
        while j and self._less_than(self.arr[j], self.arr[i]):
            self._swap(i, j)
            j = i
            i = (j-1) // 2
    
    def pop(self):
        if self.arr:
            self._swap(0, -1)
        res = self.arr.pop()
        self.bubble_down()
        return res
    
    def bubble_down(self):
        i = 0
        while True:
            p1, p2 = (i + 1) * 2, (i + 1) * 2 - 1
            if p1 < len(self.arr):
                p1, p2 = (p1, p2) if self._less_than(self.arr[p1], self.arr[p2]) else (p2, p1)
                if self._less_than(self.arr[p1], self.arr[i]):
                    self._swap(i, p1)
                    i = p1
                else:
                    break
            elif p2 < len(self.arr):
                if self._less_than(self.arr[i], self.arr[p2]):
                    self._swap(i, p2)
                break
            else:
                break
    
    def __bool__(self):
        return bool(self.arr)
    
if __name__ == "__main__":
    arr = [(i,j) for i in list(range(3)) for j in list(range(3, -1, -1))]
    random.shuffle(arr)
    h = Heap(arr)
    print(h.arr)
    print()
    while h:
        print(h.pop())