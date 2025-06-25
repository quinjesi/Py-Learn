print('Welcome to the Weight Converter!\nThis program converts weight between kilograms and pounds.')

weight = int(input('Enter weight: '))
unit = input('Enter unit (kg/lbs): ').lower()
if unit == 'kg':
    converted = weight / 0.45
    print(f'Your weight in pounds is {converted:.2f} lbs.')
elif unit == 'lbs':
    converted = weight * 0.45
    print(f'Your weight in kg is {converted:.2f} kg.')
else:
    print('Invalid unit. Please enter either "kg" or "lbs".')
