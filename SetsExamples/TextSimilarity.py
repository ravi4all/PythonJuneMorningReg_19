text_1 = """Python Programming Language is a high-level and interpreted programming language which was created by Guido Van Rossum in 1989. It was first released in 1991, which results in a great general purpose language capable of creating anything from desktop software to web applications and frameworks.
For those of you familiar with Java or C++, Python will break the mold you have built for a typical programming language. Prepare to fall in love, with Python. Python is a high-level dynamic programming language. It is quite easy to learn and provides powerful typing. Python code has a very ‘natural’ style to it, in that it is easy to read and understand (thanks to the lack of semicolons and braces). Python programming language runs on any platform, ranging from Windows to Linux to Macintosh, Solaris etc."""

text_2 = """Python is a powerful programming language ideal for scripting and rapid application development. It is used in web development (like: Django and Bottle), scientific and mathematical computing (Orange, SymPy, NumPy) to desktop graphical user Interfaces (Pygame, Panda3D).
This tutorial introduces you to the basic concepts and features of Python 3. After reading the tutorial, you will be able to read and write basic Python programs, and explore Python in depth on your own.
This tutorial is intended for people who have knowledge of other programming languages and want to get started with Python quickly."""

# 1. Remove Stopwords
text_1 = text_1.replace(',','')
text_1 = text_1.replace('.','')
text_1 = text_1.replace('(','')
text_1 = text_1.replace(')','')
token_1 = text_1.lower().split()

text_2 = text_2.replace(',','')
text_2 = text_2.replace('.','')
text_2 = text_2.replace('(','')
text_2 = text_2.replace(')','')
token_2 = text_2.lower().split()

# print(token_1)

# 2. Remove Stopwords
stopwords = ['is','am','are','the','that','those','be','if','of','at','on','for','and','am',
             'this','to','have','has','had','with','by','those','who','will','or','a','any',
             'from','was','in','it','you','which']

words_1 = []
for word in token_1:
    if word not  in stopwords:
        words_1.append(word)

words_2 = []
for word in token_2:
    if word not  in stopwords:
        words_2.append(word)

# print(words_1)
# print(words_2)
x = ['ing','ed','s']
for i in range(len(x)):
    for j in range(len(words_1)):
        if words_1[j].endswith(x[i]):
            words_1[j] = words_1[j].replace(x[i],'')
for i in range(len(x)):
    for j in range(len(words_2)):
        if words_2[j].endswith(x[i]):
            words_2[j] = words_2[j].replace(x[i],'')

intersection = set(words_1).intersection(set(words_2))
union = set(words_1).union(set(words_2))

j = len(intersection) / len(union)
print("Similarity is",j*100)
print("Similar words are",intersection)




