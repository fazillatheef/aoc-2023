import sys
import re
r = 12
g = 13
b = 14

re_game = re.compile(r'Game (?P<game_num>\d+)')
re_color = re.compile(r'(?P<rnum>\d+) red|(?P<gnum>\d+) green|(?P<bnum>\d+) blue') 
total_game = 0
for full_line in sys.stdin:
    game_possible = True
    for line in full_line.split(';'):
        s = re_game.search(line)
        if s:
            game_num = s.group("game_num")
        for rc,gc,bc in re_color.findall(line):
            if rc == "": rc = 0
            if gc == "": gc = 0
            if bc == "": bc = 0
            if int(rc) > r or int(gc) > g or int(bc) > b:
                game_possible = False
    
    if game_possible:
        total_game += int(game_num)

print(total_game)
            