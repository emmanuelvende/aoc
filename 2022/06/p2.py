import itertools

with open("input.txt", "r") as f:
    text = f.read()


def test_that_all_char_are_different(u):
    """
    u : iterable
    """
    success = True
    for pair in itertools.combinations(u, 2):
        success = success and (pair[0] != pair[1])
    return success


def find_1st_serie_of_different_chars_in_text(text, nb):
    for i, x in enumerate(text):
        if i >= nb:
            chars = [text[i - k] for k in range(nb)]
            if test_that_all_char_are_different(chars):
                answer = i + 1
                break
    return answer


# for msg in (
#     "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
#     "bvwbjplbgvbhsrlpgdmjqwftvncz",
#     "nppdvjthqldpwncqszvftbrmjlhg",
#     "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
#     "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
# ):
#     print(find_1st_serie_of_different_chars_in_text(msg, 14))

print(find_1st_serie_of_different_chars_in_text(text, 14))
