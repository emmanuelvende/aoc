def perms(u):
    """
    Returns a list of all permutations. Each permutation is itself a list of 
    permuted elements.
    """
    if len(u) == 1:
        return [u]
    v = []
    for i, x in enumerate(u):
        w = u[:i] + u[i + 1 :]
        for p in perms(w):
            v.append([x] + p)
    return v


u = list(range(4))
print(perms(u))
