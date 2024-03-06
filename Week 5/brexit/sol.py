"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/fv7htp/problems/brexit
Author: Hannah Camilla Andersen (hcan)
Date:  28/02 2024

Description:
You have crafted a list of all pairs of countries that are trading partners of one another. 
If at least half of the trading partners of any given country leave the union, country will soon follow. 
Given this information, you now intend to determine whether your home country will leave the union.
- Input:
    - One line with C, P, X, L 
        - C = number of countries (2 <= C <= 200.000)
        - P = number of pairs of trading partnerships (1 <= P <= 300.000)
        - X = your home country (1 <= X <= C)
        - L = first country that leaves the union (1 <= L <= C)
    - P * pairs A B, where A and B are trading partners (1 <= A < B <= C)
- Output:
    - For each test case, output one line containing either “leave” or “stay”, denoting whether you home country leaves or stays in the union.
    
Nodes represent countries, and directed edges represent partnerships

Use BFS to visit all trading parties of contries and check if more than half leave the union.
"""

from collections import defaultdict, deque

# Graph representation
graph = defaultdict(list)        # Adjacency list/dict (country: [trading partners])
left = set()                     # Contries that have left the union
partners_left = defaultdict(int) # Number of trading partners that have left the union

# Handle input
c, p, x, l = map(int, input().split())
for _ in range(p):
    a, b = map(int, input().split())
    # Add dependency both ways
    graph[a].append(b)
    graph[b].append(a)

#### BREATH-FIRST SEARCH ####
## Start from the first leaving country and level-wise follow all the countries that decides to leave as a result of the first country leaving
# Implented using a queue
queue = deque([l]) 
visited = set()

# The first country leaves the union 
left.add(l)                 
visited.add(l) 

while queue: 
    # Pop from front of queue
    current_country = queue.popleft() 
    
    # Loop through all trading partners of the current country
    for partner in graph[current_country]:
        # Don't visit the same country twice
        if partner in visited:
            continue
        
        # Increment partners_left for the partner
        if current_country in left:
            partners_left[partner] += 1
        
        # If a partner decides to leave the union, add it to the queue to update and check its trading partners
        if partner not in left and partners_left[partner] >= len(graph[partner]) / 2:
            left.add(partner)
            queue.append(partner)
            visited.add(partner)
#### 

# Check if the home country will leave the union
if x in left:
    print("leave")
else:
    print("stay")