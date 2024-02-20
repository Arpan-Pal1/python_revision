name = "Arpan"

def func():
    # name = "Eshita"
    print(name)

# print(name)
# func()


# x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(100)
# print(result)



# x = 99

# def func3():
#     global x   # giving global ref (don't use)
#     x = 88


# func3()
# print(x)



# x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2       # def + memory ref (bag) 

# my_result = f1()
# my_result()
# print(x)



# clouser / factory function

# def func(num):
#     def func2(x):
#         return x ** num
#     return func2


# f = func(2)
# g = func(3)



#practice

# global var
name = "Arpan"

def outerfunc(another_name):
    def innerfunc(title):
        return name + another_name + title
    return innerfunc

get_name = outerfunc(another_name="Eshita")
print(get_name('pal'))