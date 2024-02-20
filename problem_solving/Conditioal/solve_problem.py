# Age group Categorization (Chai-aur-backend)

'''age = int(input('Enter your age '))

if age < 13:
    print('Child')
elif age >= 13 and age <= 19:
    print('Teenager')
elif age >= 20 and age <= 59:
    print('Adult')
else:
    print('Senior')

'''

# Movie ticket pricing
'''
import datetime

today = datetime.date.today()

# print(today.weekday())

age = int(input('Enter your age '))

if today.weekday() == 2 : 
    if age >= 18:
        print(f'You are adult so you have to pay $12 - $2 : ${12 - 2}')
    else:
        print(f'You are children so you have to pay $8 - $2 : ${8 - 2} only')
else: 
    if age >= 18:
        print(f'You are adult so you have to pay $12')
    else:
        print(f'You are children so you have to pay $8')

'''

# Grade Calculator
'''
grade = int(input('Enter your grade '))

if grade in range(90, 101):
    print('A')
if grade in range(80, 90):
    print('B')
if grade in range(70, 80):
    print('C')
if grade in range(60, 70):
    print('D')
if grade in range(0, 60):
    print('F')
else:
    print('Invalid input')

'''

# Fruit Ripeness Checker
'''
fruit = {
    'green' : 'Unripe',
    'yellow' : 'Ripe',
    'brown' : 'Overripe'
}

input_fruit = input('Enter your fruit name ')
color = input('Enter its color(green, yellow, brown) ').lower()


if color not in fruit.keys():
    print('invalid color')
else:
    print(f'Your fruit {input_fruit} is {fruit[color]}')

'''

# Weather activity suggestion

'''
weather_suggestion = {
    'sunny' : 'Go for walk',
    'rainy' : 'Read Book',
    'Snowy' : 'Build a snowman'
}

weather_input = input('Enter your weather condition ').lower()

if weather_input in weather_suggestion.keys():
    print(f'{weather_suggestion[weather_input]}')
else:
    print('invalid input')

'''

# Transportation Mode selection
'''
distance = int(input('Enter your distance '))

if distance < 3:
    print('Walk')
elif distance >= 3 and distance <= 15:
    print('Bike')
elif distance > 15:
    print('Car')
'''


# Coffee Customization

'''
coffee_size = input('Enter your coffee size ').lower()
extra_shot = True 

if coffee_size in ['small', 'medium', 'large']:
    if extra_shot:
        print(f'{coffee_size}  with Extra shot')
    else:
        print(coffee_size)
else:
    print('invalid')

'''

# Password Strength Checker
'''
password = input('enter your password ')
password_length = len(password)

if password_length < 6:
    print('Weak')
elif password_length in range(6,11):
    print('Medium')
elif password_length > 10:
    print('Strong')
'''

# Leap year checker
'''
year = int(input('enter year'))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('Leap year')
else:
    print('Not leap year')

'''

# Pet Recommaenadation

'''
pet = input('enter animal ')
age = int(input('Enter age '))

if age in range(0, 3):
    print(f'{pet} junior food')
else:
    print(f'Senior {pet} food')
'''