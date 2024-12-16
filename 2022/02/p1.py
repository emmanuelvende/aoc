def revert_result(x):
    return "lose" if x == "win" else "win"


def duel(a, b):
    """
    Does b wins upon a ?
    Return "draw" or "win" or "lose" (ie 'a' state)
    """
    if a == b:
        return "draw"
    else:
        cases = {
            ("paper", "scissors"): "win",
            ("paper", "rock"): "lose",
            ("rock", "scissors"): "lose",
        }
        result = cases.get((a, b), None)
        if result:
            return result
        else:
            return revert_result(cases[(b, a)])


OTHER_SYMBOLS = {"A": "rock", "B": "paper", "C": "scissors"}
MY_SYMBOLS = {"X": "rock", "Y": "paper", "Z": "scissors"}
SYMBOL_SCORE = {"rock": 1, "paper": 2, "scissors": 3}


def compute_my_score(other_input, my_input):
    his_symbol = OTHER_SYMBOLS[other_input]
    my_symbol = MY_SYMBOLS[my_input]
    round_result = duel(his_symbol, my_symbol)
    score = SYMBOL_SCORE[my_symbol]
    if round_result == "win":
        score += 6
    elif round_result == "draw":
        score += 3
    return score


total_score = 0
with open("input.txt", "r") as f:
    for line in f:
        args = line.split()
        total_score += compute_my_score(*args)

print(f"{total_score=}")