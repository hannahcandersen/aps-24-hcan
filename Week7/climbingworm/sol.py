"""
a = how far it can climb at a time
b = how far it falls down
h = height of the pole

Output = number of times the worm has to climb up the pole
"""

a, b, h = map(int, input().split())
worm_position = 0
times_climbed = 0

while worm_position < h: 
    worm_position += a # Climbs up
    times_climbed += 1 
    
    # Check if worm has reached the top, if not, it falls down
    if worm_position >= h:
        break
    
    worm_position -= b # Falls down

print(times_climbed)
