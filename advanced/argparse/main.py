import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description='A simple argument parser',
        epilog='This is where you might put example usage'
    )

    # required argument
    parser.add_argument(
        '-x', action='store', required=True, help='Help text for option -x'
    )
    parser.add_argument(
        '-w', '--with', action='store', help='Help text for optional argument -w'
    )

    # optional argument
    parser.add_argument('-y', help='Help text for optional argument -y', default=False)
    parser.add_argument('-z', help='Help text for optional argument -z', type=int)

    # mutually exclusive group
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-q', help='Help text for optional argument -q', default=False
    )
    group.add_argument(
        '-r', help='Help text for optional argument -r', default=False
    )

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    get_args()
