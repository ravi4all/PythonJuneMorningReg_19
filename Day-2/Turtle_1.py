import turtle
t = turtle.Pen()
t.shape("turtle")

'''
for i in range(1,4):
    t.forward(200)
    t.left(90)
'''

'''
for i in range(50):
    t.forward(2*i)
    t.left(90)
'''
t.speed(0)
for i in range(1,100,2):
    t.circle(5*i)
    t.left(90)
