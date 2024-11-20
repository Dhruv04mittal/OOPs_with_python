Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Wapp to pass the list as an argument in the fn"""
... def process_list(input_list):
...     return [x * 2 for x in input_list]
... 
... my_list = [1, 2, 3, 4]
... result = process_list(my_list)
... print(result)
