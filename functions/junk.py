# # Count to 10
# #for i in range(1, 11):
#     #print(i)

# # Count to 10, step 2
# for i in range(1, 11, 2):
#     print(i)

# # function for finding max in a list
def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# # list of random integers
import random
lst = [random.randint(0, 99) for _ in range(20)]
# print(lst)
# print("Max value:", find_max(lst))



# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH



# def count_vowels(s):
#     return sum(1 for char in s.lower() if char in 'aeiou')
# print(count_vowels("Hello, World!"))  # Output: 3

# list 
l = [1, 2, 2, 3, 4, 4, 5]
# set
print(l)
s = {1, 2, 2, 3, 4, 4, 5}
print(s)

# python version
import sys
print(sys.version)

# def remove_duplicates(lst):
#     return list(set(lst))
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]


def main():
    print("This code is running directly.")
    print("Max value using custom find_max():", find_max(lst))

if __name__ == "__main__":
    print("This code is running directly.")
else:
    print("This code is being imported.")
    print("Max value using built-in max():", max(lst))