lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
#      indexes  0  1       2      3   4   5

# lucky_numbers[0] = 90  # tuples are immutable
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))

str = "Hello World"
str = str.replace("World", "Universe")
str = "Car"
print(str[0])


def add_numbers(num1, num2=99):
    return num1 + num2


sum = add_numbers(4)
print(sum)
