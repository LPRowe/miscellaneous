import random
import matplotlib
import matplotlib.pyplot as plt
import math
import functools
import heapq
import collections
import time

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
    points = set()
    while len(points) < n:
        points.add((bound * random.random(), bound * random.random()))
    return list(points)

def distance(start, fin):
    x1, y1 = start
    x2, y2 = fin
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#@timer
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

def path_cost(points):
    return sum(distance(a, b) for a, b in zip(points, points[1:]))

def path_relaxation(points, k = 1):
    """
    points: the tour suggested by heuristic_path 
    k: the number of points to be relaxed per cycle (recommended 1 or 2)
    
    note: points[0] = points[-1] = the starting city, never move points[0] or points[-1]
    
    When k is one, tries removing one node from the path and tries to insert it between all other
    cities.  The location that results in the smallest total path is chosen.
    This process is repeated for all n nodes. (consider prioritizing the order of checking nodes)
    i.e. do most streched node first
    
    When k is two, the same process as above is followed using 2 random nodes.
    first: check all locations individually for the two nodes
    second: check all locations with the two nodes side by side (a, b) and then (b, a)
    Place the two nodes in the location(s) that minimizes the tour length
    """
    def reduced_cost(i):
        """returns the change in path length when point i is removed from the path"""
        a, b, c = points[i-1], points[i], points[i+1]
        return distance(a, c) - distance(a, b) - distance(b, c)
    
    def insertion_cost(a, b, c):
        """returns the cost of inserting point b in between points a and c"""
        return distance(a, b) + distance(b, c) - distance(a, c)
    
    initial_cost = path_cost(points)
    
    if k == 1:
        adjusted = set() # keep track of which points have already been adjusted
        while len(adjusted) < len(points) - 2:
            for i in range(1, len(points)-1):
                if points[i] not in adjusted:
                    adjusted.add(points[i])
                    rc = reduced_cost(i)   # change in cost by removing point i
                    best = 0
                    best_index = i
                    for j in range(len(points)-1):
                        if j != i and j != i - 1:
                            c = insertion_cost(points[j], points[i], points[j+1]) # increase in cost by adding point i
                            total_cost = c + rc
                            if total_cost < best:
                                best = total_cost
                                best_index = j
                                
                    if best < 0 and best_index != i:
                        j = best_index
                        p = [points[i]]
                        if j < i:
                            points = points[:j+1] + p + points[j+1:i] + points[i+1:]
                        else:
                            points = points[:i] + points[i+1:j+1] + p + points[j+1:]

    final_cost = path_cost(points)
    
    print(round(initial_cost, 1), round(final_cost, 1), round(final_cost - initial_cost, 1))
    return final_cost, points

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
        visited = set([start])
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
    plt.figure(fig_num, figsize = (3.2, 2.4), dpi = 150)
    x, y = list(zip(*points))
    plt.scatter(x, y, color = color, s = 4)
    if connect_the_dots:
        plt.plot(x, y, color+style, lw = line_width)
    plt.show()
    
def plot_edges(edges, color, style = '--', fig_num = 2, line_width = 1):
    plt.figure(fig_num, figsize = (3.2, 2.4), dpi = 150)
    for a, b in edges:
        plt.scatter([a[0], b[0]], [a[1], b[1]], color = color, s = 4)
        plt.plot([a[0], b[0]], [a[1], b[1]], color + style, lw = line_width)
    plt.show()
    
def average_error(func1, func2, n = 12, cycles = 10):
    best = 0
    heur = 0
    for _ in range(cycles):
        points = generate_points(n, 100)
        best += func1(points)[0]
        heur += func2(points)[1]
    print(round(best, 1), round(heur, 1), round(100*(heur - best) / best, 1))
    


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
    matplotlib.rc('font', size = 7)
    compare = True
    
    n = 18
    points = generate_points(n, 100)
    
    plt.close('all')
    if compare:
        cost, best_path = optimal_path_dp(points)
        edges, heur_cost, heur_best_path = heuristic_path(points)
        rel_cost, relaxed_path = path_relaxation(heur_best_path)
        prev = heur_cost
        while rel_cost != prev:
            prev = rel_cost
            rel_cost, relaxed_path = path_relaxation(relaxed_path)
        plot_path(best_path, 'g')
        plot_path(heur_best_path, 'r', style = '--')
        error = 100 * (heur_cost - cost) / cost
        plt.title(f"Optimal: {round(cost, 1)} Approx.: {round(heur_cost, 1)} Error: {round(error, 1)}%")
        plt.legend(["Optimal Path", "Approximate Path"])
        
        plot_edges(edges, 'b', style = '-.')
        plt.title("Minimum Spanning Tree")
        
        plot_path(heur_best_path, 'r', fig_num = 3)
        plot_path(relaxed_path, 'b', style = '-', fig_num = 3)
    
    print(round(heur_cost, 1), round(rel_cost, 1), round(cost, 1))
    #average_error(optimal_path_dp, heuristic_path, n = n, cycles = 10)
        
        
        
        