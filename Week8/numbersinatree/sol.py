"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/f8j34o/problems/numbertree
Author: Hannah Camilla Andersen (hcan)
Date:   20/03

Description:
Build a binary tree.
Number the nodes starting from the bottom right leaf which gets the number 1 and then incrementing the numbers from right to left and from bottom to top.
When we want to describe a node in the tree, we can do it by describing a path starting at the root and going down toward the leaves. 
At each non-leaf node we can either go left (‘L’) or right (‘R’).

Input: 
- One line with: 
    - h: height of the tree (1 ≤ h ≤ 30)
    - path: path to a node in the tree starting at the root
Output:
    - Output one line containing the label of the node given by the path.

The idea is to pretend that the nodes are labeled after the index in an array representation of the tree.
The root is at index 1.
The left child of a node at index i is at index 2*i.
The right child of a node at index i is at index 2*i + 1.
When the array index is found, the label of the node is the maximum label minus the index.
"""

inp = input().split()

if len(inp) == 2:
    h, path = inp
else: # No path given
    path = False
    
h = int(inp[0])
max_label = 2**(h+1) - 1 # Number of nodes in a perfect binary tree
    
# Start from root. This would be index 1 in an array representation
idx = 1
    
if path:
    for direction in path:
        if direction == 'L':
            idx = 2 * idx # Left child index
        if direction == 'R':
            idx = 2 * idx + 1 # Right child index

print(max_label - (idx - 1))
    