# This program demonstrates list comprehensions,
# dict comprehensions, and set comprehensions


# 1. Numbers divisible by 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divisible_by_3 = [num for num in numbers if num % 3 == 0]

print("Numbers divisible by 3:")
print(divisible_by_3)


# 2. Words longer than 4 characters in title case

words = ["python", "java", "apple", "sql", "engineer", "data"]

long_words = [word.title() for word in words if len(word) > 4]

print("\nWords longer than 4 characters:")
print(long_words)


# 3. Celsius to Fahrenheit conversion

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("\nFahrenheit temperatures:")
print(fahrenheit)


# 4. Flatten nested list

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

flat_list = [num for sublist in nested_list for num in sublist]

print("\nFlattened list:")
print(flat_list)


# Dict comprehension example

square_dict = {num: num * num for num in range(1, 6)}

print("\nDictionary comprehension:")
print(square_dict)


# Set comprehension example

even_set = {num for num in range(1, 11) if num % 2 == 0}

print("\nSet comprehension:")
print(even_set)