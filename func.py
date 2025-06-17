# Functions
def addition():
    a = 10
    b = 23
    c = a + b
    print(f"The sum of {a} and {b} is {c}")
    return c 

d = addition()
print(d)

def subtraction(a, b):
    c = a - b
    print(c) 
    return c

subtraction(20, 10) 
print(subtraction(50, 30)) 

def multiplication(a, b=2):
    c = a * b
    return c

print(multiplication(5))
