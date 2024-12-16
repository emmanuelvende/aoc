def compute_priority(letter):
    if letter.upper() == letter:
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def find_the_item(line):
    l = len(line)
    k = l // 2
    left = line[:k]
    right = line[k:]
    anomaly = ""
    for x in left:
        if x in right:
            anomaly = x
            break
    return anomaly


total = 0
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    item = find_the_item(line)
    score = compute_priority(item)
    total += score

print(total)
