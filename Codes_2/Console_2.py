Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 2,3,4,5,2,67,43,44
>>> type(x)
<class 'tuple'>
>>> x[0] = 10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name, sal, dept = 'Ram', 23000, 'IT'
>>> data
('Ram', 23000, 'IT')
>>> name
'Ram'
>>> sal
23000
>>> dept
'IT'
>>> d = {'name':'Ram','age':30,'sal':34000,'dept':'IT'}
>>> d
{'name': 'Ram', 'age': 30, 'sal': 34000, 'dept': 'IT'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonMorningRegular/Codes_2/Dictionary.py 
>>> data
[{'name': 'Ram', 'age': 30, 'sal': 34000, 'dept': 'IT'}, {'name': 'Shyam', 'age': 34, 'sal': 23000, 'dept': 'IT'}, {'name': 'Aman', 'age': 29, 'sal': 37000, 'dept': 'HR'}, {'name': 'Gopal', 'age': 26, 'sal': 20000, 'dept': 'HR'}, {'name': 'Mohit', 'age': 38, 'sal': 40000, 'dept': 'Sales'}, {'name': 'Sumit', 'age': 31, 'sal': 37000, 'dept': 'Sales'}]
>>> data[0]
{'name': 'Ram', 'age': 30, 'sal': 34000, 'dept': 'IT'}
>>> d
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d = {'name':'Ram','age':30,'sal':34000,'dept':'IT'}
>>> d
{'name': 'Ram', 'age': 30, 'sal': 34000, 'dept': 'IT'}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Ram'
>>> d['age']
30
>>> d['sal']
34000
>>> d['dept']
'IT'
>>> d.keys()
dict_keys(['name', 'age', 'sal', 'dept'])
>>> d.values()
dict_values(['Ram', 30, 34000, 'IT'])
>>> d.items()
dict_items([('name', 'Ram'), ('age', 30), ('sal', 34000), ('dept', 'IT')])
>>> d['address'] = 'Delhi'
>>> d
{'name': 'Ram', 'age': 30, 'sal': 34000, 'dept': 'IT', 'address': 'Delhi'}
>>> for item in d:
	print(item)

	
name
age
sal
dept
address
>>> for item in d.values():
	print(item)

	
Ram
30
34000
IT
Delhi
>>> for item in d.items():
	print(item)

	
('name', 'Ram')
('age', 30)
('sal', 34000)
('dept', 'IT')
('address', 'Delhi')
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonMorningRegular/Codes_2/Dictionary.py 
Shyam 34 IT
Mohit 38 Sales
Sumit 31 Sales
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonMorningRegular/Codes_2/Dictionary.py 
Shyam 34 IT
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonMorningRegular/Codes_2/Dictionary.py 
Ram 30 IT
Shyam 34 IT
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonMorningRegular/Codes_2/Dictionary.py 
Rohit 100 102.2
Dhawan 90 110.4
Kohli 120 150.0
Dhoni 76 100.7
>>> data
{'names': ['Rohit', 'Dhawan', 'Kohli', 'Jadhav', 'Dhoni', 'Jadeja'], 'scores': [100, 90, 120, 56, 76, 34], 'strike_rate': [102.2, 110.4, 150.0, 98.6, 100.7, 87]}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["names"]
['Rohit', 'Dhawan', 'Kohli', 'Jadhav', 'Dhoni', 'Jadeja']
>>> data["scores"]
[100, 90, 120, 56, 76, 34]
>>> data["scores"] > 70
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data["scores"] > 70
TypeError: '>' not supported between instances of 'list' and 'int'
>>> data["scores"][0] > 70
True
>>> data["scores"][1] > 70
True
>>> import pandas as pd
>>> pd.DataFrame(data)
    names  scores  strike_rate
0   Rohit     100        102.2
1  Dhawan      90        110.4
2   Kohli     120        150.0
3  Jadhav      56         98.6
4   Dhoni      76        100.7
5  Jadeja      34         87.0
>>> df = pd.DataFrame(data)
>>> import matplotlib.pyplot as plt
>>> plt.bar(names,scores)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    plt.bar(names,scores)
NameError: name 'names' is not defined
>>> plt.bar(df['names'],df['scores'])
<BarContainer object of 6 artists>
>>> plt.show()
>>> plt.bar(df['names'],df['scores'], c=['r''g','b','c','o','v'])
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    plt.bar(df['names'],df['scores'], c=['r''g','b','c','o','v'])
  File "C:\Python37\lib\site-packages\matplotlib\pyplot.py", line 2459, in bar
    **({"data": data} if data is not None else {}), **kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\axes\_axes.py", line 2298, in bar
    r.update(kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\artist.py", line 916, in update
    ret = [_update_property(self, k, v) for k, v in props.items()]
  File "C:\Python37\lib\site-packages\matplotlib\artist.py", line 916, in <listcomp>
    ret = [_update_property(self, k, v) for k, v in props.items()]
  File "C:\Python37\lib\site-packages\matplotlib\artist.py", line 912, in _update_property
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property c
>>> plt.bar(df['names'],df['scores'], color=['r''g','b','c','o','v'])
Traceback (most recent call last):
  File "C:\Python37\lib\site-packages\matplotlib\colors.py", line 174, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('rg', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    plt.bar(df['names'],df['scores'], color=['r''g','b','c','o','v'])
  File "C:\Python37\lib\site-packages\matplotlib\pyplot.py", line 2459, in bar
    **({"data": data} if data is not None else {}), **kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\axes\_axes.py", line 2262, in bar
    color = itertools.chain(itertools.cycle(mcolors.to_rgba_array(color)),
  File "C:\Python37\lib\site-packages\matplotlib\colors.py", line 275, in to_rgba_array
    result[i] = to_rgba(cc, alpha)
  File "C:\Python37\lib\site-packages\matplotlib\colors.py", line 176, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "C:\Python37\lib\site-packages\matplotlib\colors.py", line 220, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'rg'
>>> plt.bar(df['names'],df['scores'], color=red)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    plt.bar(df['names'],df['scores'], color=red)
NameError: name 'red' is not defined
>>> plt.bar(df['names'],df['scores'], color='r')
<BarContainer object of 6 artists>
>>> plt.show()
>>> 
