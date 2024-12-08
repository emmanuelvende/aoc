import sys

lines = open(sys.argv[1]).read().split("\n")


def is_valid(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    a = numbers[0]
    b = numbers[1]
    remains = numbers[2:]
    if (
        is_valid(result, [a + b] + remains)
        or is_valid(result, [a * b] + remains)
        or is_valid(result, [int(f"{a}" + f"{b}")] + remains)
    ):
        return True
    return False


answer = 0
for line in lines:
    target, numbers = line.split(":")
    target = int(target)
    numbers = numbers.split()
    numbers = list(int(n.strip()) for n in numbers)
    if is_valid(target, numbers):
        answer += target

print(answer)
