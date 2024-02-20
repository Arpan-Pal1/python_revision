# write a function to calculate and return the square of a number
'''
def square(n):   # parameter
    return n**2

print(square(4)) #argument
'''

# Create a function that takes two numbers as parameters and returns their sum.
'''
def sum_of_two(n1, n2):
    return n1 + n2
print(sum_of_two(5,4))
'''


# polymorphism in function
'''
def multiply(i1, i2):
    return i1*i2

print(multiply(8,5))
print(multiply('a', 5))
print(multiply(5, 'x'))

'''

# Create a function that returns both the area and circumference of a circle given its radius
'''
import math

def circumference_area(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circumference_area(3)

print(f'{a:.2f} and other one is {c:.2f}')
'''

# default param
'''
import math

def circumference_area(radius=1):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circumference_area()

print(f'{a:.2f} and other one is {c:.2f}')
'''

# Create a lambda function to compute the cube of a number
'''
cube = lambda x : x**3
print(cube(2))
'''

# Write a function that takes variable number of arguments and returns their sum.
'''
def sum_of_multiple(*args):  #*args is a tuple
    return sum(args)

print(sum_of_multiple(1,2,3))
print(sum_of_multiple(1,2,3,700,54,8))
'''

# **kwargs
'''
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_kwargs(name='arpan', title ='pal')
'''

# Write a generator function that yields even numbers up to a specified limit
'''
def even(n):
    for i in range(1,n+1):
        if i%2 == 0:
            yield i

for i in even(10):
    print(i)
'''

# factorial of a number in recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)