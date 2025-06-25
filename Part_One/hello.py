# First Python program

# Comments, Print statements, Variables

# This is a comment

# Print statements
print('Hello World!')
msg = 'This is a boy' + ' and this is a girl'
print(msg)

# Variables
c = 'Maria'
print(c)

a = 10
b = 10
if a == b:
    print('This is true') 
else:
    print('a and b are not equal')

# Variables with different data types
air = 'Sstarr'                          # String
bar = 1                                  # Integer
car = 1.5                                # Float
dot = True                               # Boolean
ear = [1, 2, 3, 4, 5]                   # List
far = 5 + 6j                      # Complex number

print(type(dot))

f = str(bar)
print(type(f))                     # Type conversion


# More on Strings

# Multiline String
'''This is a multiline string
It can span multiple lines
This is useful for long text blocks
'''

# String Concatenation
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)

msgg = first_name + ' [' + last_name + '] is a good person'
print(msgg)

name = ['John', 'Doe']
word = ' '.join(name)
print(word)

# String Formatting (f-string)
age = 30
fstring = f'My name is {full_name} and I am {age} years old.'
print(fstring)

# String Indexing
t = 'Elizabeth'
print(t[4])
print(t[:5])  # String slicing

m = t[5:9]
print(m)  # Slicing from index 5 to 8

print(len(t))  # Length of the string

# String Methods
k = ' Hello World'
print(k)
print(k.strip())  # Removing leading and trailing spaces
print(k.lower())  # Converting to lowercase
print(k.upper())  # Converting to uppercase
print(k.replace('Hello', 'Hi'))  # Replacing a substring

hum = ' Gold,Pete,Joanna,Chris,Stella '
print(hum.strip())  # Stripping spaces from both ends
r = hum.split(',')  # Splitting a string into a list
print(r)

fur = 'waterskating'
if 'skat' in fur:
    print('skat is in waterskating')
