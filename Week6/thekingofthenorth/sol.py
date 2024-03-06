"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ehr4an/problems/thekingofthenorth
Author: Hannah Camilla Andersen (hcan)
Date:   06/03 2024

Description:
You have to determine the size of the army that you will raise to defend the North.
You will only have to defend against armies moving horizontally or vertically (an army cannot pass by your bannermen diagonally).
Your kingdom counts as defended, if there is not a single way to reach your castle, starting anywhere outside of the map, without passing to a fully defended area.
Squares on the map labeled represent high mountains, or walls, no one would ever be foolish enough to climb
- Input:
    - First line with 2 integers R and C, specifying the dimensions of the map (3 ≤ R, C ≤ 300)
    - R lines with C integers each, specifying the number of bannermen required to defend each square (0 ≤ bannermen ≤ 100.000)
    - 2 integers r and c, specifying the position of your castle (0 ≤ r ≤ R, 0 ≤ c ≤ C-1)
- Output:
    - The smallest possible army you would require to defend the kingdom given in the input.

Solve it as a minimum cut problem. Represent the map as a graph with vertices for each square and edges between adjacent squares
Use the Ford-Fulkerson algorithm to find the maximum flow/minimum cut in the graph.
Code from: https://github.itu.dk/algorithms/aps-24/blob/main/060-network-flows/code/thekingofthenorth.py 
"""

from collections import defaultdict
from itertools import product
from flow import flow

#### GRAPH REPRESENTATION ####
graph = defaultdict(lambda: defaultdict(int)) # vertex -> (vertex -> capacity). Default capacity is 0

R, C = map(int, input().split()) # R is down, C is across

# Use a 2D list to store the capacities of the vertices
inp = [[0]*C for _ in range(R)]

maxcapacity = 0

# Read the capacities from input and add them to the graph and the 2D list
for row in range(R):
    for col, capacity in enumerate(map(int, input().split())):
        maxcapacity += capacity
        graph[(row, col, 0)][(row, col, 1)] = capacity
        inp[row][col] = capacity

# Add edges between adjacent vertices with infinite capacity
for row, col in product(range(R), range(C)):
    this = (row, col, 0)
    for rn, cn in product([-1, 0, 1], [-1, 0, 1]):
        if abs(rn) + abs(cn) == 1:
            src = (row + rn, col + cn, 1)
            if min(src) < 0 or src[0] >= R or src[1] >= C:  # If the source vertex is outside the grid
                src = (-1, -1, -1)  # Set the source vertex to a special vertex representing the outside of the grid
            graph[src][this] = maxcapacity

r, c = map(int, input().split()) # Castle

# Compute the maximum flow/minumum cut from outside the map to the castle
flowvalue, fg, cut = flow(graph, (-1, -1, -1), (r, c, 1))
print(flowvalue)