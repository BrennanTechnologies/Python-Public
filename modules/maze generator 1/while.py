a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))
breakpoint()

i = 0
n = 12
# while i < 10:
# while i * i <= n:
while i <= n:
    print(i)
    i += 1

print("Done with loop")


'''
i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2

'''
