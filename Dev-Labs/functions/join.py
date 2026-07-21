# Using join() in Python 3 
listExample = ["do","re","mi","fa","so","la","ti"] 
print(listExample)  

str = "-".join(listExample)
#print(str)


# Joining elements of listExample by "-" 
#joinBy = "-"
#joinedString = joinBy.join(listExample)
#print(joinedString)

# Using join() function to join elements with empty/no separator.
print("".join(listExample))