import random

# populate array with loop
my_list = []  # Create an empty list
my_set = set()  # Create an empty set
my_tuple = ()
# print(type(my_list))


for i in range(10):  # Loop 10 times
    rnd = random.randint(1, 10)  # Generate a random number between 1 and 100
    my_list.append(rnd)  # Add the current number to the list
    my_set.add(rnd)  # Add the current number to the set

print(str(type(my_list)) + str(my_list))  # Output the full list
print(my_set)  # Output the full list

# breakpoint()

# my_array = [1, 2, 3, 4, 5]

for i in range(len(my_list)):
    print(str(i) + ": " + str(my_list[i]))
