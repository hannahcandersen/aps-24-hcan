"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/fv7htp/problems/torn2pieces
Author: Hannah Camilla Andersen (hcan)
Date:  05/03 2024

Description:
Each fragment of the map happens to perfectly contain a single subway station while also identifying all of the other stations that it connects to. 
Each connection between stations is bi-directional such that it can be travelled going either direction. 
Using all of the available fragments, your task is to determine the sequence of stations you must pass through in order to reach your final destination 
or state that there is no route if you don’t have enough information to complete your journey.
- Input:
    - N: Number of fragments (2 <= N <= 32)
    - N lines with 
        - Station and a list of all the stations it connects to (space separated)
    - Final line: Start and destination station    
- Output:
    - Give the sequence of stations that leads from the starting station to the destination station    

Use an undirected graph to represent the subway map
Use DFS as there is a single route and its an acyclic graph
"""

from collections import defaultdict
import sys
sys.setrecursionlimit(100001)

output = []     # Final route
visited = set() # Keeps track of the visited stations
def dfs(node):
    """
    Depth-first search to recursively visit all connected stations in the graph.
    Return true if the node is part of the final route

    Args:
        node (str): Current station we are visiting
        
    Complexity: O(n + m) where n is the number of nodes and m is the number of edges 
    """
    visited.add(node)
    output.append(node)
    
    # Check if we have found the whole route
    if node == start:
        return True
    
    # Else continue the search
    for connection in graph[node]: 
        if connection not in visited and dfs(connection): # Is part of the final route
            return True
        
    # Not part of the final route - remove from output
    output.pop() 
        
# Handle input
n = int(input()) # Number of fragments

# Build undirected, acyclic graph
graph = defaultdict(list) # Adjacency list/dict (station: [connected stations]).
for _ in range(n): 
    stations = input().split()
    station = stations[0]
    connections = stations[1:]
    # Add dependency both ways 
    for c in connections:
        graph[station].append(c) # station -> connection
        graph[c].append(station) # connection -> station

start, destination = input().split()

foundRoute = dfs(destination) # Start DFS from the destination

if foundRoute:
    result = output[::-1] # Reverse the list to get the correct order
    print(" ".join(result))
else:
    print("no route found")