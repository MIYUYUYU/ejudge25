N = int(input())
x = y = z = t = 0
if N == 0:
    print(f'{x} {y} {z} {t}')
else:
    #print(N**0.5)
    for x in range(1 + int(N**0.5)):
        max_y= min(x,int((N - x * x)**0.5))
        for y in range(max_y + 1):
            max_z = min(y, int((N - x * x - y * y)**0.5))
            for z in range(max_z + 1):
                rest = N - x * x - y * y  - z * z
                sqrt_rest = rest ** 0.5
                if rest < 0 or sqrt_rest > z:
                    continue
                elif  ((t:=int(sqrt_rest))*t) == rest:
                    print(f'{x} {y} {z} {t}')


#print(int(99**0.5)**2)++