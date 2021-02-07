# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:57:06 2020

@author: rowe1
"""

class Trie_Node:
    def __init__(self, char):
        self.val = char
        self.edges = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = Trie_Node(None)
    
    def insert(self, word):
        '''Inserts word into the trie'''
        curr = self.root
        for char in word:
            if char not in curr.edges:
                curr.edges[char] = Trie_Node(char)
            curr = curr.edges[char]
        curr.is_word_end = True
    
    def search(self, word):
        '''Returns true if word is in the trie'''
        curr = self.root
        for char in word:
            if char not in curr.edges:
                return False
            curr = curr.edges[char]
        return curr.is_word_end
        
        
if __name__ == "__main__":
    words = ["apple", "ape", "pen", "peace", "pencil"]
    tree = Trie()
    for word in words:
        tree.insert(word)
    
    other_words = ["banana", "penc", "pe"]
    for word in words:
        print(tree.search(word))
    print()
    for word in other_words:
        print(tree.search(word))