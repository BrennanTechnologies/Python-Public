# For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the function should return [2, 4, 6, 8, 10].

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
        print(x)

print(b)
