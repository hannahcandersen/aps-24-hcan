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

"Easy solution"
"""

a, b, h = map(int, input().split())
worm_position = 0
times_climbed = 0

while worm_position < h: 
    worm_position += a # Climbs up
    times_climbed += 1 
    
    # Check if worm has reached the top, if not, it falls down
    if worm_position >= h:
        break
    
    worm_position -= b # Falls down

print(times_climbed)
