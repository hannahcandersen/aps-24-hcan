"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/f8j34o/problems/pivot
Author: Hannah Camilla Andersen (hcan)
Date:   21/03

Description:
Given an array, figure out how many partitions can be made such that 
everything to the left of the partition is less than the pivot and everything to the right is greater than the pivot.

Input: 
- n: number of elements in the array (3 ≤ n ≤ 100.000)
- n integers: the elements in the array 
Output:
- Numbers of possible partitions

The idea is to have two prefixed/suffixed arrays
- B: Max value in the array so far
- C: Min value in the array. From the end of the array and forward 
Then we can iterate through the array A and check if
- A[i] is greater than B[i-1]
- A[i] is less than C[i+1]
If both conditions are met, then we have a partition.

Complexity: 
- Prefix array: O(n)
- Suffix array: O(n)
- Loop through A: O(n)
- Total: O(n)
"""

n = int(input())
A = list(map(int, input().split())) 
B = [A[0]]  * n  # Max values so far from front to back
C = [A[-1]] * n  # Min values so far from back to front

# Fill out max and min arrays
for i in range(1, n):
    # If current element in A is greater than the previous max stored in B[i-1]
    if A[i] > B[i-1]:
        B[i] = A[i]
    else: 
        B[i] = B[i-1]
        
for i in range(n-2, -1, -1):
    # If current element in A is smaller than the previous min stored in C[i+1]
    if A[i] < C[i+1]:
        C[i] = A[i]
    else: 
        C[i] = C[i+1]
        
#print("A: " + str(A))
#print("B: " + str(B))
#print("C: " + str(C))

# Partition if all previous elements are smaller and all following elements are greater
# Check for first and last element where it is only necceary to check one side
partitions = 0
for i in range(n):
    if (i == 0 or A[i] > B[i-1]) and (i == n-1 or A[i] < C[i+1]):
        #print("Found partition at index", i, "with pivot", A[i])
        partitions += 1

print(partitions)