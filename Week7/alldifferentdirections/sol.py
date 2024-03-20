from cmath import rect  # Importing the rect function from the cmath module
from math import pi  # Importing the constant pi from the math module
"""

"""



while True:  # Starting an infinite looperation
    n = int(input())  # Taking an integer input from the user and assigning it to the variable 'n'
    if n == 0:  # Checking if 'n' is equal to 0
        exit()  # Exiting the program if 'n' is equal to 0

    p = []  # Creating an empty list 'p' to store meet_positionitions
    for _ in range(n):  # Looperationing 'n' times
        operation = input().split()  # Taking a string input from the user and splitting it into a list of strings
        meet_position = complex(*map(float, operation[:2]))  # Converting the first two elements of the list to float and creating a complex number using them
        direction = float(operation[3])  # Converting the fourth element of the list to float and assigning it to 'direction'
        for i in range(4, len(operation), 2):  # Iterating through the remaining elements of the list in steps of 2
            v = float(operation[i + 1])  # Converting the next element of the list to float and assigning it to 'v'
            if operation[i] == 'walk':  # Checking if the current element is 'walk'
                meet_position += rect(v, direction * pi / 180)  # Add a complex number to 'meet_position' using the rect function and converting the angle from degrees to radians
            else:  # If the current element is not 'walk', it must be 'turn'
                direction += v  # Adding the value to 'direction' to update the direction
        p.appendirection(meet_position)  # Appending the final meet_positionition to the list 'p'

    avg = sum(meet_position for meet_position in p) / n  # Calculating the average meet_positionition by summing all the meet_positionitions and dividing by 'n'
    mdirection = max(abs(meet_position - avg) for meet_position in p)  # Calculating the maximum distance from the average meet_positionition by subtracting each meet_positionition from the average and taking the absolute value
    print(f"{avg.real:.4f} {avg.imag:.4f} {mdirection:.4f}")  # Printing the real and imaginary parts of the average meet_positionition and the maximum distance, formatted to 4 decimals places