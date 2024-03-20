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

Represent the tree using an array.
The root is at index 1.
The left child of a node at index i is at index 2*i.
The right child of a node at index i is at index 2*i + 1.

MEMORY LIMIT EXCEEDED
"""

inp = input()
# Only height is given
if len(inp) <= 2:
    h = int(inp)
    print(2**(h+1)-1) 
    exit()
else: # Both height and path is given
    h, path = inp.split()
    h = int(h)

# Number of nodes in tree, which is also the label of the root node
max_l = 2**(h+1) 

# Array to represent the tree
tree = [0] * max_l

# Update label from end of the array to front
l = 1 
for i in range(max_l-1, 0, -1):
    tree[i] = l
    l += 1
#print(tree)

# Start path from root
node_i = 1
for direction in path:
    if direction == 'L':
        node_i *= 2
    else: # direction == 'R'
        node_i = 2*node_i + 1

print(tree[node_i])