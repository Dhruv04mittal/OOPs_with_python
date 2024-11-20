Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Wapp that accept string and calculate the number of uppercase and lowercase letters in the string """
... def count_case(string):
...     upper_count = sum(1 for c in string if c.isupper())
...     lower_count = sum(1 for c in string if c.islower())
...     print(f"Uppercase : {upper_count} , lowercase : {lower_count}")
...     return upper_count, lower_count
...     
...     
... 
... result = count_case("Hello World!")
... print(result)
