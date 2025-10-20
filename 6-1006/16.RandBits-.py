import random
def randbits(p, n):
    if n > p or n <= 0:
        return 0
    positions = random.sample(range(p), n)
    num = 0
    for pos in positions:
        num |= (1 << pos)
    #print(*positions)
    return num

#print(*[randbits(6, i) for i in range(1, 10)])