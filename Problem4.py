# Input string
input_string = input("Enter a string: ")

# Specify the number of characters to remove
n = int(input("Enter the number of characters to remove: "))

# Use string slicing to remove the first n characters
result = input_string[n:]

# Print the result
print("String after removing the first", n, "characters:", result)