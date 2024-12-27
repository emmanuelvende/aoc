import sys
import pyperclip
import re
import json


def pr(x):
    print(x)
    pyperclip.copy(x)


s = open(sys.argv[1], "r").read()

j = json.loads(s)

# clean the json from everythin that is red
def clean_red(j):
    if type(j) == list:
        return j
    elif type(j) == dict:
        if "red" in j.values():
            return {}
        cleaned = {}
        for k, v in j.items():
            cleaned[k] = clean_red(v)
    else:
        return j




    #     if "red" in j:
    #         return []
    #     cleaned = []
    #     for x in j:
    #         if type(x) in (list, dict):
    #             cleaned.append(clean_red(x))
    #         else:
    #             cleaned.append(x)
    # elif type(j) == dict:
    #     pass

s = json.dumps(j)
m = re.findall("-?\d+\.?\d*", s)
r = sum((int(x) for x in m))
pr(r)
