"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/jm82a4/problems/holeynqueensbatman
Author: Hannah Camilla Andersen (hcan)
Date:  11/02 2024

Description:
You can’t place a queen on a square that has a hole, 
but a queen can threaten another even if there is a hole on the path between them
- Input:
    - N, M: Size of one side of the boards (3 <= N <= 12), number of holes. 
    - M * Holes: x,y 
    - End: 0 0
- Output:
    - Number of ways to place the queens on the board so that no queen threatens another.

"""

def search(row, n, m, holes, column, diag1, diag2):
    """
    Search recursively row by row for all possible solutions.

    Args:
        y: Current row to consider
        n: Size of the board (n x n)
        m: Number of holes
        holes: Set of holes
        column: Columns that contain a queen
        diag1: Diagonals (one way) that contain a queen
        diag2: Diagonals (other way) that contain a queen
        
    Complexity: Complete search, O(2^n)
    """
    
    count = 0 # Number of solutions
    
    # Successfully added a queen to each row
    if row == n: 
        return 1
    
    # Iterate through all columns in current row
    for col in range(n): 
        # Check if current place has a hole - queen can't be placed no matter what  
        if (row, col) in holes: 
            continue
        
        # Check if current column and diagonals are occupied - queen can't be placed
        if column[col] or diag1[row+col] or diag2[row-col+n-1]:
            continue
        
        # Spot available, place queen and update column and diagonals
        column[col] = diag1[row+col] = diag2[row-col+n-1] = True
        
        # Continue search with next row and update count
        count += search(row+1, n, m, holes, column, diag1, diag2)
        
        # Backtrack - Unmark column and diagonals to search for other solutions in the current row
        column[col] = diag1[row+col] = diag2[row-col+n-1] = False
    
    return count

# Handle one test case each iteration
while True:
    n, m = map(int, input().split())
    
    # Check if input is 0 0, if so we are done
    if n == 0 and m == 0: 
        break
    
    column = [False] * n         
    diag1 =  [False] * (2*n-1)   
    diag2 =  [False] * (2*n-1)   
    holes = set() 

    # Zero holes, handle special case
    if m == 0: 
        print(search(0, n, m, holes, column, diag1, diag2)) 
        continue
    
    # More than zero holes, read holes and add to set
    for _ in range(m):
        x, y = map(int, input().split())
        holes.add((x, y))

    # Test case done - handle it
    print(search(0, n, m, holes, column, diag1, diag2))
    
