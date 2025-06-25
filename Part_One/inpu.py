name = input('What is your name?: ')
color = input('What is your favorite color?: ')
print(f'{name} likes {color}!')

birth_year = input('What year were you born?: ')
current_year = input('Enter current year: ')
age = int(current_year) - int(birth_year)
print(f'{name} is {age} years old.')

print(type(name))
print(type(age))

weight_lbs = int(input('Enter your weight in pounds: '))
weight_kg = weight_lbs * 0.45
print(f'Your weight in kg is {weight_kg:.2f} kg.')

