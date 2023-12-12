def next_seq(seq):
    s = seq[-1]
    while not all(x==0 for x in seq):
        new_seq = []
        for i in range(len(seq)-1):
            new_seq.append(seq[i+1] - seq[i])
        seq = new_seq
        s += seq[-1]
    return s

def extrapolate(array):
    if all(x==0 for x in array):
        return 0
    
    deltas = [y-x for x,y in zip(array,array[1:])]
    diff = extrapolate(deltas)
    return array[0] - diff

with open("input.txt") as seqs:
    sm = 0
    for seq in seqs:
        sm += extrapolate([int(x) for x in seq.split()])

print(sm)