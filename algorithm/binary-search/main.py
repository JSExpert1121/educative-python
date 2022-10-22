from binary_search import (
    linear_search,
    binary_search_iterative,
    binary_search_recursive,
    binary_search_closest_number,
    bs_fixed_point
)

def run_search():
    data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
    target = 29
    print(linear_search(data, target))
    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data) - 1))

def run_closest():
    data = [2, 5, 6, 7, 8, 8, 9]
    print(binary_search_closest_number(data, 4))

def run_fixed_point():
    data = [-10, -5, 0, 3, 7]
    print(bs_fixed_point(data))
    data = [0, 2, 5, 8, 17]
    print(bs_fixed_point(data))


if __name__ == '__main__':
    # run_search()
    # run_closest()
    run_fixed_point()
