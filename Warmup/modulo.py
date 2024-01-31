""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ouwzxz/problems/modulo
Author: Hannah Camilla Andersen (hcan)
Date:   30/01 2024

Description: 
- Input: 
    10 numbers n where 0 => n < 1000
- Output: 
    The number of distinct values when considered modulo 42
"""

# Function for calculating mod 42
def modulo(n): 
    return n % 42 

# Create list with input elements 
input_lst = []
for _ in range(10): 
   input_lst.append(int(input())) # Add line to list 
    
# Convert list to modolu 42 values 
mod_lst = map(modulo, input_lst)

# Find numbers of unique values. Convert to set and get length
mod_set = set(mod_lst)

# Print number of unique values 
print(len(mod_set)) 
