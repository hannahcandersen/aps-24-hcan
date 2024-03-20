"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/f8j34o/problems/supercomputer
Author: Hannah Camilla Andersen (hcan)
Date:   20/03

Description:
Add N-bit memory that supports two operations:
- Flip the bit at position i
- Given l and r, count the number of 1-bits in the range [l,r]
All bits in the memory are initially set to 

Input:
- First line: n, k: number of bits in memory (1 ≤ n ≤ 1.000.000), number of queries (1 ≤ k ≤ 100.000)
- k lines of either: 
    - F i: Flip bit i (1 ≤ i ≤ n)
    - C l r: Count number of 1-bits in range [l,r] (1 ≤ l ≤ r ≤ n)
    
Output:
- For each query of type C, output the number of 1-bits in the range [l,r]

Solve it using a segment tree.
Use sum queries where bit 1 contributes with 1 to the sum and bit 0 does not.
Complexity:
- Construction: O(n) 
- Query: O(log n)
- Update: O(log n)
"""

###### SEGMENT TREE ######
class SegmentTree():
    def __init__(self, n):
        # Build a segment tree array with 2n elements 
        ## Root node is placed at 1 (1-indexed). Contains sum of all elements.
        ## Parent node is placed at N//2. Contains sum of children
        ## Leaf nodes are placed at N to 2N
        ## This means the children of node i are found at 2*i and 2*i + 1
        
        # Find the smallest power of 2 that is greater than n to make the tree complete
        self.N = 1 
        while self.N < n:
            self.N *= 2
        
        # Build array A with 2n elements, all initally set to 0
        self.A = [0 for _ in range(2 * self.N)]

    def get(self, i):
        # Get the value of the i-th element
        return self.A[self.N + i] # 1-indexed
    
    def update(self, i, k):
        # Update the i-th element to k and recalculate the affected nodes
        
        # Find leaf node position. 
        pos = self.N + i
        # Set the value of the leaf node to k
        self.A[pos] = k
        
        # Continiously update the parent nodes until reaching the root
        pos //= 2
        while pos > 0:
            # Update parent to sum of children
            self.A[pos] = self.A[2 * pos] + self.A[2 * pos + 1] 
            pos //= 2
    
    def query(self, i, j):
        # Sum of elements from i-th to j-th element
        return self.__bottom_up_range_sum(i, j)
        #return self.__top_down_range_sum(1, 0, self.N, i, j + 1)

    def __bottom_up_range_sum(self, i, j):
        # Find index of leaf nodes
        i += self.N
        j += self.N

        sum = 0
        while i <= j: # 
            # Odd = Right child 
            if i % 2 == 1:
                # Add value of the node to the sum
                sum += self.A[i]
                i += 1 
            # Even = Left child
            if j % 2 == 0:
                # Add value of the node to the sum
                sum += self.A[j]
                j -= 1 
            i //= 2 # Move up to parent
            j //= 2 # Move up to parent
        return sum

    # Alternative solution using top-down recursion
    def __top_down_range_sum(self, p, start, span, i, j):
        # If the range [i,j] is outside the range [start, start+span]
        if start + span <= i or j <= start:
            return 0
        # If the range [i,j] is completely inside the range [start, start+span]
        if i <= start and start + span <= j:
            return self.A[p] 
        
        # Recursively find the sum of the left and right child
        left = self.__top_down_range_sum(2 * p, start, span // 2, i, j)
        right = self.__top_down_range_sum(2*p + 1, start + span // 2, span // 2, i, j)
        
        return left + right

###### MAIN ######
n, k = map(int, input().split()) # Number of bits, number of queries
st = SegmentTree(n) # Initialize segment tree with n bits

for _ in range(k):
    op, *args = input().split() # Operation, arguments
    
    if op == 'F':
        i = int(args[0]) - 1 # Bit to flip 
        st.update(i, 1 - st.get(i)) # Flip the bit. k is 1 if 0, 0 if 1
    else: # op == 'C'
        l, r = map(int, args) # Range
        print(st.query(l-1, r-1)) 