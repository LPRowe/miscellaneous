# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:15:32 2020

@author: rowe1
"""

class Union_Find(object):
    def __init__(self):
        """
        self.group: maps group_id to the nodes that are in the group
        self.node_id: maps node to the group it belongs to
        """
        self.group_id = 0
        self.groups = {}
        self.node_id = {}
        
    def test(self):
        n = 5
        adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            adjacency_matrix[i][i] = 1
            self.union(i, i)
            for j in range(i+1, n):
                adjacency_matrix[i][j] = adjacency_matrix[j][i] = random.randint(0, 1)
                if adjacency_matrix[i][j]:
                    self.union(i, j)
        
        # Check if union find is working correctly
        for row in adjacency_matrix:
            print(row)
        print(self.groups)
        
        # Reset group_id, node_id, and groups
        self.__init__()        
        
    def union(self, a, b):
        """Nodes a and b share an edge add the edge to the data structure."""
        if (a in self.node_id) and (b in self.node_id) and (self.node_id[a] != self.node_id[b]):
            self.merge(a, b)
        elif (a in self.node_id) or (b in self.node_id):
            self.add(a,b)
        else:
            self.create_new_group(a,b)
            
    def merge(self, a, b):
        """Nodes a and b belong to different groups.  Merge the two groups together."""
        old_id, target_id = sorted((self.node_id[a], self.node_id[b]), key = lambda id: len(self.groups[id]))
        for node in self.groups[old_id]:
            self.node_id[node] = target_id
        self.groups[target_id] |= self.groups[old_id]
        del self.groups[old_id]
    
    def add(self, a, b):
        """"Adds a new node to an existing group."""
        a, b = (a, b) if a in self.node_id else (b, a)
        target_id = self.node_id[a]
        self.node_id[b] = target_id
        self.groups[target_id] |= set([b])
    
    def create_new_group(self, a, b):
        """"Neither node a or node b belong to a group.  Create a new group containing {a, b}."""
        self.groups[self.group_id] = set([a,b])
        self.node_id[a] = self.node_id[b] = self.group_id
        self.group_id += 1
        
if __name__ == "__main__":
    import random
    u = Union_Find()
    u.test()
    