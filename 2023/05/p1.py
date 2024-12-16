import sys

with open(sys.argv[1], "r") as f:
    data = f.read()

blocks = data.split("\n\n")

# print(blocks)


class M:
    def __str__(self):
        return f"{self.name} --> {str(self.lines)}"


MM = []


for i, block in enumerate(blocks):
    if i == 0:
        seeds_str = block.split(":")[1].strip()
        seeds = [int(s) for s in seeds_str.split()]
        # print(seeds)
    else:
        m = M()
        infos = block.split("\n")
        m.name = infos[0].split()[0]
        m.lines = []
        for x in infos[1:]:
            m.lines.append([int(y) for y in x.split()])
        MM.append(m)

# for x in MM:
# print(x)


# dst, src, rng
def find_which_source_range(s, lines):
    line_index = -1
    for i, line in enumerate(lines):
        _, b, c = line
        if b <= s < b + c:
            line_index = i
            break
    return line_index


def translate_from_line(s, line):
    a, b, c = line
    return s - b + a


def translate_seed(s):
    for m in MM:
        line_index = find_which_source_range(s, m.lines)
        if line_index >= 0:
            s = translate_from_line(s, m.lines[line_index])
    return s


translated_seeds = [translate_seed(s) for s in seeds]
result = min(translated_seeds)
print(result)
