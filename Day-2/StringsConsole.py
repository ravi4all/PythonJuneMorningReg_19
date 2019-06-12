Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "this is python programming and python is used for machine learning"
>>> text[0]
't'
>>> text[0:4]
'this'
>>> text[6]
's'
>>> text[-1]
'g'
>>> text[0:15:2]
'ti spto '
>>> text[0:15:1]
'this is python '
>>> text[0:15:3]
'tssyo'
>>> len(text)
66
>>> text[0:]
'this is python programming and python is used for machine learning'
>>> text[0:68]
'this is python programming and python is used for machine learning'
>>> text[0:-1]
'this is python programming and python is used for machine learnin'
>>> text[0:6]
'this i'
>>> text[12:1]
''
>>> text[12:1:-1]
'ohtyp si si'
>>> text[12:0:-1]
'ohtyp si sih'
>>> text[12::-1]
'ohtyp si siht'
>>> text[12:1:-1]
'ohtyp si si'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gninrael '
>>> text[-10:-1]
'e learnin'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'this is python programming and python is used for machine learning'
>>> text.upper()
'THIS IS PYTHON PROGRAMMING AND PYTHON IS USED FOR MACHINE LEARNING'
>>> text.capitalize()
'This is python programming and python is used for machine learning'
>>> text.title()
'This Is Python Programming And Python Is Used For Machine Learning'
>>> text.split()
['this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> text.count('i')
6
>>> text.find('i')
2
>>> text.find('i',3)
5
>>> text.find('i',6)
23
>>> a = 'नमस्ते'
>>> type(a)
<class 'str'>
>>> a.encode()
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87'
>>> text.encode()
b'this is python programming and python is used for machine learning'
>>> text.endswith('g')
True
>>> text.index('x')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    text.index('x')
ValueError: substring not found
>>> text.find('this').endswith('s')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    text.find('this').endswith('s')
AttributeError: 'int' object has no attribute 'endswith'
>>> text.split([0].endswith('s'))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    text.split([0].endswith('s'))
AttributeError: 'list' object has no attribute 'endswith'
>>> text.split()[0].endswith('s')
True
>>> text.split()
['this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> text.split()[0]
'this'
>>> text.split()[0].endswith('s')
True
>>> text.startswith('t')
True
>>> text.isalpha()
False
>>> x = "hello"
>>> x.isalpha()
True
>>> text.center(50)
'this is python programming and python is used for machine learning'
>>> text.center(60)
'this is python programming and python is used for machine learning'
>>> text.center(70)
'  this is python programming and python is used for machine learning  '
>>> text.center(67)
' this is python programming and python is used for machine learning'
>>> text.center(68)
' this is python programming and python is used for machine learning '
>>> text.center(100)
'                 this is python programming and python is used for machine learning                 '
>>> text.center(100,'*')
'*****************this is python programming and python is used for machine learning*****************'
>>> x = text.center(100,'*')
>>> x
'*****************this is python programming and python is used for machine learning*****************'
>>> x.strip()
'*****************this is python programming and python is used for machine learning*****************'
>>> x.strip('*')
'this is python programming and python is used for machine learning'
>>> x.replace('python','java')
'*****************this is java programming and java is used for machine learning*****************'
>>> x
'*****************this is python programming and python is used for machine learning*****************'
>>> x.replace('python','java')
'*****************this is java programming and java is used for machine learning*****************'
>>> _
'*****************this is java programming and java is used for machine learning*****************'
>>> 12 + 5
17
>>> _
17
>>> _ = "hello"
>>> _
'hello'
>>> 12 + 5
17
>>> _
'hello'
>>> 
