def decorator(funcion):
    def inner(*args, **kwargs):                 #именнованные и неименновые аргументы 
        print("any1")
        funcion(*args, **kwargs)
        print("any2")
    return inner

def decorator2(funcion):
    def inner(*args, **kwargs):
        print("any10")
        funcion(*args, **kwargs)
        print("any20")
    return inner


@decorator
@decorator2
def say(arg1, arg2):
    print("any3", arg1, arg2)


say("pfff", 32)