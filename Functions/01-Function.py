# Global Variable

x = 10
y = 20
# print(x+y)
# Function declaration/definition
def add():
    # Local Scope
    global x
    x = 12
    y = 22
    z = x + y
    print(z)

# Function call
add()
z = x + y
print(z)