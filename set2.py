# Display numbers using a loop
num_list = [12, 75, 150, 180, 145, 525, 50]
for num in num_list:
    print(num, end=" ")
print()  # Print a newline

# Append new strings in the middle of a string
str1 = "ault"
str2 = "kelly"
new_str = str1[:2] + str2 + str1[2:]
print("New string:", new_str)

# Arrange string "PyNaTive" with lowercase characters first
original_str = "PyNaTive"
lowercase_chars = ''.join([char for char in original_str if char.islower()])
uppercase_chars = ''.join([char for char in original_str if char.isupper()])
arranged_str = lowercase_chars + uppercase_chars
print("Arranged string:", arranged_str)

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)
