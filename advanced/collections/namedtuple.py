from collections import namedtuple


def main():
    Parts = namedtuple("Part", "id_num desc cost amount")
    auto_parts = Parts(id_num="1234", desc="Ford Engine",
                       cost=1200.00, amount=10)
    print(auto_parts.desc)

    Parts = {
        'id_num': '1234',
        'desc': 'Ford Engine',
        'cost': 1200.00,
        'amount': 10
    }
    print(Parts.keys())
    parts = namedtuple('Parts', Parts.keys())(**Parts)
    print(parts)


if __name__ == '__main__':
    main()
