"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ehi4oo/problems/climbingworm
Author: Hannah Camilla Andersen (hcan)
Date:   20/03

Description:
Worm can crawl up a distance a, but falls down b distance every night. 
How many days does it take for the worm to reach the top?

Input: 
- One line with three integers a, b, h: 
    - a: Distance worm can climb up in a day (0 ≤ a ≤ b ≤ 100)
    - b: Distance worm falls down in a day (0 ≤ a ≤ b ≤ 100)
    - h: Height of pole (1 ≤ h ≤ 100.000)
Output:
- Number of days it takes for the worm to reach the top.

Solve it using the formula: ceil((h - a) / (a - b)) + 1
h-a = distance from start to the next-to-last climb
a-b = distance climbed in each cycle
Therefore (h-a) / (a-b) is the times it takes to get to the next-to-last climb
Add one for the final climb itself (as it does not fall down after climbing to the top)
Ciel to round up to the nearest whole number
"""

from math import ceil

def calculate_climbs(a, b, h):
    # If the worm can reach the top in a single climb, return 1
    if a >= h:
        return 1
    # Calculate the number of complete cycles
    return ceil((h - a) / (a - b)) + 1 

a, b, h = map(int, input().split())
print(calculate_climbs(a, b, h))