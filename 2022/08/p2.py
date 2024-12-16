import sys
import aoc_square


def get_distance_view(me, rest_of_trees):
    view_distance = 0
    for x in rest_of_trees:
        view_distance += 1
        if me <= x:
            break
    return view_distance



def compute_element_score(i, j):
    me = square.get_element(i, j)
    top = square.get_elements_to_top(i, j)
    top_dist = get_distance_view(me, top)

    right = square.get_elements_to_right(i, j)
    right_dist = get_distance_view(me, right)

    bottom = square.get_elements_to_bottom(i, j)
    bottom_dist = get_distance_view(me, bottom)

    left = square.get_elements_to_left(i, j)
    left_dist = get_distance_view(me, left)

    return top_dist * right_dist * bottom_dist * left_dist



def test_01(square):
    for i, j in ((2, 1), (2, 3)):
        me = square.get_element(i, j)
        print(f"{(i,j)} --> {me}")
        top = square.get_elements_to_top(i, j)
        print(f"{top=}")
        top_dist = get_distance_view(me, top)
        print(f"{top_dist=}")

        right = square.get_elements_to_right(i, j)
        print(f"{right=}")
        right_dist = get_distance_view(me, right)
        print(f"{right_dist=}")

        bottom = square.get_elements_to_bottom(i, j)
        print(f"{bottom=}")
        bottom_dist = get_distance_view(me, bottom)
        print(f"{bottom_dist=}")

        left = square.get_elements_to_left(i, j)
        print(f"{left=}")
        left_dist = get_distance_view(me, left)
        print(f"{left_dist=}")

        score = top_dist * right_dist * bottom_dist * left_dist
        print(f"{score=}")
        print("-" * 40)


if __name__ == "__main__":

    square = aoc_square.SquareOfNumbers(sys.argv[1])
    scores = {}
    a = square.side()
    for i in range(a):
        for j in range(a):
            scores[(i, j)] = compute_element_score(i, j)

    print(max(scores.values()))