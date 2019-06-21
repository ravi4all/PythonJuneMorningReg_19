Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2019\June\PythonMorningRegular\SetsExamples\TextSimilarity.py 
>>> words_2
['python', 'powerful', 'programming', 'language', 'ideal', 'scripting', 'rapid', 'application', 'development', 'used', 'web', 'development', 'like:', 'django', 'bottle', 'scientific', 'mathematical', 'computing', 'orange', 'sympy', 'numpy', 'desktop', 'graphical', 'user', 'interfaces', 'pygame', 'panda3d', 'tutorial', 'introduces', 'basic', 'concepts', 'features', 'python', '3', 'after', 'reading', 'tutorial', 'able', 'read', 'write', 'basic', 'python', 'programs', 'explore', 'python', 'depth', 'your', 'own', 'tutorial', 'intended', 'people', 'knowledge', 'other', 'programming', 'languages', 'want', 'get', 'started', 'python', 'quickly']
>>> for i in range(len(words_2)):
	if words_2[i].endswith('ing'):
		print(words_2[i])

		
programming
scripting
computing
reading
programming
>>> for i in range(len(words_2)):
	if words_2[i].endswith('ing'):
		words_2[i] = words_2[i].replace('ing','')

		
>>> for i in range(len(words_2)):
	if words_2[i].endswith('ing'):
		print(words_2[i])

		
>>> words_2
['python', 'powerful', 'programm', 'language', 'ideal', 'script', 'rapid', 'application', 'development', 'used', 'web', 'development', 'like:', 'django', 'bottle', 'scientific', 'mathematical', 'comput', 'orange', 'sympy', 'numpy', 'desktop', 'graphical', 'user', 'interfaces', 'pygame', 'panda3d', 'tutorial', 'introduces', 'basic', 'concepts', 'features', 'python', '3', 'after', 'read', 'tutorial', 'able', 'read', 'write', 'basic', 'python', 'programs', 'explore', 'python', 'depth', 'your', 'own', 'tutorial', 'intended', 'people', 'knowledge', 'other', 'programm', 'languages', 'want', 'get', 'started', 'python', 'quickly']
>>> for word in words_2:
	print(re.search('(ing|ed)', word))

	
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    print(re.search('(ing|ed)', word))
NameError: name 're' is not defined
>>> import re
>>> for word in words_2:
	print(re.search('(ing|ed)', word))

	
None
None
None
None
None
None
None
None
None
<re.Match object; span=(2, 4), match='ed'>
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
<re.Match object; span=(6, 8), match='ed'>
None
<re.Match object; span=(5, 7), match='ed'>
None
None
None
None
None
<re.Match object; span=(5, 7), match='ed'>
None
None
>>> for word in words_2:
	if re.search('(ing|ed)', word):
		print(word)

		
used
intended
knowledge
started
>>> for word in words_2:
	if re.search('(ing|ed|s)$', word):
		print(word)

		
used
interfaces
introduces
concepts
features
programs
intended
languages
started
>>> 
