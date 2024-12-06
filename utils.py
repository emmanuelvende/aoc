def tr(m):
    return list(list(line) for line in list(zip(*m)))


def trs(m):
    return list("".join(line) for line in list(zip(*m)))


def vrv(m):
    return list(line for line in m[::-1])


def hrv(m):
    return list(line[::-1] for line in m)


def left(m, n):
    pass


def right(m, n):
    pass


def top(m, n):
    pass


def bottom():
    pass


def main():
    m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    print(m)
    print(tr(m))
    print(vrv(m))
    print(hrv(m))

    ma = ["azerty", "uiopqs", "dfghjk"]
    print(ma)
    print(trs(ma))
    print(vrv(ma))
    print(hrv(ma))


if __name__ == "__main__":
    main()
