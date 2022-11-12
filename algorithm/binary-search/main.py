from bisect import bisect_left, bisect_right, insort_left, insort_right
from binary_search import (
    linear_search,
    binary_search_iterative,
    binary_search_recursive,
    binary_search_closest_number,
    bs_fixed_point,
    bs_find_peak_in_bitonic
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

def run_bitonic_peak():
    print(bs_find_peak_in_bitonic([1, 2, 3, 4, 5, 4, 3, 2, 1]))
    print(bs_find_peak_in_bitonic([1, 6, 5, 4, 3, 2, 1]))
    print(bs_find_peak_in_bitonic([1, 2, 3, 4, 5]))
    print(bs_find_peak_in_bitonic([5, 4, 3, 2, 1]))

def run_bisect():
    print(bisect_left([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 2))
    print(bisect_right([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285))

    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    insort_left(A, 108)
    print(A)
    insort_right(A, 108)
    print(A)


if __name__ == '__main__':
    # run_search()
    # run_closest()
    # run_fixed_point()
    # run_bitonic_peak()
    run_bisect()
