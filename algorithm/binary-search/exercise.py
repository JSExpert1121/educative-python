
def integer_square_root(k):
    start = 0
    end = k

    while start <= end:
        middle = (start + end) // 2
        square = middle * middle
        if square == k:
            return middle
        elif square > k:
            end = middle - 1
        else:
            start = middle + 1

    return end


def find(A):
    start = 0
    end = len(A) - 1

    while start < end:
        middle = (start + end) // 2

        if A[middle] > A[end]:
            start = middle + 1
        else:
            end = middle

    return start


if __name__ == '__main__':
    # print(integer_square_root(300))
    # print(integer_square_root(12))
    # print(integer_square_root(49))
    # print(integer_square_root(900000))
    print(find([4, 5, 6, 7, 1, 2, 3]))
    print(find([1, 2, 3, 4, 5, 6, 7]))
    print(find([2, 3, 4, 5, 6, 7, 1]))
    print(find([3, 4, 5, 6, 7, 1, 2]))
