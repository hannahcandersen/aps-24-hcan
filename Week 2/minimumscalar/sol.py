"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/jm82a4/problems/minimumscalar
Author: Hannah Camilla Andersen (hcan)
Date:  12/02 2024

Description:
You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). 
The scalar product of these vectors is a single number, calculated as x1*y1 + x2*y2+ ... + xn*yn.
Suppose you are allowed to permute the coordinates of each vector as you wish.
- Input: 
    - T: Number of test cases (T <= 10)
    - T * Test cases: 
        - N: Numbers in vector (1 <= N <= 800)
        - 2 * N * x: Numbers in vector, where -100.000 <= x <= 100.000
- Output: 
    - For each test case, output a line Case #X: Y
        where X is the test case number, starting from 1, 
        and Y is the minimum scalar product of all permutations of the two given vectors.
"""

def find_min_scalar_product(v1, v2):
    """
    Use greedy approach to find the minimum scalar product, 
    by ordering the vectors and multiplying the smallest with the largest.
    Inspiration: https://prepinsta.com/python-program/finding-minimum-scalar-product-of-two-vectors/ 

    Args:
        v1 (int list): First vector
        v2 (int list): Second vector
        
    Complexity: O(n log n) for sorting (Timsort) 
                + O(n) for iterating over the vectors
    """
    
    # Sort the vectors
    v1.sort()             # Smallest number first
    v2.sort(reverse=True) # Largest number first
    
    # Find the scalar product (msp) of the sorted vectors
    msp = 0
    for i in range(n):
        msp += v1[i]*v2[i]
        
    return msp

# Read and handle all test cases
t = int(input())
for i in range(t):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    
    print(f"Case #{i+1}: {find_min_scalar_product(v1, v2)}")
