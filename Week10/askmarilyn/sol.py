"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/m2t8d3/problems/askmarilyn
Date:   22/04

Description:
- At the bar, there are three small boxes with doors labelled A, B, and C. When you buy a drink, Marilyn places the bottle in one of the boxes; you don’t know which.
- Then the following ritual unfolds. You point to one of the three doors. Marilyn will then smile enigmatically and open one of the other doors, showing its contents. You then get to change your original decision: maybe you now pick the door Marilyn just opened (in particular if you can see the bottle there!), or you stick with your first choice, or you pick the remaining door.
- This entire ritual -– you choose, Marilyn opens, you make your final decision – is called a round. 
- You’ll play 1000 rounds. You need to get as many drinks as you can.

Rounds of inputs and outputs:
Input:
- Guess: A, B or C
Output:
- The door Marilyn opens: A, B or C and 0 if the bottle is not there, 1 if the bottle is there
Input: 
- Final decision: A, B or C
Output:
- 1 A meaning, the bottle was in A
- 0 B meaning, the bottle was in B
After 1000 rounds, your program must exit. 
If you end up with at least 600 drinks, no matter which strategy Marilyn uses, your program is accepted. Otherwise it is judged as wrong answer.

Solution description:
- Randomly choose one of the doors 
- If she opens a door with the bottle, guess that door
- If she opens a door without the bottle, switch to the door that was not opened and not the original guess
This switching strategy is based on the Monty Hall problem, where switching after one non-prize door is revealed statistically provides a better chance of winning (2/3 chance).
"""

import random 

for round in range(1000): 
    # Initial guess is random
    guess = random.choice(["A", "B", "C"])
    print(guess)
    
    # Read the door Marilyn opens and if the bottle is there
    opened, has_bottle = input().split()
    has_bottle = int(has_bottle) # 1 = True, 0 = False
    
    # If she opened a door with the bottle, guess that door
    if has_bottle == 1:
        final_guess = opened
    # Else, always switch to the door that was not opened and not the original guess
    else:
        doors = ['A', 'B', 'C']
        remaining_doors = [door for door in doors if door not in [guess, opened]]
        final_guess = remaining_doors[0]

    print(final_guess)
    
    _ = input() # Read the result of the round
        
        
        