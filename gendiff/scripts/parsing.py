import yaml
import copy


def parse(filepath):
    result = yaml.safe_load(open(filepath))
    return result


def compare(a, b):
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
    result = minusresult
    result.update(sameresult)
    result.update(plusresult)
    return result
