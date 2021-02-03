### Intro

The traveling salesman problem (TSP) is a classic NP-complete problem.

The problem consists of a salesman who must travel from home, to a set of cities, and return home.

His objective is to find the shortest possible path to do so.

The problem of course does not need to be cities and roads.

Think of the problem in terms of vertices (cities) that are fully connected by a set of edges (roads).

The solution to this probelm can be applied to a wide variety of situations.

### Methods

####<b>The brute force approach:</b>
1. generate all permuations of N cities
2. calculate the cost of the path created by each permuation
Here, the cost to travel from city A to city B is the distance between cities A and B.
However, different instances of the problem may have different cost functions.
3. return the lowest cost path
which works... but scales with O(n!) which makes this approach infeasible for sets of cities larger than &approx; 12.

The time and space complexity of the solution can be greatly improved through dynamic programming.

####<b>The dynamic programming approach:</b>
1. Choose a specific starting city.
We must travel to every city once, so it does not matter which city you choose.
2. Store the visited cities in a bit-masked integer.
i.e. 106 = '0b1101010' means we have visited cities 1, 3, 5, and 6 (counting the '1' bits from the right)
3. At each iteration, consider visiting all N cities next.
If a city has already been visited (as shown in the bit-mask) then do not visit it a second time.
Otherwise try visiting the city for the cost of distance(current_city, next_city) plus the cost to visit the remaining cities.

This is the bones of the DP solution, but thus far it is not much better than the brute force solution.

Why? Because it is currently lacking memoization.

Consider the following scenarios for a case of 7 cities, 
A: the salesman visits city 1, 3, 2, 4 
B: the salesman visits city 1, 2, 3, 4 

Journies A and B may have different costs, but the <b>best</b> possible path from city 4 to cities {5, 6, 7} and returning home to city 1 must be the same for both path's A and B.  Once the optimal path from 4 -> {5, 6, 7} -> 1 has been calculated once in scenario A, it would be a duplication of effort to calculate it again for scenario B.

Remembering the minimum cost and best path from the state (current_city, visited_cities) allows us to skip these calculations the second, third, ...Nth time the state is visited.  

This reduces the time complexity of the solution from O(n!) to O(n<sup>2</sup>&middot;2<sup>n</sup>).
This is a substantial improvement, which allows us to calculate the optimal solution for up to &approx; 20 cities.

At this point, you might be thinking 20 cities is not a lot of cities, and you are right.
However, in order to further improve the time complexity of our solution, we must forego accuracy.

####<b>The heuristic approach:</b>

1. Calculate the minimum spanning tree (MST) of the set of cities.
This can be done with Prim's Algorithm or Kruskal's Algorithm.
Kruskal's Algorithm was implemented here - see TSP_heruistic.py >> heuristic_path
2. Create a path based on the preorder traversal of the MST.
3. Repeat step 2 for all N cities and return the path that has the minimum cost.


Average heuristic path is 11.5% longer than the optimal path for 15 vertices and 9.5% longer for 12 vertices

| n | (heuristic - optimal) / optimal |
|:----:|:---:|
| 3  | 0.0% |
| 4  | 3.3% |
| 6  | 4.6% |
| 9  | 7.2% |
| 12 | 9.5% |
| 15 | 11.5%|
| 18 | 14.8%|


### Comparisons