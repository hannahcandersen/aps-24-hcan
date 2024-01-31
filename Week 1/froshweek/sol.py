""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/zr5cjv/problems/froshweek 
Author: Hannah Camilla Andersen (hcan)
Date:   31/01 2024

Description: 
- Input: 
    - n: First line. Number of students. 1 > n > 10^9 
    - s: n times student numbers (s). No student number will appear more than once
        
- Output: 
    - Minimum number of swaps required to arrange the students in increasing order by student number. 
    - This rearrangement of the line must be accomplished only by successively swapping pairs of consecutive students. 
"""

swaps = 0 

def mergeSort(myList):
    """
    Inspired by: https://www.educative.io/answers/merge-sort-in-python
    
    Args:
        myList: List or sub-list to perform mergesort on
        
    Complexity: O(n log n) - because the list is being split in log(n) calls and the merging process takes linear time in each call.
    """
    
    if len(myList) > 1:
        mid = len(myList) // 2 # integer division
        left = myList[:mid]
        right = myList[mid:]
        print(left, right)

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Iterators
        i = 0 # Left half
        j = 0 # Right half
        k = 0 # Result list (mylist)
        
        # Traverse sub-lists until one of the halves is exhausted
        while i < len(left) and j < len(right): 
            print("START: i: ", i, "j: ", j, "k: ", k, "left: ", left, "right: ", right, "myList:", myList)
            
            # If the current item (i) in left is smaller, add it to the result list
            # Update swaps with the number of spaces moved
            # And continue comparison for next element in left (i++)
            if left[i] <= right[j]: 
                myList[k] = left[i]  
                # Update swaps
                swaps += 1 # change
                i += 1 
            # Else, add the current item (j) in right to the result list
            # And continue comparison for next element in right (j++)
            else:
                myList[k] = right[j]
                # Update swaps
                swaps += 1 # change
                j += 1 
            # Move to the next slot in the result list
            k += 1
            
            print("END:   i: ", i, "j: ", j, "k: ", k, "left: ", left, "right: ", right, "myList:", myList)

        # Add remaining elements from the sub-list that is not exhausted
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1     
            
# Main
n = int(input())
students = []

for _ in range(n): 
    students.append(int(input()))

print(students) # Before sort
mergeSort(students)
print(students) # After sort
print(swaps)
            
