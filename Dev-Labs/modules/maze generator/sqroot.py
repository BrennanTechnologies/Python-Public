
from tqdm import tqdm


def sqrt1(n):
    # set the initial guess to n/2
    guess = n / 2

    # iterate until the guess is accurate enough
    # while abs(guess**2 - n) > 0.0001:
    while abs(guess**2 - n) > 1e-120:
        # improve the guess using the Babylonian method
        guess = (guess + n / guess) / 2

    # return the final guess as the square root of n
    return guess


def sqrt2(x):
    if x < 0:
        return None  # square root of negative numbers is undefined

    if x == 0 or x == 1:
        return x  # square root of 0 or 1 is the number itself

    # set initial values for lower and upper bounds
    lower_bound = 1
    upper_bound = x

    # iterate until we find the square root within a certain tolerance
    while abs(upper_bound - lower_bound) > 1e-120:
        guess = (lower_bound + upper_bound) / 2
        if guess * guess > x:
            upper_bound = guess
        else:
            lower_bound = guess

    # return the final guess as the square root
    return lower_bound


def sqrt3(n):
    # set the initial guess to n/2
    guess = n / 2

    # set the total number of iterations and create a progress bar
    total_iterations = 100000000
    progress_bar = tqdm(total=total_iterations)

    # iterate until the guess is accurate enough
    for i in range(total_iterations):
        # improve the guess using the Babylonian method
        guess = (guess + n / guess) / 2

        # update the progress bar
        progress_bar.update(1)

    # close the progress bar and return the final guess as the square root of n
    progress_bar.close()
    return guess


n = 16
# a = sqrt1(n)
# b = sqrt2(n)
c = sqrt3(n)
# print(a)
# print(b)
print(c)
