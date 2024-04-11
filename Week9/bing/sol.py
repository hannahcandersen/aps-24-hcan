class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, x):
        current = self.root

        for char in x:
            current.count += 1
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.count += 1

        return current.count - 1

    def print(self):
            stack = [(self.root, "ROOT", 0)]
            while len(stack) > 0:
                node, c, depth = stack.pop()
                print(depth * "--", c, node.count)
                for c, child in node.children.items():
                    stack.append((child, c, depth + 1))


N = int(input())

t = Trie()
for _ in range(N):
    print(t.insert(input().strip()))

t.print()