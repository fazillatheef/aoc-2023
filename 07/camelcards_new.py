card_value = {"T":"A","J":"1","Q":"C","K":"D","A":"E"}
def rank(hand):
    count_cards = [hand.count(c) for c in hand if c != "J"]
    if 5 in count_cards:
        rank_group = 6
    elif 4 in count_cards:
        if hand.count("J") == 1:
            rank_group = 6
        else:
            rank_group = 5
    elif 3 in count_cards:
        if hand.count("J") == 2:
            rank_group = 6
        elif hand.count("J") == 1:
            rank_group = 5
        elif 2 in count_cards:
            rank_group = 4
        else:
            rank_group = 3
    elif 2 in count_cards:
        if hand.count("J") == 3:
            rank_group = 6
        elif hand.count("J") == 2:
            rank_group = 5
        elif hand.count("J") == 1: ###
            if count_cards.count(2) == 4:
                rank_group = 4
            else:
                rank_group = 3
        elif count_cards.count(2) == 4:
            rank_group = 2
        else:
            rank_group = 1
    elif "J" in hand:
        match hand.count("J"):
            case 5: rank_group = 6
            case 4: rank_group = 6
            case 3: rank_group = 5
            case 2: rank_group = 3
            case 1: rank_group = 1
    else:
        rank_group = 0

    rank_value = str(rank_group) + "".join([card_value.get(c,c) for c in hand])
    print(rank_value,hand)

    return rank_value

with open("input.txt") as games_file:
    games = []
    for line in games_file:
        cards,points = line.split()
        games.append((cards,int(points)))
        
games.sort(key = lambda x : rank(x[0]))

total = 0
for i,(h,p) in enumerate(games,1):
    total += (i*p)

print(total)
