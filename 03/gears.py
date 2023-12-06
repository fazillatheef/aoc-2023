class part:
    def __init__(self,xpos,ypos,length,value):
        self.xpos = xpos
        self.ypos = ypos
        self.length = length
        self.value = value
    def __repr__(self):
        return f"{self.value} @ {self.xpos},{self.ypos} with {self.length} length"
class gear:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.parts = []
    def __repr__(self):
        return f"Gear found at {self.xpos},{self.ypos} with parts {[p for p in self.parts]}"
        
import sys

num = 0
xpos = 0
ypos = 0
all_parts = []
all_gears = []
for line in sys.stdin:
    for c in line:
        if c.isnumeric():
            num = 10 * num + int(c)
        else:
            if num > 0:
                lstr=len(str(num))
                all_parts.append(part(xpos - lstr,ypos,lstr,num))
            if c == "*":
                all_gears.append(gear(xpos,ypos))
            num = 0
        xpos += 1
    xpos = 0
    ypos += 1

for g in all_gears:
    for p in all_parts:
        if g.xpos >= p.xpos - 1 and g.ypos >= p.ypos - 1 and g.xpos <= p.xpos + p.length and g.ypos <= p.ypos + 1:
            g.parts.append(p)
total = 0
for g in all_gears:
    if len(g.parts)> 1:
        power = 1
        for p in g.parts:
            power *= p.value 
        total += power

print(total)