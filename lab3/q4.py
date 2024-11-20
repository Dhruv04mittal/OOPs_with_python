Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Q4. WAP to create a simple console base calculator"""
... print("Simple Calculator")
... print("Choose operation:")
... print("1. Addition")
... print("2. Subtraction")
... print("3. Multiplication")
... print("4. Division")
... 
... operation = input("Enter choice (1/2/3/4): ")
... 
... num1 = float(input("Enter first number: "))
... num2 = float(input("Enter second number: "))
... 
... if operation == '1':
...     result = num1 + num2
...     print(f"The result of addition is: {result}")
... elif operation == '2':
...     result = num1 - num2
...     print(f"The result of subtraction is: {result}")
... elif operation == '3':
...     result = num1 * num2
...     print(f"The result of multiplication is: {result}")
... elif operation == '4':
...     if num2 != 0:
...         result = num1 / num2
...         print(f"The result of division is: {result}")
...     else:
...         print("Error: Division by zero is not allowed.")
... else:
