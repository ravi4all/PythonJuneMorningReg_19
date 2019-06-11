Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> print("hell world")
hell world
>>> name = 'Ram'
>>> print("Hello",name)
Hello Ram
>>> print
<built-in function print>
>>> a = True
>>> type(a)
<class 'bool'>
>>> True = False
SyntaxError: can't assign to keyword
>>> is = "hello"
SyntaxError: invalid syntax
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
35
>>> 
