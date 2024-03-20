"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/jm82a4/problems/geppetto
Author: Hannah Camilla Andersen (hcan)
Date:  30/01 2024

Description:
There are M pairs of ingredients that cannot be on the same pizza at the same time. 
Given these restrictions, Geppetto wants to know how many different pizzas he can make.  
- Input:
    - N, M: Number of ingredients, number of forbidden pairs (1 <= M <= 20)
    - M * Forbidden pairs: a,b (1 <= a,b <= N) 
- Output:
    - Number of different pizzas Geppetto can make with the given restrictions.

"""

n, m = map(int, input().split())
forbidden_pairs = set() # To avoid duplicates

# Read forbidden pairs and add to set
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1 # 0-indexing
    b -= 1 # 0-indexing
    # Add them sorted to the set to avoid duplicates like (a,b) and (b,a)
    forbidden_pairs.add(tuple(sorted([a,b])))

def search(subset, k):
    """
    Search recursively for all possible subsets.

    Args:
        subset: Current subset of ingredients 
        k: Current ingredient to consider
        
    Complexity: Complete search, O(2^n)
    """
    
    if k == n: # Succesful subset
        return 1
    else:
        cnt = 0
        # Generate subsets with k not being part
        cnt += search(subset, k + 1)
        # Generate subsets with k being part
        # Check if adding k'th ingredient to the current pizza is possible
        for i in subset:
            if (i, k) in forbidden_pairs:
                return cnt # If not, return the count without adding k to the subset
        subset.append(k) # If possible, add k to the subset
        cnt += search(subset, k + 1) # And continue the search
        subset.pop() # Backtrack
        return cnt

print(search([], 0))