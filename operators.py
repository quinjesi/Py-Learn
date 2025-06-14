# Operators in Python

# Arithmetic Operators
a = 2 + 3  # Addition
b = 5 - 2  # Subtraction
c = 4 * 3  # Multiplication
d = 10 / 2  # Division
e = 10 % 3  # Modulus
f = 2 ** 3  # Exponentiation
g = 10 // 3  # Floor Division

print(a, b, c, d, e, f, g)

# Assignment Operators
x = 5
y = 10
z = 15

x += 2  # Equivalent to x = x + 2
y -= 5  # Equivalent to y = y - 5
z *= 3  # Equivalent to z = z * 3
z /= 2  # Equivalent to z = z / 2
print(x, y, z)

# Comparison Operators
r = 5
s = 10
if r == s:
    print("True")
elif r > s:
    print("r is greater than s")
elif r < s:
    print("r is less than s")
elif r != s:
    print("r is not equal to s")

# Logical Operators
a = True
b = False
if a and b:
    print("Both are True")
elif a or b:
    print("At least one is True")
else:
    print("Both are False")

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True, same object
print(x is not z)  # True, different objects

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True, 3 is in the list
print(6 not in my_list)  # True, 6 is not in the list