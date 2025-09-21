state, n, a, b = map(int,input().split(','))
mask64 = (1 << 64) - 1
#print(type(state))
for i in range(n):
    state ^= state << 7 & mask64
#    print(f"step{i}: state<<7 = {bin(state)}")
    state ^= state >> 9 & mask64
#    print(f"step{i}: state>>9 = {bin(state)}")
range_s =  b - a + 1
result = a + (state % range_s)
#print(f"result = {bin(result)}")
print (result)