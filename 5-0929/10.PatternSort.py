def pattsort (pattern, seq):
    pattern_pair = list(enumerate(pattern))
    sorted_pair = sorted(pattern_pair, key=lambda pair: pair[1])
    sorted_seq = sorted(seq)
    #print(sorted_pair)
    result = [0] * len(pattern)
    for i in range(len(pattern)):
        result[sorted_pair[i][0]] = sorted_seq[i]
    #print(result)

    return result

#print(*pattsort((5, 4, 6, 3, 8, 1), (2, 2, 6, 1, 9, 6)))