import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = []
for line in L:
    D.append(int(line))

def nb_of_ways(amount, containers):
    """
    Nb of ways to put `amount` among the `containers`
    Base cases:
        - if amount == 0, only one way : [] (return 1)
        - if containers == [], no way (return 0)
    Else:
        iterate on all containers ; for each one, recall the same
        function with the adjusted amount and the remaining containers 
    """
    if amount == 0:
        return 1
    if containers == []:
        return 0
    t = 0
    for i, c in enumerate(containers):
        t += nb_of_ways(amount - c, containers[i + 1 :])
    return t

r = nb_of_ways(150, D)
pr(r)