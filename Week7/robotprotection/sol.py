"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ehi4oo/problems/robotprotection
Author: Hannah Camilla Andersen (hcan)
Date:   20/03

Description:
Robotic guard should protect a polygonal area based on beacons placed
Robot walks toward a beacon in a straight line, then turns and walks to the next beacon
It can also stop and change turn at any time

Input: 
- Up to 30 configurations of beacons
    - n: number of beacons (1 ≤ n ≤ 10.000)
    - Next n lines: 
        - x, y: coordinates of the beacon (both in range -10000 to 10000)
Output:
For each configuration of beacons, output the area the robot has to patrol. 
Your answer should be accurate to within 0,1 square units.

Beacons are points in a polygonal area
Find convex hull of the points to find the area the robot has to patrol
Using Andrew's algorithm to find the convex hull

Complexity: O(n log n)
"""

def vec(p1,p2):
    # Returns the vector from p1 to p2
    return (p2[0]-p1[0],p2[1]-p1[1])

def orth_right(vec): 
    # Returns the vector orthogonal to vec, but rotated 90 degrees to the right
    return (vec[1],-vec[0])

def dotp(v1,v2):
    # Returns the dot product of two vectors. Used to determine if a point is to the right or left of a line
    return v1[0]*v2[0] + v1[1]*v2[1]

def isRight(p1,p2,p3):
    # Returns True if p3 is to the right of the line from p1 to p2
    return dotp(orth_right(vec(p1,p2)),vec(p2,p3)) > 0

def isLeft(p1,p2,p3):
    # Returns True if p3 is to the left of the line from p1 to p2
    return dotp(orth_right(vec(p1,p2)),vec(p2,p3)) < 0


########### Main ##########
while True:
    n = int(input()) # Number of beacons
    
    if n == 0:
        break
    
    # Construct list of beacons represented as tuples (x,y)
    beacons = [] 
    for _ in range(n):
        beacon = tuple(map(int,input().split()))
        beacons.append(beacon)
    
    # Sort beacons by x-coordinates
    beacons.sort() 
    
    # Divide and conquer by simoultaneously finding the upper and lower hull
    upper = beacons[:2]
    lower = beacons[:2]

    for b in beacons[2:]:
        # For upper hull, remove points that are to the right of the line from the second last to the last point
        while len(upper)>=2 and isLeft(upper[-2],upper[-1],b):
            upper.pop()
        upper.append(b)
        
        # For lower hull, remove points that are to the left of the line from the second last to the last point
        while len(lower)>=2 and isRight(lower[-2],lower[-1],b):
            lower.pop()
        lower.append(b)

    # Merge the upper and lower hulls
    # First and last point of upper and lower are the two extreme points in x direction
    hull = upper[:-1] + lower[::-1] # first and last point are the same - actually good here

    # Calculates the area of the trapezoid formed by two consecutive points.   
    # Shoelace formula 
    areas = [(hull[i+1][0] - hull[i][0]) *(hull[i+1][1]+hull[i][1])/2 for i in range(len(hull)-1)]
    
    # Sum the areas of the trapezoids to get the total area
    print(f"{sum(areas):.2f}")