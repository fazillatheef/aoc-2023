import sys
import re
max_r = 0
max_g = 0
max_b = 0

re_color = re.compile(r'(?P<rnum>\d+) red|(?P<gnum>\d+) green|(?P<bnum>\d+) blue') 
total_game = 0
for full_line in sys.stdin:
    max_r = 0
    max_g = 0
    max_b = 0
    for line in full_line.split(';'):
        for rc,gc,bc in re_color.findall(line):
            if rc == "": rc = 0
            if gc == "": gc = 0
            if bc == "": bc = 0
            if int(rc) > max_r:
                max_r = int(rc)
            if int(gc) > max_g:
                max_g = int(gc)
            if int(bc) > max_b:
                max_b = int(bc)
    
    total_game += max_r * max_g * max_b

print(total_game)
            