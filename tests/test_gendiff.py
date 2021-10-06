from gendiff.scripts.gendiff import generate_diff


def test_comparision():
    a = 'file1.json'
    b = 'file2.json'
    c = json.load(open(result.json))
    assert generate_diff(a, b) == c