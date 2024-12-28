import sys
import pyperclip
import re
import json


def pr(x):
    print(x)
    pyperclip.copy(x)


s = open(sys.argv[1], "r").read()

j = json.loads(s)


def clean_red(j):
    if type(j) == list:
        cleaned = []
        for x in j:
            cleaned.append(clean_red(x))
        return cleaned
    elif type(j) == dict:
        if "red" in j.values():
            return {}
        cleaned = {}
        for k, v in j.items():
            cleaned[k] = clean_red(v)
        return cleaned
    else:
        return j


j = clean_red(j)

s = json.dumps(j)
m = re.findall("-?\d+\.?\d*", s)
r = sum((int(x) for x in m))
pr(r)
