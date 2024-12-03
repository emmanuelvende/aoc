with open("in.txt", "r") as f:
    lines = f.read().split("\n")

reports = list(list(map(int, line.split())) for line in lines)


def safe_increase_condition(prev, next):
    return next > prev and 1 <= abs(next - prev) <= 3


def safe_decrease_condition(prev, next):
    return next < prev and 1 <= abs(next - prev) <= 3


def safe_progressing(report, condition):
    safe = True
    prev = report[0]
    for next in report[1:]:
        if condition(prev, next):
            prev = next
            continue
        safe = False
        break
    return safe


def is_safe(report):
    return safe_progressing(report, safe_increase_condition) or safe_progressing(
        report, safe_decrease_condition
    )


safes = list(report for report in reports if is_safe(report))

result = len(safes)
print(result)
