file = open('test.txt', 'w')


try:
    file.write('hello arpan')
finally:
    file.close()

with open('test.txt', 'w') as file:
    file.write('hello arpan')