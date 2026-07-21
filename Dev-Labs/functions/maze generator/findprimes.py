def find_primes(n):
    # create a boolean array indicating whether each number less than n is prime
    is_prime = [True] * n

    # set the first two numbers to be composite (not prime)
    is_prime[0] = is_prime[1] = False

    # iterate over all numbers up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # if i is prime, mark all multiples of i as composite (not prime)
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False

    # return a list of all prime numbers less than n
    return [i for i in range(n) if is_prime[i]]


# p = find_primes(1200000)
# print(p)

n = 10
m = n**0.5
print(m)
