"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/zwdnut/problems/quiteaproblem
Author: Hannah Camilla Andersen (hcan)
Date:   14/04

Description:
- Find out if the word "problem" appears in a given string.

Input:
- A line of most 80 characters
Output:
- print "yes" if the word "problem" appears in the string, otherwise print "no"

Solution description:
- String matching
"""
import sys

def find_problem():
    for line in sys.stdin:
        # Convert the line to lowercase
        line = line.lower()
        # Check if 'problem' is in the line
        if 'problem' in line:
            print('yes')
        else:
            print('no')

find_problem()