# Conditionals(if, elif, else)

a = 10
b = 5

if a > b:
    print("a is greater than b")
    if a < 20:
        print("a is less than 20")
    else:
        print("a is not less than 20")  
elif a == b:
    print("a is equal to b")
else:
    print("a is not greater than b")


# Loops 

# While loop
a = 20
while a <= 25:
    print(a)
    if a == 23:
        break 
    a += 1

# For loop
for i in range(1, 6):
    print(i)
    if i == 3:
        break

b = ('hello', 'world')
for x in b:
    print(x)

# For loop with a list
my_list = [10, 20, 30, 40, 50]
for x in my_list:
    print(x)

# For loop with a string
my_string = "hello"
for p in my_string:
    print(p)

# For loop with a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")