card_value = {"T":"A","J":"B","Q":"C","K":"D","A":"E"}
def rank(hand):
    count_cards = [hand.count(c) for c in hand]
    if 5 in count_cards:
        rank_group = 6
    elif 4 in count_cards:
        rank_group = 5
    elif 3 in count_cards:
        if 2 in count_cards:
            rank_group = 4
        else:
            rank_group = 3
    elif 2 in count_cards:
        if count_cards.count(2) == 4:
            rank_group = 2
        else:
            rank_group = 1
    else:
        rank_group = 0

    return str(rank_group) + "".join([card_value.get(c,c) for c in hand])

with open("input.txt") as games_file:
    games = []
    for line in games_file:
        cards,points = line.split()
        games.append((cards,int(points)))
        
games.sort(key = lambda x : rank(x[0]))
print(games)
total = 0
for i,(h,p) in enumerate(games,1):
    total += (i*p)

print(total)
