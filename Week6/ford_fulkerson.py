"""
Author: Hannah Camilla Andersen (hcan)
Date: 11/03 2024

My attempt at implementing the Ford-Fulkerson algorithm 
Can be used to find maximum flow / minimum cut in a flow network

Solution inspired by code from lecture and: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/'
"""


"""  The algorithm starts with an initial flow of zero, and iteratively finds a path from s to t that has available capacity, and then increases the flow along that path by the maximum amount possible. This process continues until no more augmenting paths can be found.
"""

from collections import deque

def build_path(source, sink, parent):
    """ BFS helper function to construct and return the path from the sink to the source using the parent dictionary.

    Args:
        source:         The source node.
        sink:           The sink node.
        parent (dict):  A dictionary where keys are nodes and values are their parents in the path.

    Returns:
        list: A list representing the path from the source to the sink.
    """
    path = []
    current = sink 
    
    while current != source:
        path.append(current)
        current = parent[current]
    path.append(source)
    
    return list(reversed(path))


def bfs(graph, source, sink):
    """ Breadth-first search to find the shortest path from source to sink in the residual graph

    Args:
        graph (dict): The graph, represented as a dictionary where the keys are nodes and the values are dictionaries 
                      representing the adjacent nodes and their capacities. (node -> neigbors -> capacity)
        source:       Source node from which the flow starts
        sink:         Destination node to which the flow goes
    
    Returns:
        tuple: A list representing the path from the source to the sink. Returns None if no path is found.
    """
    
    queue = deque([source])  # (node, parent) tuple
    visited = set([source])
    parent = {source: None}  # To keep track of the parent of each node, to be able to reconstruct the path

    while queue:
        vertex= queue.popleft()

        # If the sink is reached, return the path
        if vertex == sink:
            return build_path(source, sink, parent)

        # Iterate through all the neighbors of the current node
        for neighbor, _ in graph[vertex].items():
            if neighbor not in visited:
                queue.append(neighbor)  
                visited.add(neighbor)
                parent[neighbor] = vertex # Remember the parent

    # If no path is found
    return None

def ford_fulkerson(original_graph, source, sink):
    """
    Implements the Ford-Fulkerson algorithm to find the maximum flow in a flow network.
    Works by repeatedly finding paths from the source to the destination in the residual graph 
    and augmenting the flow along these paths until no more augmenting paths can be found.

    Args:
        orggraph (dict):   The original graph, represented as a dictionary where the keys are nodes and the values 
                           are dictionaries representing the adjacent nodes and their capacities.
        src (hashable):    The source node from which the flow starts.
        dest (hashable):   The destination node where the flow ends.

    Returns:
        tuple: A tuple where the first element is the maximum flow, the second element is the residual graph, 
               and the third element is the set of visited nodes.
    """
    
    

