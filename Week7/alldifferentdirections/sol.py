"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ehi4oo/problems/alldifferentdirections
Author: Hannah Camilla Andersen (hcan)
Date:   20/03

Description:
Ask n people for directions.
Compute average direction that they all lead to.
Compute the maximum straigt line distance between each direction from the average direction.
- Input:
    - Up to 100 test cases (lines)
        - n: number of people (1 ≤ n ≤ 20)
        - Following n lines (x,y) direction: 
            - (x,y): Where you meet the person
            - A number of instructions (max 25) of the form
                - start a: Initial direction you are facing
                - turn a: angle you turn in degrees. Negative for right, positive for left
                - walk x: number of units to walk in the current direction
- Output:
    - For each test case, print a line with the and coordinates of the average destination, followed by the distance between the worst directions and the averaged destination.

Solve it by converting the directions to complex numbers and using the rect function from the cmath module to calculate the average direction and the maximum distance from the average direction.
"""
from cmath import rect
from math import pi

while True:
    n=int(input()) # Number of people
    if n == 0:
        exit()
    
    p = [] # List of positions
    
    for _ in range(n):
        op = input().split() # x, y, start, turn, walk, turn, walk, ...
        pos = complex(*map(float,op[:2])) # Start position as complex number
        direction = float(op[3]) # Start direction
        
        # Handle instructions
        for i in range(4,len(op),2): # Start at 4, step 2
            # print("xyd",x,y,d, op[i],op[i+1])
            value = float(op[i+1]) # Value to turn or walk (number)
            
            if op[i] == 'walk':
                # print("walk",v)
                pos += rect(value,direction * pi / 180) # Update position with rect function
                # RECT: Walking a certain distance corresponds to adding a complex number with a certain magnitude (the distance walked) and argument (the current direction) to the current position. This is done using the rect function, which creates a complex number with a given magnitude and argument.
            else: # turn
                direction += value # Update direction
                
        p.append(pos) # Add position to list of positions
        
    # Calculate average direction by summing all complex numbers and dividing by n    
    average_direction = sum(pos for pos in p) / n
    # Calculate maximum distance from average direction by comparing the absolute value of the difference between each position and the average position
    max_direction = max( abs(pos-average_direction) for pos in p )
    
    # Print result. .4f to print 4 decimals 
    print(f"{average_direction.real:.4f} {average_direction.imag:.4f} {max_direction:.4f}")
    # x, y, max