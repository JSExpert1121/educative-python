from time import sleep

def linear_search(data: list, target):
    for item in data:
        if item == target:
            return True

    return False


def binary_search_iterative(data: list, target):
    start = 0
    end = len(data) - 1

    while start <= end:
        middle = (start + end) // 2
        if data[middle] == target:
            return True

        if data[middle] > target:
            end = middle - 1
        else:
            start = middle + 1

    return False


def binary_search_recursive(data: list, target, start, end):
    if start > end:
        return False

    middle = (start + end) // 2
    if data[middle] == target:
        return True
    if data[middle] > target:
        return binary_search_recursive(data, target, start, middle - 1)
    else:
        return binary_search_recursive(data, target, middle + 1, end)


def binary_search_closest_number(data: list, target: int):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]

    start = 0
    end = len(data) - 1

    min_diff = min_left_diff = min_right_diff = float('inf')
    result = None
    while start <= end:
        middle = (start + end) // 2
        current = data[middle]
        if middle < (len(data) - 1):
            min_right_diff = abs(data[middle+1] - target)
        if middle > 0:
            min_left_diff = abs(data[middle-1] - target)

        if min_right_diff < min_diff:
            result = data[middle+1]
            min_diff = min_right_diff
        if min_left_diff < min_diff:
            result = data[middle-1]
            min_diff = min_left_diff

        if current > target:
            end = middle - 1
        elif current < target:
            start = middle + 1
        else:
            return current

    return result


def bs_fixed_point(data: list):
    if len(data) == 0:
        return None

    start = 0
    end = len(data) - 1

    while start <= end:
        middle = (start + end) // 2
        mid_value = data[middle]

        if mid_value > middle:
            end = middle - 1
        elif mid_value < middle:
            start = middle + 1
        else:
            return mid_value


def bs_find_peak_in_bitonic(data: list):
    if len(data) == 0:
        return None

    start = 0
    end = len(data) - 1

    while start <= end:
        middle = (start + end) // 2
        if middle == end:
            return data[middle]
        else:
            if data[middle] > data[middle+1]:
                end = middle
            else:
                start = middle + 1

    return data[start]
