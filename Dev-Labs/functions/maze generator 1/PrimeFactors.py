def factor(n):
    factors = []
    # Check if 2 is a factor
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd factors up to square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2
    # If n is prime, add it as a factor
    if n > 2:
        factors.append(n)
    return factors


print(factor(122333356783))
