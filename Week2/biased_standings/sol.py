"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/jm82a4/problems/geppetto
Author: Hannah Camilla Andersen (hcan)
Date:  30/01 2024

Description:
For each team, compute the distance between their preferred place and their place in the ranklist. 
The sum of these distances will be called the badness of this ranklist.
Given team names and their preferred placements find one ranklist with the minimal possible badness.      
- Input: 
    - T: Number of test cases (T <= 20)
    - T * Test cases: 
        - Blank line
        - N: Number of teams (N <= 100.000)
        - N * Teams: name, place (1 <= place <= N)
- Output: 
    - The badness of the best possible ranklist

"""

t = int(input())

def find_best_ranklist(preferences):
    """
    Sort the dictionary by preference and count the badness of the ranklist made by the sorted dictionary.
    
    Complexity: 
    - Sorting the dictionary is O(n log n) (Timsort) 
    - Iterating over dictionary is O(n)
    """
    # Sort by preference increasing
    sorted_dict = dict(sorted(preferences.items(), key=lambda item: item[1])) # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    
    # Count the badness if added in the order of the sorted dictionary
    badness = 0
    for i, (_, preference) in enumerate(sorted_dict.items()):
        badness += abs(i+1 - preference) # Distance between preferred place and place in the ranklist
    
    print(badness)

# Read all test cases
for _ in range(t): 
    preferences = {}  # Dictionary to store team preferences for this test case
    input()           # Skip blank line 
    n = int(input())  # Number of teams
    for _ in range(n): 
        team, place = input().split()
        place = int(place)
        preferences.update({team: place})
    #print(preferences)
    find_best_ranklist(preferences)

