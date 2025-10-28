def manyfor(order, *sequences):
    output = []
    index_seq = [0] * len(sequences)
    iterators = []
    for sequence in sequences:
        if hasattr(sequence, '__iter__') and not isinstance(sequence,str):
            iterators.append(iter(sequence))
        else:
            iterators.append(sequence)
    #print(iterators)
    order_iter = iter(order)

    while True:
        try:
            current_index = next(order_iter)
            #print(next(iterators[current_index]))
            try:
                if hasattr(iterators[current_index], '__next__'):
                    output.append(next(iterators[current_index]))
                    #print(output)
                else:
                    output.append(iterators[current_index][index_seq[current_index]])
                    index_seq[current_index] += 1
                    #print(output)
            except (StopIteration,IndexError):
                break
        except (StopIteration,IndexError):
            break
    return output
# from itertools import count
# print(*manyfor([], "ae kha-kha", "Mnsatm", count(2, 2)))
# print(*manyfor((1, 0, 2) * 16, [], "Mnsatm", count(2, 2)))
# print(*manyfor((1, 0, 2) * 16, "ae kha-kha", [], count(2, 2)))
# print(*manyfor((1, 0, 2) * 16, "ae kha-kha", "Mnsatm", []))