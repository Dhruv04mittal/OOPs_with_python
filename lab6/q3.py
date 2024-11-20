Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Wapp to take variable length arguments in fn and perform cube of each elements """
... def cube_elements(*args):
...     return [x ** 3 for x in args]
... 
... result = cube_elements(1, 2, 3, 4)
... print(result)
