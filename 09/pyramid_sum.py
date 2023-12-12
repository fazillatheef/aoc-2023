def next_seq(seq):
    # There is something wrong abt this
    s = seq[-1]
    while not all(x==0 for x in seq): # this was sum, which is wrong if you have negative numbers
        new_seq = []
        for i in range(len(seq)-1):
            new_seq.append(seq[i+1] - seq[i])
        seq = new_seq
        s += seq[-1]
    return s

def extrapolate(array):
    if all(x==0 for x in array):
        return 0
    
    deltas = [y -x for x,y in zip(array,array[1:])]
    diff = extrapolate(deltas)
    return array[-1] + diff

with open("input.txt") as seqs:
    sm = 0
    for seq in seqs:
        sm += next_seq([int(x) for x in seq.split()])

print(sm)
