my_list = [1, 2, 3]
list_iterator = iter(my_list)
next(list_iterator)

for item in my_list:
    print(item)

def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number

import itertools
t1=(1, 3, 6)
t2=[4, 1, 4]
t=itertools.chain(t1, t2)
print(next(t1))