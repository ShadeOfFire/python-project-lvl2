#!/usr/bin/env python3
import argparse
import json


def generate_diff(filepath1, filepath2):
    a = json.load(open(filepath1))
    b = json.load(open(filepath2))
    sameresult = {}
    minusresult = {}
    plusresult = b
    for i in a:
        if a.get(i) == plusresult.get(i):
            sameresult[i] = a.get(i)
            del plusresult[i]
        else:
            minusresult[i] = a.get(i)
    print('{')
    for i in minusresult:
        print('-', i, minusresult.get(i))
    for i in sameresult:
        print(' ', i, sameresult.get(i))
    for i in plusresult:
        print('+', i, plusresult.get(i))
    print('}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first_file", help="echo the string you use here")
    parser.add_argument("second_file", help="echo the string you use here")
    parser.add_argument("-f", help="set format of output", action="store_true")
    parser.add_argument("--format", help="set format of output", action="store_true")
    args = parser.parse_args()
    if args.format:
       print("format")
    if args.f:
       print("verbosity turned on")
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
