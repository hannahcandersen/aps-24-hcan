"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/cqrk6f/problems/tight
Author: Hannah Camilla Andersen (hcan)
Date:  21/02 2024

Description:
Given is an alphabet {0,1,..,k}, 0 <= k <= 9. 
We say that a word of length n over this alphabet is tight 
if any two neighbour digits in the word do not differ by more than 1.
- Input:
    - K, N: The alphabet size and the length of the word (1 <= K <= 9, 1 <= N <= 100)
- Output:
    - For each line, output the percentage of tight words of length n over the given alphabet.
"""
def solve(k, n):
    """
    Uses dynamic programming (iterative) to find the percentage of tight words of length n over the given alphabet.

    Args:
        k (int): Size of the alphabet. The alphabet then corresponds to {0,1,..,k}.
        n (int): Length of the word

    Returns:
        int: Percentage of tight words of length n over the given alphabet
    """
    
    # results[i][j] represents the number of tight words of length i ending with digit j.
    results = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Base case: There is 1 tight word of length 1 for each digit in the alphabet (the digit itself).
    for j in range(k + 1):
        results[1][j] = 1

    # Fill the results table for lengths from 2 to N.
    for i in range(2, n + 1):
        # For each digit in the alphabet
        for j in range(k + 1):
            # Extend the prior word of length i-1 with the digit j.
            # Calculate the sum of tight words ending with j, j-1 or j+1
            # Add the number of tight words of length i-1 ending with j (meaning the last digits are j, j)
            results[i][j] = results[i - 1][j] 
            # Add the number of tight words of length i-1 ending with j-1 (meaning the last digits are j-1, j)
            if j > 0:
                results[i][j] += results[i - 1][j - 1]
            # Add the number of tight words of length i-1 ending with j+1 (meaning the last digits are j+1, j)
            if j < k:
                results[i][j] += results[i - 1][j + 1]

    # Sum all tight words of length N
    total_tight_words = sum(results[n])

    # Total possible words of length N 
    total_possible_words = (k + 1) ** n

    # Calculate the percentage of tight words among all possible words.
    return (total_tight_words / total_possible_words) * 100

while True:
    try:
        k, n = map(int, input().split())
        percentage = solve(k, n)
        print(f"{percentage:.9f}") # Print with 9 decimals
    except EOFError: # No more input
        break
