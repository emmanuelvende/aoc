# import sys

# with open(sys.argv[1], "r") as f:
#     data = f.read()

# lines = data.split("\n")


def v(n):
    return n * (n + 1) // 2


def distance_run(t_waited, t_total):
    speed = t_waited
    t_remaining = t_total - t_waited
    distance = t_remaining * speed
    # print(f"{speed=}, {t_remaining=}, {distance=}")
    return distance


def compute_wins(race_duration, d_to_beat):
    wins = 0
    for t in range(race_duration + 1):
        t_waiting = race_duration - t
        d = distance_run(t_waiting, race_duration)
        # print(t_waiting, t, d)
        if d > d_to_beat:
            wins += 1
    return wins


# durations = [int(s.strip()) for s in lines[0].split(":")[1].split()]
# distances = [int(s.strip()) for s in lines[1].split(":")[1].split()]
# TD = zip(durations, distances)

TD = [(47, 207), (84, 1394), (74, 1209), (67, 1014)]

W = []

for t, d in TD:
    W.append(compute_wins(t, d))

result = 1
for x in W:
    result *= x

print(result)
