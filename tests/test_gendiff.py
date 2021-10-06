from gendiff.scripts.gendiff import generate_diff
import json
import os


def test_comparision():
    a = 'gendiff/scripts/file1.json'
    b = 'gendiff/scripts/file2.json'
    c = json.load(open('gendiff/scripts/result.json'))
    print('---')
    print(c)
    print('---')
    assert generate_diff(a, b) == c