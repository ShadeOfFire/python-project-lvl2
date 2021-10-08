#!/usr/bin/env python3
import argparse

from collections import OrderedDict
from gendiff.scripts.parsing import parse
from gendiff.scripts.parsing import compare


def generate_diff(filepath1, filepath2):
    a = parse(filepath1)
    b = parse(filepath2)
    result = compare(a, b)
    print('{')
    sortedd = OrderedDict(sorted(result.items(), key=lambda s: s[0][2:]))
    for i in sortedd:
        print(i, sortedd.get(i))
    print('}')
    return(sortedd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first_file", help="echo the string you use here")
    parser.add_argument("second_file", help="echo the string you use here")
    parser.add_argument("-f", help="set format of output", action="store_true")
    help = "set format of output"
    parser.add_argument("--format", help=help, action="store_true")
    args = parser.parse_args()
    if args.format:
        print("format")
    if args.f:
        print("verbosity turned on")
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
