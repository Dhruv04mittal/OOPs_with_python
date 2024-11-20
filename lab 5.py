Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 1. Write a Python program to triple all numbers in a given list of integers. Use Python map.

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
tripled_numbers = list(map(lambda x: x * 3, numbers))
print("Tripled numbers:", tripled_numbers)


# 2. Write a Python program to add three given lists using Python map and lambda.

list1 = list(map(int, input("Enter first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter second list of numbers separated by space: ").split()))
list3 = list(map(int, input("Enter third list of numbers separated by space: ").split()))
sum_lists = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print("Sum of lists:", sum_lists)


# 3. Write a Python program to listify the list of given strings individually using Python map.

strings = input("Enter a list of strings separated by space: ").split()
listified_strings = list(map(list, strings))
print("Listified strings:", listified_strings)


# 4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.

numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
powers = list(map(lambda x, idx: x ** (idx + 1), numbers, range(len(numbers))))
print("Powers based on index:", powers)


# 5. Write a Python program to square the elements of a list using the map() function.

numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)


# 6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.

sequence = input("Enter a sequence of characters: ")
upper_case = list(map(lambda x: x.upper(), set(sequence)))
lower_case = list(map(lambda x: x.lower(), set(sequence)))
print("Uppercase unique letters:", upper_case)
print("Lowercase unique letters:", lower_case)


# 7. Write a Python program to add two given lists and find the difference between them. Use the map() function.

list1 = list(map(int, input("Enter first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter second list of numbers separated by space: ").split()))
added_lists = list(map(lambda x, y: x + y, list1, list2))
difference_lists = list(map(lambda x, y: x - y, list1, list2))
print("Added lists:", added_lists)
print("Difference of lists:", difference_lists)


# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

int_list = list(map(int, input("Enter a list of integers separated by space: ").split()))
... int_tuple = tuple(map(int, input("Enter a tuple of integers separated by space: ").split()))
... converted_list = list(map(str, int_list))
... converted_tuple = list(map(str, int_tuple))
... print("Converted list:", converted_list)
... print("Converted tuple:", converted_tuple)
... 
... 
... # 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
... 
... tuple_data = tuple(map(int, input("Enter a tuple of integers separated by space: ").split()))
... new_list = list(map(lambda x: x * 2 if x % 2 == 0 else str(x), tuple_data))
... print("New list after processing:", new_list)
... 
... 
... # 10. Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.
... 
... def fibonacci(n):
...     fib = [0, 1]
...     while len(fib) < n:
...         fib.append(fib[-1] + fib[-2])
...     return fib
... 
... N = int(input("Enter the number of Fibonacci numbers to square: "))
... fib_numbers = fibonacci(N)
... squared_fib = list(map(lambda x: x ** 2, fib_numbers))
... print(f"Squared Fibonacci numbers (first {N}):", squared_fib)
... 
... 
... # 11. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.
... 
... array = list(map(int, input("Enter a list of integers separated by space: ").split()))
... sum_elements = sum(map(int, array))
... print("Sum of elements:", sum_elements)
