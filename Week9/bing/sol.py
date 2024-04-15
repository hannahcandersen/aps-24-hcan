"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/zwdnut/problems/bing
Author: Hannah Camilla Andersen (hcan)
Date:   14/04

Description:
- Analyze the stream of searches coming in, 
and let everyone know how many of these searches began with the letters currently in the search bar.

Input:
- N: number of searches (1 ≤ N ≤ 100.000)
- N words with searches with 1-32 characters of a-z 
Output:
- For each word, output an integer representing 
how many of the previous words began with or were equal to that word.

Solution description:
- Insert each word into a trie as it comes in
- Update the count as you travserse each node
"""

class Node:
    def __init__(self):
        # Dictionary to hold the children nodes for each character
        self.children = {}
        # Count to keep track of how many times a node is visited during insertions
        self.count = 0

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = Node()

    def insert(self, x):
        # Start from the root node
        current = self.root

        # Traverse each character in the string x
        for char in x:
            # Increment the count of visits for the current node
            current.count += 1
            # If the character is not already a child of the current node, add it
            if char not in current.children:
                current.children[char] = Node()
            # Move to the child node corresponding to the character
            current = current.children[char]
        # Once the last character of x is processed, increment its count
        current.count += 1

        # Return the count of the last character node before the last increment
        return current.count - 1

    def print(self):
        # Stack to manage the nodes for printing, starts with the root
        stack = [(self.root, "ROOT", 0)]
        while len(stack) > 0:
            # Pop a node from the stack
            node, c, depth = stack.pop()
            # Print the current node's character and its count at the current depth
            print(depth * "--", c, node.count)
            # Push all child nodes of the current node to the stack for further processing
            for c, child in node.children.items():
                stack.append((child, c, depth + 1))


# MAIN
N = int(input()) # Number of searches

t = Trie()
# For each operation, insert the string in the trie
for _ in range(N):
    print(t.insert(input().strip()))

# Print the entire contents of the Trie
#t.print()
