Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Q2. WAP to find the given number is palindrome or not."""
... number = input("Enter a number: ")
... 
... reversed_number = number[::-1]
... 
... if number == reversed_number:
...     print(f"{number} is a palindrome.")
... else:
...     print(f"{number} is not a palindrome.")
... """Output-
... Enter a number: 121
