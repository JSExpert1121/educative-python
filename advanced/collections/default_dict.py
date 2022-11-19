from collections import defaultdict


def main():
    sentence = "The red for jumped over the fence and ran to the zoo for food"
    words = sentence.split(' ')

    d = defaultdict(int)
    for word in words:
        d[word] += 1

    print(d)

    my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
               (345, 222.66), (678, 300.25), (1234, 35.67)]
    
    d = defaultdict(list)
    for num, value in my_list:
        d[num].append(value)

    print(d)

    animal = defaultdict(lambda: 'Monkey')
    animal['sam'] = 'Tiger'
    print(animal['Nick'])
    print(animal)


if __name__ == '__main__':
    main()
