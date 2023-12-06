import sys

table = []
for line in sys.stdin:
    table.append(line[:-1])

ymax = len(table)
xmax = len(table[0])

machine_part = False
total = 0
num = 0

for j in range(ymax):
    for i in range(xmax):
        if table[j][i].isnumeric():
            num = num * 10 + int(table[j][i])
            for m in range(-1,2):
                for n in range(-1,2):
                    checkx = i + m 
                    checky = j + n
                    if checkx >= 0 and checkx < xmax and checky >=0 and checky < ymax:
                        if not table[checky][checkx].isnumeric() and table[checky][checkx] != '.':
                            machine_part = True
        else:
            if machine_part:
                total += num
            machine_part = False
            num = 0 



print(total)

        
    
    