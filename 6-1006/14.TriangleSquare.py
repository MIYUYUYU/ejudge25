import decimal
decimal.getcontext().prec = 1000

x1, y1, x2, y2, x3, y3 = [decimal.Decimal(x.strip()) for x in input().split(',')]
a1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2).sqrt()
a2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2).sqrt()
a3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2).sqrt()
s = (a1 + a2 + a3) / 2
area = (s * (s - a1) * (s - a2) * (s - a3)).sqrt()
print (f"{area:.200f}".rstrip('0').rstrip('.'))