def get_elements_before(u, i):
    return u[:i]


def get_elements_after(u, i):
    return u[i + 1 :]


def get_row(rows, i):
    return rows[i]


def get_column(rows, i):
    return list([row[i] for row in rows])


def get_elements_to_right(rows, i, j):
    """
    i: col_index, j : row_index
    """
    return get_elements_after(get_row(rows, j), i)


def get_elements_to_left(rows, i, j):
    return list(reversed(get_elements_before(get_row(rows, j))))


def get_elements_to_bottom(rows, i, j):
    return get_elements_after(get_column(rows, i), j)


def get_elements_to_top(rows, i, j):
    return list(reversed(get_elements_before(get_column(rows, i), j)))


def compute_rows_from_input_filename(input_filename):
    with open(input_filename, "r") as f:
        lines = f.readlines()
    # Append new line at end of input:
    lines[-1] += "\n"
    _rows = []
    for line in lines:
        row = [int(x) for x in line[:-1]]   # each line is '\n' terminated
        _rows.append(row)
    return _rows


class SquareOfNumbers:
    def __init__(self, input_filename):
        self._rows = compute_rows_from_input_filename(input_filename)

    def get_element(self, i, j):
        return self._rows[j][i]

    def get_row(self, i):
        return self._rows[i]

    def get_column(self, i):
        return list([row[i] for row in self._rows])

    def get_elements_to_right(self, i, j):
        return get_elements_after(get_row(self._rows, j), i)

    def get_elements_to_left(self, i, j):
        return list(reversed(get_elements_before(get_row(self._rows, j), i)))

    def get_elements_to_bottom(self, i, j):
        return get_elements_after(get_column(self._rows, i), j)

    def get_elements_to_top(self, i, j):
        return list(reversed(get_elements_before(get_column(self._rows, i), j)))

    def side(self):
        return len(self._rows)

    def __str__(self):
        s = ""
        for k in range(len(self._rows)):
            s += f"{self.get_row(k)}\n"
        return s[:-1]


def test_print_rows(square):
    print("ROWS :")
    for k in range(square.side()):
        print(f"{k} --> {square.get_row(k)}")


def test_print_columns(square):
    print("COLUMNS :")
    for k in range(square.side()):
        print(f"{k} --> {square.get_column(k)}")


def test_print_elements_to_direction(square):
    for i, j in ((2, 3), (3, 3), (2, 1)):
        print(f"{(i, j)} -> {square.get_elements_to_top(i, j)=}")
        print(f"{(i, j)} -> {square.get_elements_to_right(i, j)=}")
        print(f"{(i, j)} -> {square.get_elements_to_bottom(i, j)=}")
        print(f"{(i, j)} -> {square.get_elements_to_left(i, j)=}")
        print(40 * "-")


def test_print_elements(square):
    for i, j in ((2, 3), (3, 3), (2, 1)):
        print(f"{(i, j)} = {square.get_element(i, j)=}")


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1]
    square = SquareOfNumbers(input_filename)
    print(square)
    test_print_elements(square)
    test_print_rows(square)
    test_print_columns(square)
    test_print_elements_to_direction(square)
