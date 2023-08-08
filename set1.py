
print("Hello, World!")

# Data types and basic operations
num1 = 10
num2 = 5
result = num1 + num2
print("Result:", result)

# List creation and operations
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.remove(3)
print("List:", my_list)

# Sum and average of a list
sum_list = sum(my_list)
avg = sum_list / len(my_list)
print("Sum:", sum_list)
print("Average:", avg)

# String reversal
my_string = "Hello, World!"
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)

# Counting occurrences of a value in a list
value_to_count = 2
count = my_list.count(value_to_count)
print("Count of", value_to_count, ":", count)

# Printing numbers in a range
for i in range(1, 11):
    print(i, end=" ")
print()  # Print a newline

# Factorial calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num_for_factorial = 5
print("Factorial of", num_for_factorial, ":", factorial(num_for_factorial))

# Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

fibonacci_length = 10
print("Fibonacci sequence:", fibonacci(fibonacci_length))

# List comprehension: Creating a list of numbers from 1 to 100
numbers_1_to_100 = [x for x in range(1, 101)]
print("List comprehension:", numbers_1_to_100)
