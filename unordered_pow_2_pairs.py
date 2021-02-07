class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.tail = False

class Trie(object):
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, string):
        curr = self.root
        for char in string:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.tail = True
    
    def find_pairs(self):
        
        @functools.lru_cache(None)
        def helper(a, b, overlap):
            
            if a.tail:
                return (overlap == 1) and (a != b)
            
            if overlap > 1:
                return 0
            
            res = 0
            if '0' in a.children and '0' in b.children:
                res += helper(a.children['0'], b.children['0'], overlap)
            if '0' in a.children and '1' in b.children:
                res += helper(a.children['0'], b.children['1'], overlap)
            if '1' in a.children and '0' in b.children:
                res += helper(a.children['1'], b.children['0'], overlap)
            if '1' in a.children and '1' in b.children:
                res += helper(a.children['1'], b.children['1'], overlap + 1)
            return res
        
        return helper(self.root, self.root, 0)
        
def unordered_pairs(nums):
    L = len(bin(max(nums))[2:])
    tree = Trie()
    for n in nums:
        tree.insert(bin(n)[2:].zfill(L))
    return tree.find_pairs() // 2 # divided by 2 so the pair {7, 4} and {4, 7} is not counted twice

if __name__ == "__main__":
    import functools
    nums = [1, 2, 3, 5, 7, 8, 10]
    print(unordered_pairs(nums))
    
    
    
    
    
    