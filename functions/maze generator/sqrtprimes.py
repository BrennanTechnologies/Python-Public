import math


def sqrt_of_primes(start, end):
    for num in range(start, end+1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
            print(num, math.sqrt(num))


sqrt_of_primes(1, 10)


def sqrt_of_primes1(start, end):
    for num in range(start, end+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            print(num, num**0.5)


sqrt_of_primes1(1, 20)
