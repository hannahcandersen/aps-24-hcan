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
    - Must be accomplished only by successively swapping pairs of consecutive students. 
"""

swaps = 0


def mergeSort(myList):
    """
    Inspired by: https://www.educative.io/answers/merge-sort-in-python
    Complexity: O(n log n) - because the list is being split in log(n) calls and the merging process takes linear time in each call.
    """
    
    global swaps 
    
    if len(myList) > 1:
        mid = len(myList) // 2 # integer division
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Iterators
        i = 0 # Left half
        j = 0 # Right half
        k = 0 # Result list (modified mylist)
        
        # Traverse sub-lists until one of the halves is exhausted
        while i < len(left) and j < len(right): 
            # If left[i] is smallest, add it to the result list. No need to swap
            # Then continue comparison with next element in left (i++)
            if left[i] <= right[j]: 
                myList[k] = left[i]  
                i += 1 
            # If right[j] is smallest, add it to the result list and update swaps
            else:
                myList[k] = right[j]
                swaps += len(left) - i # The number of elements in left that are greater than right[j] is the spaces it needs to move               
                j += 1 
            k += 1

        # Add remaining elements from the sub-list that is not exhausted
        # The sublists are sorted, so no need to move
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

#print(students) 
mergeSort(students)
#print(students) 
print(swaps)
            
