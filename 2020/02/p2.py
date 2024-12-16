import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()


def is_valid(m, M, L, p):
    return int(p[m - 1] == L) + int(p[M - 1] == L) == 1


lines = map(lambda x: x.strip(), lines)

policies = []
passwords = []
for line in lines:
    line = line.split(":")
    policies.append(line[0].strip())
    passwords.append(line[1].strip())

minis = []
maxis = []
letters = []
for policy in policies:
    policy = policy.split(" ")
    minis.append(policy[0].split("-")[0])
    maxis.append(policy[0].split("-")[1])
    letters.append(policy[1])

count = 0
for i in range(len(minis)):
    m = int(minis[i])
    M = int(maxis[i])
    L = letters[i]
    p = passwords[i]
    # print(m, M, L, p)
    if is_valid(m, M, L, p):
        count += 1

print(count)
