import argparse
import os
from collections import ChainMap

def main():
    app_defaults = {'username': 'admin', 'password': 'password'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    cmd_line_args = {key: value for key, value in vars(args).items() if value}

    chain_map = ChainMap(cmd_line_args, os.environ, app_defaults)
    print(chain_map['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] = 'test_user'
    main()
