import random
import matplotlib.pyplot as plt
import math
import functools
import heapq
import collections
import time
import multiprocessing
import concurrent.futures

def timer(fcn):
    def wrapper(*args, **kwargs):
        t0 = time.time_ns()
        res = fcn(*args, **kwargs)
        t = time.time_ns() - t0
        print(f"{fcn.__name__}: {round(t * 10**-6, 1)} 'ms'")
        return res
    return wrapper

class UnionFind:
    def __init__(self):
        self.group_id = 0
        self.groups = {}
        self.id = {}
        
    def union(self, a, b):
        """Returns True if an edge was created"""
        A, B = a in self.id, b in self.id
        if A and B and self.id[a] != self.id[b]:
            self.merge(a, b)
        elif A and B:
            return False
        elif A or B:
            self.add(a, b)
        else:
            self.create(a, b)
        return True
        
    def merge(self, a, b):
        obs, targ = sorted((self.id[a], self.id[b]), key = lambda i: len(self.groups[i]))
        for node in self.groups[obs]:
            self.id[node] = targ
        self.groups[targ] |= self.groups[obs]
        del self.groups[obs]
        
    def add(self, a, b):
        a, b = (a, b) if a in self.id else (b, a)
        targ = self.id[a]
        self.id[b] = targ
        self.groups[targ] |= {b}
        
    def create(self, a, b):
        self.groups[self.group_id] = {a, b}
        self.id[a] = self.id[b] = self.group_id
        self.group_id += 1

def generate_points(n, bound):
    x = [random.randint(0, bound) for _ in range(n)]
    y = [random.randint(0, bound) for _ in range(n)]
    return list(set(list(zip(x,y))))

def distance(start, fin):
    x1, y1 = start
    x2, y2 = fin
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

@timer
def optimal_path_dp(points):
    
    @functools.lru_cache(None)
    def helper(i, used):
        
        if used == target:
            return (cost[i][0], [points[0]])
        
        best = math.inf
        best_path = []
        for j in range(N):
            if not (used & bitmask[j]):
                c, p = helper(j, used | bitmask[j])
                c += cost[i][j]
                if c < best:
                    best = c
                    best_path = [points[j]] + p
        return best, best_path
    
    N = len(points)
    cost = [[distance(points[i], points[j]) for i in range(N)] for j in range(N)]
    bitmask = [1 << i for i in range(N)]
    target = (1 << N) - 1
    c, p = helper(0, 1)
    return c, [points[0]] + p
    
@timer
def optimal_path(points):
    """
    Non-memoized approach to finding the optimal path.
    Takes a list of points and finds the optimal tour to visit all points and return home.
    Very slow compared to memoized version. For demonstration purposes only.
    """
    
    def helper(cost, path, points):
        nonlocal best_path, best
        
        if not points or cost >= best:
            cost += distance(path[-1], path[0])
            if cost < best:
                path.append(path[0])
                best = cost
                best_path = path
            return None
        
        for i,p in enumerate(points):
            helper(cost + distance(path[-1], p), path + [p], points[:i]+points[i+1:])
    
    best = math.inf
    best_path = []
    for i, p in enumerate(points):
        helper(0, [p], points[:i]+points[i+1:])
    return best, best_path

@timer
def heuristic_path(points):
    """
    Uses Kruskal's algorithm to create a MST of the points
    Perofrsm a pre-order DFS exploration from each node and generates a path as the nodes are visited.
    Selects the shortest path.
    """
    
    h = []
    for i in range(len(points)):
        a = points[i]
        for j in range(i):
            b = points[j]
            heapq.heappush(h, (distance(a, b), a, b))
    
    # Create MST
    uf = UnionFind()
    edges = []
    while len(edges) < len(points) - 1:
        dist, a, b = heapq.heappop(h)
        if uf.union(a, b):
            edges.append((a, b))
    
    g = collections.defaultdict(list)
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    
    # Perform DFS to find approximation of the optimal path
    def helper(node):
        nonlocal path, best_path, best, cost, visited
        path.append(node)
        for neigh in g[node]:
            if neigh not in visited:
                visited.add(neigh)
                cost += distance(neigh, node)
                helper(neigh)
    
    best_path = []
    best = math.inf
    for start in points:
        visited = set()
        path = []
        cost = 0
        helper(start)
        path.append(start)
        cost = sum(distance(a, b) for a, b in zip(path, path[1:]))
        if cost < best:
            best = cost
            best_path = path
    
    return edges, best, best_path
    
    
def plot_path(points, color, style = '-', connect_the_dots = True, fig_num = 1, line_width = 1):
    plt.figure(fig_num)
    x, y = list(zip(*points))
    plt.scatter(x, y, color = color)
    if connect_the_dots:
        plt.plot(x, y, color+style, lw = line_width)
    plt.show()
    
def plot_edges(edges, color, style = '--', fig_num = 1, line_width = 1):
    plt.figure(fig_num)
    for a, b in edges:
        plt.scatter([a[0], b[0]], [a[1], b[1]], color = color, s = 4)
        plt.plot([a[0], b[0]], [a[1], b[1]], color + style, lw = line_width)
    plt.show()
    
def average_error(func1, func2, n = 18, cycles = 10):
    best = 0
    heur = 0
    for _ in range(cycles):
        points = generate_points(n, 10)
        best += func1(points)[0]
        heur += func2(points)[1]
    print(best, heur, round(100*(heur - best) / best, 1))

if __name__ == "__main__":
    """
    The traveling salesman problem (TSP) requires a salesman to visit
    all n vertices (nodes) and return to the starting node taking the
    shortest possible path.  
    
    The brute force solution is O(n!) and becomes intractible above
    approximately 12 nodes.  
    
    Here we will solve the TSP optimally and using a heuristic, compare the
    time complexity of each solution and the amount of error.
    """
    show_optimal_path = False
    show_mst = False
    show_heur_path = False
    
    toggle = False
    if toggle:
        show_optimal_path ^= 1
        show_mst ^= 1
        show_heur_path ^= 1
    
    n = 15
    points = generate_points(15, 10)
    
    plt.close('all')
    if show_optimal_path:
        cost, best_path = optimal_path_dp(points)
        plot_path(best_path, 'g')
    
    if show_heur_path | show_mst:
        edges, heur_cost, heur_best_path = heuristic_path(points)
        if show_heur_path:
            plot_path(heur_best_path, 'r', style = '--')
        if show_mst:
            plot_edges(edges, 'b', style = '-.')
        error = 100 * (heur_cost - cost) / cost
        plt.title(f"Optimal: {round(cost, 1)} Approx.: {round(heur_cost, 1)} Error: {round(error, 1)}%")
        
            
    p = average_error(optimal_path_dp, heuristic_path)
