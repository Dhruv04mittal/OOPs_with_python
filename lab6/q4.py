Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Wapp for solving tower of Hanoi problem for n = 3 disk"""
... def tower_of_hanoi(n, source, target, auxiliary):
...     if n == 1:
...         print(f"Move disk 1 from {source} to {target}")
...         return
...     tower_of_hanoi(n - 1, source, auxiliary, target)
...     print(f"Move disk {n} from {source} to {target}")
...     tower_of_hanoi(n - 1, auxiliary, target, source)
... 
