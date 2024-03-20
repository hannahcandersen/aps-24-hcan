""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/zr5cjv/problems/busnumbers?tab=metadata
Date:   31/01 2024

Description: 
- Input: 
    - n: Number of busses. 1 <= n <= 1000
    - list: n times bus numbers seperated by spaces. 
- Output: 
    - Shortest representation of the list of bus numbers.  
    - 3+ consecutive numbers are represented by the first and last number seperated by "-"
"""

n = int(input())
bus_numbers = list(map(int, input().split())) # Read and convert to list of ints
sequence_of_strings = []

# Sort the list
bus_numbers.sort()

# Run through the list and add correct string representation
i = 0
while i < len(bus_numbers):
    start = bus_numbers[i] # Start of potential sequence
    end = start            # End of potential sequence

    # Check for consecutive numbers and find end of sequence
    while i < len(bus_numbers) - 1 and bus_numbers[i + 1] == bus_numbers[i] + 1:
        end = bus_numbers[i + 1] 
        i += 1

    if start == end: # No consecutive
        sequence_of_strings.append(str(start))
    elif end - start == 1:  # Only two consecutive
        sequence_of_strings.append(str(start))
        sequence_of_strings.append(str(end))
    else: # 3+ consecutive
        sequence_of_strings.append(f"{start}-{end}")
    
    i += 1

result = " ".join(sequence_of_strings) # Join the list of strings into one string seperated by spaces
print(result)
