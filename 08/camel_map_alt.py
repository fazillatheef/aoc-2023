# This only worked because the input file is created in such a way that starting from A to Z is 
# repeating with the same interval. Otherwise we will need to add the steps from Z to A to get 
# distance between Z to Z
from math import lcm

records = open("input.txt").read().split('\n')

direction = records[0]

mapping = {}
for map in records[2:]:
    src,dest = [x.strip() for x in map.split("=")]
    links = [x.strip() for x in dest[1:-1].split(",")]
    mapping[src] = links

print(mapping)

current_loc = [x for x in mapping.keys() if x.endswith('A')]

print(current_loc)

steps = []
for loc in current_loc:
    print(loc)
    step = 0
    l = loc
    while True:
        found = False
        for d in direction:
            if l.endswith('Z'):
                steps.append(step)
                found = True
                break
            step += 1
            if d == 'R':
                l = mapping[l][1]
            else:
                l = mapping[l][0]
        if found:
            break

print(steps)
final = steps.pop()
for i in range(len(steps)):
    final = lcm(final,steps[i])

print(final)

        



