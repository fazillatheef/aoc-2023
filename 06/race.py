import sys

for line in sys.stdin:
    if line.find("Time") > -1:
        time = list(map(int,line.split(":")[1].split()))
    if line.find("Distance") > -1:
        distance = list(map(int,line.split(":")[1].split()))

races = list(zip(time,distance))

def check_win(t,d):
    wins = 0
    for i in range(1,t):
        speed = i
        time_remaining = t - i
        distance = speed * time_remaining
        if distance > d:
            wins += 1
    return wins
    
wins = 1
for t,d in races:
    wins *= check_win(t,d)

print(wins)