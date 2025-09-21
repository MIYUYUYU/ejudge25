k = int(input())
Number_of_digits = 0
number = 0
while True:
    x = (k * 10 ** Number_of_digits - k ** 2) % (10 * k - 1)
    if x != 0:
        Number_of_digits += 1
    else :
        x = (k * 10 ** Number_of_digits - k ** 2) // (10 * k - 1)
        break
print(10*x+k)

# k = int(input())
# digits = 1
# power = 10
# d = 10 * k - 1
#
# while True:
#     n = k * power - k * k
#     if n % d == 0:
#         A = n // d
#         if power // 10 <= A < power:
#             result = 10 * A + k
#             print(result)
#             break
#     digits += 1
#     power *= 10