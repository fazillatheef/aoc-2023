import sys

for line in sys.stdin:
    if line.find("Time") > -1:
        time = int(line.split(":")[1].replace(" ","").strip())
    if line.find("Distance") > -1:
        distance = int(line.split(":")[1].replace(" ","").strip())

def check_win(t,d):
    wins = 0
    for i in range(1,t):
        speed = i
        time_remaining = t - i
        distance = speed * time_remaining
        if distance > d:
            wins += 1
    return wins

print(time,distance)
print(check_win(time,distance))