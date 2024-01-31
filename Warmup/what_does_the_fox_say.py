""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ouwzxz/problems/whatdoesthefoxsay
Author: Hannah Camilla Andersen (hcan)
Date:   30/01 2024

Description: 
- Input: 
    T: Number of test cases
    Test cases: 
        The first line of each test case contains the recording
        Next lines are pre-known sounds of other animals (animal goes sound)
        The last line is: what does the fox say?
        
- Output: 
    - The sounds made by the fox, in the order from the recording.    
"""

t = int(input())

# Handle one test case. What does the fox says? 
def handle_test(rec, a_sounds):
    rec_sounds = rec.split()
    unknown_sounds = [sound for sound in rec_sounds if sound not in a_sounds] # Returns a list of sounds not found in a_sounds
    print((" ".join(unknown_sounds))) # Print list as a single string with spaces inbetween 
    
# Read all test cases
for _ in range(t): 
    recording = input()   
    animal_sounds = []  # List of known sounds
    while True:           
        iput = input()
        # Test case ended - handle this test case
        if iput == "what does the fox say?":  
            handle_test(recording, animal_sounds)
            break
        # Test case continues - update animal info
        else:
            info = iput.split()
            animal_sounds.append(info[2])
            
            
            
            
