calories = []
total = 0

with open("input.txt", "r") as f:
    for line in f:
        text = line[:-1]
        if not text:
            calories.append(total)
            total = 0
        else:
            total += int(text)

print(calories)
maxi = max(calories)
elf_max = calories.index(maxi)

# Part-1 solving
print(f"Rank : {elf_max+1} with {maxi} calories")

# Part-2 solving
calories_ordered = sorted(calories)
print(calories_ordered)
top_three_total = sum(calories_ordered[-1:-4:-1])
print(f"{top_three_total=}")
