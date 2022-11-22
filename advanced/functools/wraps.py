from datetime import datetime
from functools import wraps, partial

def execution_time(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        '''A wrapper function'''
        start = datetime.utcnow()
        func(*args, **kwargs)
        print('Elapsed time: {}s'.format(datetime.utcnow() - start))

    return wrapped_func


@execution_time
def calc_power():
    '''Sum of power'''
    x = 0
    for i in range(1000):
        x = x = pow(1.5, i)

    print(f'x = {x}')


def algebra(x, y):
    return 2 * x + 6 * y


def main():
    solve = partial(algebra, x=2, y=3)
    print (solve)

if __name__ == '__main__':
    print(calc_power.__name__)
    print(calc_power.__doc__)
