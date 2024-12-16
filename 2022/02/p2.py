def revert_result(x):
    return "lose" if x == "win" else "win"


def duel(a, b):
    """
    a and b are symbols names (ex : "rock")
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

DUEL_RESULTS = {"X": "lose", "Y": "draw", "Z": "win"}


def what_must_i_play(a, round_result):
    """
    a is symbol name (ex: "paper")
    round_result is one of ("win", "lose", "draw")
    """
    if round_result == "draw":
        return a
    else:
        cases = {
            ("rock", "win"): "paper",
            ("rock", "lose"): "scissors",
            ("paper", "win"): "scissors",
            ("paper", "lose"): "rock",
            ("scissors", "win"): "rock",
            ("scissors", "lose"): "paper",
        }
        return cases[(a, round_result)]


def compute_my_score(his_symbol, my_symbol):
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
        his_symbol = OTHER_SYMBOLS[args[0]]
        duel_result = DUEL_RESULTS[args[1]]
        my_symbol = what_must_i_play(his_symbol, duel_result)
        total_score += compute_my_score(his_symbol, my_symbol)

print(f"{total_score=}")
