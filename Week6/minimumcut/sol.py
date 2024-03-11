"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ehr4an/problems/mincut
Author: Hannah Camilla Andersen (hcan)
Date:   11/03 2024

Description:
Find minimum cut in a graph
- Input:
    - First line with 4 integers
        - N: number of nodes             (2 ≤ N ≤ 500
        - M: number of edges             (0 ≤ M ≤ 10000)
        - S: source node                 (0 ≤ s < N-1)'
        - T: sink node                   (0 ≤ t < N-1)
    - M lines with 3 integers
        - u: start node of edge         
        - v: end node of edge           
        - c: capacity of the edge       
- Output:
    - Begin with a line containing an integer, giving the size of U
    - Then follow k lines giving the vertices in U, one per line. 
    If there are multiple choices for U any one will be accepted
    
Solve it using the Ford-Fulkerson algorithm to find the maximum flow in the graph.
"""