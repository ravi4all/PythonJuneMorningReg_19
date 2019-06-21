Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello this is python programming"
>>> text.split()
['hello', 'this', 'is', 'python', 'programming']
>>> import re
>>> text = "hello this is python programming. Ram loves to study Python and Ram Scored 95 marks"
>>> re.findall('[a-z]\w+', text)
['hello', 'this', 'is', 'python', 'programming', 'am', 'loves', 'to', 'study', 'ython', 'and', 'am', 'cored', 'marks']
>>> re.findall('[A-Z]\w+', text)
['Ram', 'Python', 'Ram', 'Scored']
>>> re.findall('[a-z | 0-9]\w+', text)
['hello', ' this', ' is', ' python', ' programming', ' Ram', ' loves', ' to', ' study', ' Python', ' and', ' Ram', ' Scored', ' 95', ' marks']
>>> re.findall('[a-z | 0-9]', text)
['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'a', 'm', ' ', 'l', 'o', 'v', 'e', 's', ' ', 't', 'o', ' ', 's', 't', 'u', 'd', 'y', ' ', 'y', 't', 'h', 'o', 'n', ' ', 'a', 'n', 'd', ' ', 'a', 'm', ' ', 'c', 'o', 'r', 'e', 'd', ' ', '9', '5', ' ', 'm', 'a', 'r', 'k', 's']
>>> re.findall('[A-Z | 0-9]\w+', text)
[' this', ' is', ' python', ' programming', ' Ram', ' loves', ' to', ' study', ' Python', ' and', ' Ram', ' Scored', ' 95', ' marks']
>>> re.findall('[A-Z|0-9]\w+', text)
['Ram', 'Python', 'Ram', 'Scored', '95']
>>> text.endswith("ing")
False
>>> text
'hello this is python programming. Ram loves to study Python and Ram Scored 95 marks'
>>> 
