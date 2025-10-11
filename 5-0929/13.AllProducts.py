def get_factorizations(n):
    result = []

    def factorize(start, remain, current):
        #剩余为1说明全分解
        if remain == 1:
            result.append(current)
            return

        #将剩余大数直接加入分组
        if not current or remain >= current[-1]:
            result.append(current + [remain])

        #分解剩余数
        for i in range(start, int(remain ** 0.5) + 1):
            if remain % i == 0:
                current.append(i)
                factorize(i, remain // i, current)
                current.pop()

    factorize(2, n, [])
    result.sort()
    return result


n = int(input().strip())
factorizations = get_factorizations(n)

for factors in factorizations:
    for i in range(len(factors)-1):
        print(factors[i], end = '*')
    print(factors[-1])
#print(factorizations,sep='*')

