from collections import Counter

def main():
    counter = Counter('superfluous')
    print(counter)
    print(list(counter.elements()))
    print(counter.most_common(3))

    counter2 = Counter('super')
    counter.subtract(counter2)
    print(counter)


if __name__ == '__main__':
    main()
