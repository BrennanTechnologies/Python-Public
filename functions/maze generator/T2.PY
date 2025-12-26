# For example, if the input string is "Hello, World!", the function should return "Hll, Wrld!"

vowels = ['a', 'e', 'i', 'o', 'u']
string = "Hello, World!"
new_string = ""
for x in string:
    if x not in vowels:
        new_string += x
print(new_string)
