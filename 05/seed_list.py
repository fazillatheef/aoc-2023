import math
import sys

maps =[]
single_map = []
for line in sys.stdin:
    if line.find("seeds:") > -1:
        seed_list = [int(n) for n in line.split(":")[1].strip().split()]
        seeds = [(seed_list[i],seed_list[i]+seed_list[i+1]) for i in range(0,len(seed_list),2)]
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

for conv in maps:
    trys = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for m in conv:
            os = max(s,m[1])
            oe = min(e,m[1] + m[2])
            if os < oe:
                trys.append((os - m[1] + m[0],oe - m[1] + m[0]))
                if os > s:
                    seeds.append((s,os))
                if oe < e:
                    seeds.append((oe,e))
                break
        else:
            trys.append((s,e))
    seeds = trys
lowest = min(trys)    

print(lowest[0])
# had to add a empty line in input because it
# was not taking the last mapping. Need to fix that.
# Need to make this version faster - need to use the map to split the seed ranges??


