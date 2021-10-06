#!/usr/bin/env python3
import argparse
import json
import copy
import collections


def generate_diff(filepath1, filepath2):
    a = json.load(open(filepath1))
    b = json.load(open(filepath2))
    sameresult = {}
    minusresult = {}
    plusresult = copy.deepcopy(b)
    for i in a:
        if a.get(i) == plusresult.get(i):
            sameresult[i] = a.get(i)
            del plusresult[i]
        else:
            j = ('- ' + i)
            minusresult[i] = a.get(i)
            minusresult[j] = minusresult.pop(i)
    dict = copy.deepcopy(plusresult)
    for i in dict:
        j = ('+ ' + i)
        plusresult[j] = plusresult.pop(i)
    dict = copy.deepcopy(sameresult)    
    for i in dict:
        j = ('  ' + i)
        sameresult[j] = sameresult.pop(i)
    print('{')
    result = minusresult
    result.update(sameresult)
    result.update(plusresult)    
    sortedd = collections.OrderedDict(sorted(result.items(), key=lambda s: s[0][2:]))
    for i in sortedd:
        print(i, sortedd.get(i))
    print('}')
    return(sortedd)


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
