import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = []
for line in L:
    D.append(int(line))

# We keep same recursive strategy but this time we store the nb of containers we have used
# to fill
def all_ways(amount, containers):
    """
    Compute all the ways to use the given containers to fill.
    Returns a list of the nb of containers used each time.
    """

    def _nb_of_ways(amount, containers, how_much_containers):
        """
        Don't return nb of ways anymore. Instead, store the nb of containers used
        """
        if amount == 0:
            how_much_containers_used.append(how_much_containers)
        if containers == []:
            return
        for i, c in enumerate(containers):
            _nb_of_ways(amount - c, containers[i + 1 :], how_much_containers + 1)

    how_much_containers_used = []
    _nb_of_ways(amount, containers, 0)

    return how_much_containers_used


ways_to_fit = all_ways(150, D)
print(ways_to_fit)

mini = min(ways_to_fit)
r = sum(x == mini for x in ways_to_fit)

pr(r)