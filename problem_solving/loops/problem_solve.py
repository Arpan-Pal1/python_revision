# count positive number
'''
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0

for item in numbers:
    if item > 0 :
        count += 1

print(count)
'''

# Sum of even number

'''
n = int(input('enter the range'))

sum = 0

for i in range(n+1):
    if i % 2 == 0:
        sum += i

print(sum)

'''

# multiplication table but skip the 5th one
'''
num = int(input('Enter any number '))

for i in range(1,11):
    if i == 5:
        continue
    print(f'{num} * {i} = {num*i}')
    
'''

# Reverse a string
'''
str = input('Enter any string ')

new_str = str[::-1]
print(new_str)
'''

# Find First non-repeated charcter
'''
input_str = "teeteracdacd"

for l in input_str:
    if input_str.count(l) == 1:
        print('repeat ', l)
        break
'''

# Factorial calculator
'''
n = int(input('Enter a number '))

mul = 1
for i in range(1, n+1):
    mul *= i

print(mul)
'''


# Validate input
'''
validation = True 
while validation:
    value = int(input('Please enter a number between 1-10 '))
    if value in range(1,11):
        validation = False
        break
'''

# prime number checker
'''
n = int(input('Enter a number '))

flag = False

for i in range(2, n//2+1):
    if n%i == 0:
        flag = True
        break
if flag:
    print('not prime')
else:
    print('prime')

'''

# List uniqueness checker
'''
items = ["apple", "banana", "orange",  "apple", "mango"]

flag = True

for i in items:
    if items.count(i) > 1:
        flag = False
        break
if flag:
    print('unique')
else:
    print('not unique')
'''

