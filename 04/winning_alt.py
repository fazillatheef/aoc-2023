import sys
cards =[]
card_num = 0
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
                game_point += 1
        except:
            print(line)
            exit()
    cards.append(game_point)

print(cards)

def count_cards(cards,pos):
    if len(cards) == 1:
        return 1
    if len(cards) == 0:
        return 0
    sum = 1
    for i in range(cards[pos]):
        sum += count_cards(cards[pos:],min(i+1,len(cards)))
    return sum

total_count = 0
for i in range(len(cards)):
    total_count += count_cards(cards[i:],0) 
print(total_count)

# Need to find if there is a better way to write this recursion






     