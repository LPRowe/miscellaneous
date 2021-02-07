class QuickList:
    def __init__(self, arr = []):
        self.arr = arr
        self.items = set(arr)
        
    def append(self, item):
        self.arr.append(item)
        
    def __contains__(self, item):
        return item in self.items
    
    def __getitem__(self, index):
        return self.arr[index]
    
    def __setitem__(self, index, value):
        if -len(self.arr) <= index < len(self.arr):
            self.arr[index] = value
        else:
            raise Exception(f"{index} is out of range.")
    
    def copy(self):
        return QuickList(self.arr)
    
    
if __name__ == "__main__":
    arr = list(range(10))
    arr = QuickList(arr)
    print(7 in arr)
    print(10 in arr)