Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 1. Check if the given number is a Disarium Number
def is_disarium(num):
    num_str = str(num)
    total = sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str))
    return total == num

num = int(input("Enter a number to check if it's a Disarium Number: "))
if is_disarium(num):
    print(f"{num} is a Disarium Number.")
else:
    print(f"{num} is not a Disarium Number.")


# 2. Determine whether the given number is a Harshad Number
def is_harshad(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

num = int(input("Enter a number to check if it's a Harshad Number: "))
if is_harshad(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")


# 3. Print Armstrong Number from 1 to 1000
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == num

print("Armstrong Numbers from 1 to 1000:")
for i in range(1, 1001):
    if is_armstrong(i):
        print(i, end=" ")


# 4. Compute the value of X^n
def power(x, n):
    return x ** n

x = int(input("Enter the base value (x): "))
n = int(input("Enter the exponent value (n): "))
print(f"The value of {x}^{n} is {power(x, n)}")


# 5. Calculate the value of nCr
import math

def nCr(n, r):
    return math.comb(n, r)

n = int(input("Enter n (total items): "))
r = int(input("Enter r (selected items): "))
print(f"The value of {n}C{r} is {nCr(n, r)}")


# 6. Generate Fibonacci Series
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

n = int(input("Enter the number of Fibonacci terms: "))
print(f"The first {n} Fibonacci numbers are:")
for num in fibonacci(n):
    print(num, end=" ")
print()


# 7. Count the sum of digits in the entered number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = int(input("Enter a number to sum its digits: "))
print(f"The sum of digits in {num} is {sum_of_digits(num)}")


# 8. Find the reverse of a given number
def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter a number to reverse it: "))
print(f"The reverse of {num} is {reverse_number(num)}")


# 9. Check whether a given number is a Perfect Number
def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

num = int(input("Enter a number to check if it's a Perfect Number: "))
if is_perfect(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")


# 10. Check whether a given number is Palindrome or Not
def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number to check if it's a Palindrome: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")


# 11. Display the following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for x in range(1, i+1):
        print(x, end=" ")
    print()


# 12. Display the following pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1, 6):
    for x in range(i):
        print(i, end=" ")
    print()


# 13. Display the following pattern:
# A
# B B
# C C C
# D D D D
# E E E E E
for i in range(65, 70):
    for x in range(i - 64):
        print(chr(i), end=" ")
    print()


# 14. Display the following pattern:
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5, 0, -1):
    for x in range(i):
        print("*", end=" ")
    print()


# 15. Display the following pattern:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5, 0, -1):
    for x in range(1, i + 1):
        print(x, end=" ")
    print()


# 16. Display the following pattern:
# *
# * * *
# * * * * *
# * * * * * * *
# * * * * * * * * *
for i in range(1, 6):
    for x in range(2 * i - 1):
        print("*", end=" ")
    print()


# 17. Display the following pattern:
# 1
# 2 3 2
# 3 4 5 4 3
# 4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5
for i in range(1, 6):
    row = list(range(i, 2 * i))
    for num in row + row[::-1][1:]:
        print(num, end=" ")
    print()


# 18. Display the following pattern:
# * * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * *
# *
for i in range(9, 0, -2):
    for x in range(i):
        print("*", end=" ")
    print()


# 19. Display the following pattern (Pascal Triangle):
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
from math import comb
... for i in range(6):
...     for j in range(i + 1):
...         print(comb(i, j), end=" ")
...     print()
... 
... 
... # 20. Display the following pattern:
... # 1
... # 2 3
... # 4 5 6
... # 7 8 9 10
... num = 1
... for i in range(1, 5):
...     for x in range(num, num + i):
...         print(x, end=" ")
...     num += i
...     print()
... 
... 
... # 21. Display the following pattern:
... # A
... # B A B
... # A B A B A
... # B A B A B A B
... for i in range(1, 5):
...     for x in range(2 * i - 1):
...         print(chr(65 + (x % 2)), end=" ")
...     print()
... 
... 
... # 22. Display the following pattern:
... # 1
... # 0 1 0
... # 1 0 1 0 1
... # 0 1 0 1 0 1 0
... for i in range(1, 5):
...     for x in range(2 * i - 1):
...         print((i + x) % 2, end=" ")
...     print()
