

def func(a,b,c):
    return a * b * c

def func_1(a1):
    def func_2(a2):
        def func_3(a3):
            return func(a1, a2, a3)
        return func_3
    return func_2

def curry(func):
    def curried(*args):
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        else:
            return lambda x:curried(*(args + (x,)))
    return curried

if __name__ == "__main__":
    res = func(1,2,3)
    print(res)

    res_curry = func_1(1)(2)(3)
    print(res_curry)

    