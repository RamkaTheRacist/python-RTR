# def func(x):
#     x**2

# g = func
# print(g(1))


# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))
# math(calc2, 10)

# def sum(x, y):
#     return x + y

# f = sum

# sum = lambda x, y: x + y

# def mult(x, y):
#     return x*y

# def math(op, x, y):
#     print(op(x,y))

# math(sum, 2, 5)



def mult(x, y):
    return x*y

def math(op, x, y):
    print(op(x,y))

math(lambda x, y: x + y, 2, 5)