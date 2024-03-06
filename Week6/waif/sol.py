"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ehr4an/problems/waif
Author: Hannah Camilla Andersen (hcan)
Date:   06/03 2024

Description:
Daycare center, where only a certain amount of toys from each category are allowed. 
Not all toys are liked by all children.
Find the maximum amount of children who can be satisfied with the toys available.
- Input:
    - First line with 3 integers
        - N: number of children         (1 ≤ N)
        - M: number of toys             (M ≤ 100)
        - P: number of toy categories   (0 ≤ P ≤ M)
        Both children and toys are numbered starting from 1
    - N lines with integers, where line 1 is child 1, line 2 is child 2, etc.
        - k: Number of toys the child likes       (1 ≤ k ≤ M) 
        - t1 t2 ... tk: the toys the child likes  (1 ≤ ti ≤ M)
    - P lines with integers, where line 1 is category 1, line 2 is category 2, etc.
        - l: Number of toys in the category       (1 ≤ l ≤ M)
        - t1 t2 ... tl: the toys in the category  (1 ≤ ti ≤ M)
        - r: At most r of the toys in the category can be used (1 ≤ r ≤ l ≤ m) 
- Output:
    - Maximum number of children that can be satisfied with the toys available

Solve it as a maximum matching problem, where the children are the left side and the toy categories are the right side containing the toys.
The size of a maximum flow (capacity 1 for all edges) in the graph equals the size of a maximum matching in the original graph.

"""
from collections import defaultdict

n, m, p = map(int, input().split()) # Children, toys, categories

#### GRAPH REPRESENTATION ####
# vertex -> (vertex -> capacity). All capacities are 1 except for the categories where it is r
# Source -> Sink -> Toys -> Category they belong to -> Sink. If no category, go straight to sink with capacity 1 
graph = defaultdict(lambda: defaultdict(int)) 
# Vertice 0 is source
source_v = 0
# Vertices 1 - n are children
child_start = 1
# Vertices n+1 - n+m are toys
toy_start = n
# Vertices n+m+1 - n+m+p are categories
category_start = n+m+1
# Vertice n+m+p+1 is sink
sink_v = n+m+p+1

#### BUILD GRAPH ####
# Children preferences
for i in range(n): 
    child_v = i + child_start 
    line = list(map(int, input().split()))
    preferences = line[1:] # Toys the child likes
    
    # Connect source to child 
    graph[source_v][child_v] = 1 # Adds edge from source to child with capacity 1
    
    # Connect child to toys
    for toy in preferences: 
        toy_v = toy + toy_start 
        graph[child_v][toy_v] = 1
        
# Toy categories
for j in range(p): 
    category_v = j + category_start
    line = list(map(int, input().split()))
    toys_in_j_category = line[1:-1] # Toys in the category (excluding the number of toys and the maximum amount of toys)
    r = line[-1] # Maximum amount of toys in the category (capacity)
    
    # Add edge between toy and category
    for toy in toys_in_j_category: 
        toy_v = toy + toy_start 
        graph[toy_v][category_v] = 1

    # Add edge between category and sink with capacity r
    graph[category_v][sink_v] = r 

# Connect the rest of the toys (not in a category) to the sink with capacity 1
for toy_v in range(toy_start, category_start): 
    if toy_v not in graph:
        graph[toy_v][sink_v] = 1

print(graph)