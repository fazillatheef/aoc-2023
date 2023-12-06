import sys

result = 0
strs = "one two three four five six seven eight nine".split(" ")
for line in sys.stdin:
    st = ""
    ed = ""

    for i,c in enumerate(line):
        if st != "":
            break
        if c.isnumeric():
            st = c
            break
        for j in range(len(strs)):
            f = line.find(strs[j])
            if f == i:
                st = str(j + 1)   
                break
        
    for i in range(len(line)-1,-1,-1):
        if ed != "":
            break
        if line[i].isnumeric():
            ed = line[i]
            break
        for j in range(len(strs)):
            f = line.find(strs[j],i)
            if f == i:
                ed = str(j + 1)   
                break
    print(st+ed)
    result += int(st+ed)
    
print(result)
    