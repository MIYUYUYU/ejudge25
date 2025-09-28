P = [int(x.strip()) for x in input().split(',')]
Q = [int(y.strip()) for y in input().split(',')]
if len(P) == 1:
    if P[0] in Q:
        print("YES")
        exit(0)
    else:
        print("NO")
        exit(0)
step = Q.index(P[1]) - Q.index(P[0])
first = Q.index(P[0])
j = 0
found = True
for i in range(first, len(Q), step):
    if j >= len(P):
        break
    else:
        if P[j] != Q[i]:
            print("NO")
            found = False
            break
        j += 1
if found:
    print("YES")
# print(f"first = {first}")
# print(f"step = {step}")
# print(P)
# print(Q)