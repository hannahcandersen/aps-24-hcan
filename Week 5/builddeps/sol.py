"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/fv7htp/problems/builddeps 
Author: Hannah Camilla Andersen (hcan)
Date:  28/02 2024

Description:
Given the Makefile and a changed file, output the set of files that need to be recompiled, 
in an order that satisfies the dependencies
No two files depend on each other directly or indirectly.
- Input:
    - N: Number of rules (1 <= N <= 100.000)
    - N * rules of the form "f: f1 f2 ... fk" where f is the file and f1, f2, ..., fk are the files it depends on. At most 5 dependencies.
    - C: The filename of the changed file (1-10 lowercase letters)
- Output:
    - The set of files that need to be recompiled, in an order that satisfies the dependencies
    - Can be multiple correct answers
    
Nodes represent files, and directed edges represent dependencies between files, pointing from a dependency to the dependent file.
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(100001)

# Uses a dict to represent the graph
# defaultdict is used to initialize the dict as we dont know the keys in advance
# key = file, value = list of files that depend on the key 
graph = defaultdict(list)
output = []
visited = set() # Keeps track of the visited nodes
def dfs(node):
    """
    Depth-first search to recursively visit all nodes in the graph that are affected by the change.

    Args:
        node (int): Current node we are visiting
        
    Complexity: O(n + m) where n is the number of nodes and m is the number of edges 
    """
    
    visited.add(node) # We have now visited the node
    for file in graph[node]: # Loop through all the files that depend on the current file
        if file not in visited:
            dfs(file) 
    output.append(node)  # Because of the recursive calls, it adds the last visited file firsts

# Handle input
n = int(input())
for _ in range(n):
    file, dependencies = input().split(':')
    for dep in dependencies.split(' '):
        if dep != '':
            # Reverses the arrow - the file depends on dep
            graph[dep].append(file)

changed_file = input().strip()
dfs(changed_file)

# Print the files in the order they need to be recompiled (in reverse order as we added the last visited file firsts
for v in output[::-1]:
    print(v)