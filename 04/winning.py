import sys

points = 0
for line in sys.stdin:
    win = [False] * 100
    game,data = line.split(":")
    lucky_nums,your_nums = data.split("|")
    for num in lucky_nums.replace("  "," ").strip().split(" "):
        win[int(num)] = True
    
    game_point = 0
    for num in your_nums.replace("  "," ").strip().split(" "):
        try:
            if win[int(num)] == True:
                if game_point == 0:
                    game_point = 1
                else:
                    game_point =  2*game_point
        except:
            print(line)
    points += game_point

print(points)
    