def manyfor(order, *sequence):
    # 为每个序列创建迭代器和索引跟踪
    iterators = []
    indices = [0] * len(sequence)

    for i, seq in enumerate(sequence):
        if hasattr(seq, '__iter__') and not isinstance(seq, str):
            # 对于可迭代对象，创建迭代器
            iterators.append(iter(seq))
        else:
            # 对于其他类型，保持原样
            iterators.append(seq)
    #print(iterators)
    output = []

    # 始终将 order 作为迭代器处理
    order_iter = iter(order)

    while True:
        try:
            # 获取下一个序列索引
            seq_index = next(order_iter)

            # 获取当前序列和对应的迭代器
            current_seq = sequence[seq_index]
            current_iter = iterators[seq_index]
            #print(iterators[seq_index])

            if hasattr(current_iter, '__next__'):
                # 如果是迭代器，直接调用 next()
                element = next(current_iter)
                output.append(element)
            elif hasattr(current_seq, '__getitem__'):
                # 如果是支持下标的序列，使用索引访问
                try:
                    element = current_seq[indices[seq_index]]
                    output.append(element)
                    indices[seq_index] += 1
                except IndexError:
                    # 序列耗尽，结束循环
                    break

        except (StopIteration, IndexError):
            # 当序列耗尽或索引超出范围时结束
            break

    return output
# print("".join(manyfor((1, 0, 2) * 16, "ae kha-kha", "Mnsatm", "nrme noob")))
#from itertools import count
# print()
# print(*manyfor((1, 0, 2) * 16, "ae kha-kha", "Mnsatm", count(2, 2)))
# print(*manyfor(count(1), "ae kha-kha", "Mnsatm", "nrme noob"))
# print(*manyfor((1, 0, 2) * 16, count(2, 2), "Mnsatm", "nrme noob"))
# print(*manyfor((1, 0, 2) * 16, "ae kha-kha", count(2, 2), "nrme noob"))
# print()
# print(*manyfor([], "ae kha-kha", "Mnsatm", count(2, 2)))
#print(*manyfor((1, 0, 2) * 16, [], "Mnsatm", count(2, 2)))
#print(*manyfor((1, 0, 2) * 16, "ae kha-kha", [], count(2, 2)))
# print(*manyfor((1, 0, 2) * 16, "ae kha-kha", "Mnsatm", []))
# print()
from itertools import cycle, repeat
N = 300000
print(sum(manyfor(cycle(range(3)), cycle(range(4)), repeat(1), repeat(2, N))))