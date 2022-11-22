from datetime import datetime
from functools import singledispatch

def execution_time(func):
    def wrapped_func(*args, **kwargs):
        start = datetime.utcnow()
        func(*args, **kwargs)
        print('Elapsed time: {}s'.format(datetime.utcnow() - start))

    return wrapped_func


@execution_time
def calc_power():
    x = 0
    for i in range(1000):
        x = x = pow(1.5, i)

    print(f'x = {x}')


if __name__ == '__main__':
    calc_power()
