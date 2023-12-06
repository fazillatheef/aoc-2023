import sys

result = 0
for line in sys.stdin:
    for c in line:
        if c.isnumeric():
            st = c
            break
    for c in line[::-1]:
        if c.isnumeric():
            ed = c
            break
    result += int(st+ed)
    
print(result)
    