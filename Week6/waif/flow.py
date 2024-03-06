"""
    Use to find the maximum flow in a graph using the Ford-Fulkerson algorithm.
    
    Can be used for graphs represented as:
      graph = defaultdict(lambda: defaultdict(int)) # vertex -> (vertex -> capacity)
      
    Code taken from: https://github.itu.dk/algorithms/aps-24/blob/main/060-network-flows/code/flow.py
"""
from collections import defaultdict

### BREADTH-FIRST SEARCH ###
def bfs(graph, src, dest, mincap=0): 
    """
    Implements the Breadth-First Search algorithm to find a path from a source node to a destination node in a graph.
    Works by exploring all the vertices at the current depth/level before moving on to vertices at the next depth level.

    Args:
        graph (dict): The graph, represented as a dictionary where the keys are nodes and the values are dictionaries 
                      representing the adjacent nodes and their capacities.
        src (hashable): The source node from which the path starts.
        dest (hashable): The destination node where the path ends.
        mincap (int, optional): The minimum capacity that an edge must have to be considered.

    Returns:
        tuple: A tuple where the first element is a boolean indicating whether a path has been found and the second element 
               is the path if a path has been found or the set of visited nodes if no path has been found.
    """
    
    # Initialize the parent dictionary with the source node as its own parent
    parent = {src:src} 

    # Initialize the current layer with the source node
    layer = [src] 

    # While there are nodes in the current layer
    while layer:
        # Initialize the next layer
        nextlayer = []

        # For each node in the current layer
        for u in layer:
            # For each adjacent node and its capacity
            for v,cap in graph[u].items():
                # If the capacity is greater than the minimum capacity and the node has not been visited
                if cap > mincap and v not in parent:
                    # Set the parent of the node
                    parent[v] = u

                    # Add the node to the next layer
                    nextlayer.append(v)

                    # If the node is the destination
                    if v == dest:
                        # Initialize the path
                        p =  []

                        # Start from the destination
                        current_vertex = dest

                        # While the source has not been reached
                        while src != current_vertex:
                            # Add the edge from the parent to the current node to the path
                            p.append((parent[current_vertex],current_vertex))

                            # Move to the parent
                            current_vertex = parent[current_vertex]

                        # Return that a path has been found and the path
                        return (True,p)

        # Move to the next layer
        layer = nextlayer

    return (False,set(parent))
    
    
    
### FORD-FULKERSON ALGORITHM ###
def flow(orggraph, src, dest):
    """
    Implements the Ford-Fulkerson algorithm to find the maximum flow in a flow network.
    Works by repeatedly finding paths from the source to the destination in the residual graph 
    and augmenting the flow along these paths until no more augmenting paths can be found.

    Args:
        orggraph (dict): The original graph, represented as a dictionary where the keys are nodes and the values 
                         are dictionaries representing the adjacent nodes and their capacities.
        src (hashable): The source node from which the flow starts.
        dest (hashable): The destination node where the flow ends.

    Returns:
        tuple: A tuple where the first element is the maximum flow, the second element is the residual graph, 
               and the third element is the set of visited nodes.
    """
    # Create a new graph from the original graph
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    # Copy the original graph to the new graph and find the maximum capacity
    for u, d in orggraph.items():
        for v, c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity, c)

    # Initialize the current flow to 0
    current_flow = 0
    # Initialize the minimum capacity to the maximum capacity. To make it faster and more likely to find a high flow path
    mincap = maxcapacity
    # While there are paths from the source to the destination
    while True:
        # Find a path from the source to the destination
        ispath, p_or_seen = bfs(graph, src, dest, mincap)
        # If no path was found
        if not ispath:
            # If the minimum capacity is greater than 0
            if mincap > 0:
                # Halve the minimum capacity
                mincap = mincap // 2
                # Continue with the next iteration of the loop
                continue
            else:
                # Return the current flow, the residual graph, and the set of visited nodes
                return (current_flow,
                        {a: {b: c - graph[a][b] for b, c in d.items() if graph[a][b] < c}
                         for a, d in orggraph.items()},
                        p_or_seen)
        # If a path was found
        p = p_or_seen
        # Find the minimum capacity of the path
        saturation = min(graph[u][v] for u, v in p)
        # Increase the current flow by the minimum capacity of the path
        current_flow += saturation
        # For each edge in the path
        for u, v in p:
            # Decrease the capacity of the edge by the minimum capacity of the path
            graph[u][v] -= saturation
            # Increase the capacity of the reverse edge by the minimum capacity of the path
            graph[v][u] += saturation