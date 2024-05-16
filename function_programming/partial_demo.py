from functools import partial

def my_partial(wrapped_fn, *initial_args):
    def new_fn(*invoke_args):
        return wrapped_fn(*(initial_args + invoke_args))
    return new_fn

def func(x,y):
    return x * y

def sum_fuc(a,b,c):
    return a + b + c


if __name__ == "__main__":
    res = partial(func,2)(5)
    print(res)

    sum_res = my_partial(sum_fuc,2,3)(5)
    print(sum_res)