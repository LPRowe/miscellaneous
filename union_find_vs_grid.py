# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:51:23 2020

@author: rowe1
"""

class Union_Find(object):
    def __init__(self, n):
        self.parent_list = list(range(n))
        self.size_list = [1] * n
    
    def find(self, val):
        root = val
        while root != self.parent_list[root]:
            root = self.parent_list[root]
        curr = val
        while curr != root:
            curr, self.parent_list[curr] = self.parent_list[curr], root
        return root
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        if self.is_connected(x, y):
            return None
        x_root, y_root = sorted((self.find(x), self.find(y)), key = lambda r: self.size_list[r])
        self.size_list[y_root] += self.size_list[x_root]
        self.parent_list[x_root] = y_root
    
class Group_By_ID(object):
    def __init__(self):
        """
        self.group: maps group_id to the nodes that are in the group
        self.node_id: maps node to the group it belongs to
        """
        self.group_id = 0
        self.groups = {}
        self.node_id = {}
        
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

# =============================================================================
# Simple problem to test the time-complexity of grid and unionfind
# =============================================================================
def find_circle_grid(M):
    n = len(M)
    grid = Group_By_ID()
    for i in range(n):
        for j in range(i, n):
            if M[i][j]:
                grid.union(i,j)
    return len(grid.groups)

def find_circle_uf(M):
    n = len(M)
    uf = Union_Find(n)
    for i in range(n):
        for j in range(i, n):
            if M[i][j]:
                uf.union(i, j)
    return len(set(uf.find(i) for i in range(n)))

# =============================================================================
# Time complexity test
# =============================================================================
if __name__ == '__main__':
    import random, time
    import matplotlib.pyplot as plt
    
    # Generate random edge-matrices
    matrix_size = [(1 << i) for i in range(6,13)]
    matrix_density = 0.9 # 0.1 is a sparse graph, 0.9 is a dense graph
    M = []
    for n in matrix_size:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mat[i][j] = mat[j][i] = 1 if random.random() <= matrix_density else 0
        M.append(mat)
    
    # runtimes for group by id and union find
    t_grid = []
    t_uf = []
    
    # calculate runtime for each method on different size matrices
    for m in range(len(matrix_size)):
        print()
        print(m, matrix_size[m])
        t0 = time.time_ns()
        find_circle_grid(M[m])
        t_grid.append(time.time_ns() - t0)
        
        t0 = time.time_ns()
        find_circle_uf(M[m])
        t_uf.append(time.time_ns() - t0)
        print(int(t_grid[-1]*(1e-3)), int(t_uf[-1]*(1e-3)))
    
    #plot results
    plt.close('all')
    plt.figure()
    plt.loglog(matrix_size, t_grid, 'b-', lw=2, label='Group by ID', basex=2, basey=10)
    plt.loglog(matrix_size, t_uf, 'r-', lw=2, label='Union-Find', basex=2, basey=10)
    plt.xlabel("n")
    plt.ylabel(r"time [ns]")
    plt.legend()
    plt.show()
    
    # uf - grid ratio
    ratio = [u / max(g, 1) for u,g in zip(t_uf, t_grid)]
    print(ratio)
    print(sum(ratio) / len(ratio))