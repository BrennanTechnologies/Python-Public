a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for x in a:
    if x % 2 == 0:
        sum += x
        print(x)

print(sum)
