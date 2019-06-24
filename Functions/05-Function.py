def calc(x,y):
    z = x + y
    # print(z)
    return z

# print(calc(4,5))
s = calc(4,5)
print(s)

def playerHealth():
    health = 56
    return health

def enemyHealth():
    health = 45
    return health

def game():
    ph = playerHealth()
    eh = enemyHealth()

    if ph < eh:
        print("Health Low")
    else:
        print("Keep it up")
game()