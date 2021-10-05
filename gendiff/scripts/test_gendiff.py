from gendiff import generate_diff
import json


def test_comparition():
    a = 'file1.json'
    b = 'file2.json'
    c = open('result.json')
    #print(a)
    #print(b)
    print(c)
    print(generate_diff(a, b))
    #assert generate_diff(a, b) == c

test_comparition()
