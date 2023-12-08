import math
import sys

maps =[]
single_map = []
for line in sys.stdin:
    if line.find("seeds:") > -1:
        seeds = [int(n) for n in line.split(":")[1].strip().split()]
    elif line.strip() == "":
        if len(single_map) == 0:
            continue
        else:
            maps.append(single_map)
    elif line.find("map:") > -1:
        single_map = []
    else:
        single_map.append([int(n) for n in line.strip().split()])


lowest = math.inf
for s in seeds:
    inp = s
    for conv in maps:
        output = inp
        for m in conv:
            if inp >= m[1] and inp <= m[1] + m[2]:
                output = inp - m[1] + m[0]
                break
        inp = output
    lowest = min(output,lowest)    

print(lowest)
# had to add a empty line in input because it
# was not taking the last mapping. Need to fix that.


