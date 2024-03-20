""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/zr5cjv/problems/grandpabernie
Author: Hannah Camilla Andersen (hcan)
Date:   31/01 2024

Description: 
- Input: 
    - n: Number of trips. 1 <= n <= 10^5
    - n times: 
        - s: Country visited
        - y: Year of visit. 1 <= y <= 10^6
    - q: Number of queries. 1 <= q <= 10^5
    - q times: 
        - s: Country to query
        - k: kth visit to country.     
- Output: 
    - For each query output a line containing the year in which Grandpa Bernie went on that trip. 
"""

# Use a dictionary to store the trips
# Key: Country
# Value: List of years
trips = {}

# Read trip history 
n = int(input())

for _ in range(n): 
    country, year = input().split()
    year = int(year)
    if country not in trips: 
        trips[country] = []
    trips[country].append(year)

# Sort the lists of years for each country
for country in trips: 
    trips[country].sort()
    
# Read queries and look up the year in trips dict
q = int(input())

for _ in range(q): 
    country, k = input().split()
    k = int(k)
    print(trips[country][k-1]) # k-1 because lists are 0-indexed
    