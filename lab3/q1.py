Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Q1.  WAP to find a number is Prime or not."""
... number = int(input("Enter a number: "))
... 
... if number > 1:
...     is_prime = True
...     for i in range(2, int(number ** 0.5) + 1):
...         if number % i == 0:
...             is_prime = False
...             break  
...     if is_prime:
...         print(f"{number} is a prime number.")
...     else:
...         print(f"{number} is not a prime number.")
... else:
...     print(f"{number} is not a prime number.")
... #Output -
