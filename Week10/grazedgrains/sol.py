"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/m2t8d3/problems/grazedgrains
Author: Hannah Camilla Andersen (hcan)
Date:   22/04

Description:
- In total n circular UFOs have landed in Celeste’s field. 
The ith one left a crop circle which destroyed all crops within radius ri of the point xi, yi
Field extends indefinitely in all directions
Estimate the total area of the field that is destroyed by the UFOs
Estimate = error less than 10% 

Input:
- N: number of UFOs (1 ≤ N ≤ 10)
- N lines with x, y, r describing the crop circle
Output:
- The total area covered by the crop circles in the input, with a relative error of at most 1/10

Solution description:
- Use randomness to generate points in the field and check if they are inside any of the crop circles
- Calculate the area based on the proportion of points inside the circles
"""

import random

n = int(input()) # Number of UFOs

# list of list(x,y,r) for each UFO
ufos = [list(map(int, input().split())) for _ in range(n)]

TOTAL = 100000 # The total number of random points generated. Higher number gives more accurate results.
HITS = 0  # The number of random points that are inside a crop circle

# Generating random points to sample the area.
for _ in range(TOTAL):
    # Generate a random point (x, y). 
    x, y =  random.random() * 30 - 10,  random.random() * 30 - 10

    #print(f"Check ({x}, {y})")

    # Check if the point is inside any of the crop circles
    for ufo_x, ufo_y, ufo_r in ufos:
        if (x - ufo_x)**2 + (y - ufo_y)**2 <= ufo_r ** 2:
            # If the point is inside a circle, increase the HITS counter and stop checking further.
            HITS += 1
            break

# Calculating the estimated area based on the proportion of hits and the assumed total area sampled.
print(HITS/TOTAL * 900)

