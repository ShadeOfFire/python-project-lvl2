#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("first_file", help="echo the string you use here")
parser.add_argument("second_file", help="echo the string you use here")
parser.add_argument("-f", "--format", help="set format of output")
parser.parse_args()

if args.f:
    print("verbosity turned on")

if args.format:
    print("format")





def main():
    print('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()
