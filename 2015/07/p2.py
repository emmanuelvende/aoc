import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = {}


def int_if_possible(x):
    try:
        return int(x)
    except ValueError:
        return x


# put in form D[signal] = [op, arg1, arg2]
for instr in L:
    left, right = instr.split("->")
    signal = right.strip()
    args = [x.strip() for x in left.split()]
    if len(args) == 1:
        a = int_if_possible(args[0])
        D[signal] = ["", a, None]
    elif len(args) == 2:
        assert args[0] == "NOT"
        a = int_if_possible(args[1])
        assert type(a) == str
        D[signal] = ["NOT", a, None]
    elif len(args) == 3 and args[1] == "RSHIFT":
        a = int_if_possible(args[0])
        assert type(a) == str
        D[signal] = [f"RSHIFT {int(args[2])}", a, None]
    elif len(args) == 3 and args[1] == "LSHIFT":
        a = int_if_possible(args[0])
        assert type(a) == str
        D[signal] = [f"LSHIFT {int(args[2])}", a, None]
    elif (len(args) == 3 and args[1] == "AND") or (len(args) == 3 and args[1] == "OR"):
        a = int_if_possible(args[0])
        b = int_if_possible(args[2])
        D[signal] = [args[1], a, b]
    else:
        assert False
    assert len(D[signal]) == 3


def bitwise_not(x):
    assert type(x) == int
    s_in = f"{x:016b}"
    s_out = "".join(["1" if x == "0" else "0" for x in s_in])
    return int(f"0b{s_out}", 2)


R = {}


def compute(signal):
    if type(signal) == int:
        return signal
    op, arg1, arg2 = D[signal]
    if (op, arg1, arg2) in R:
        return R[(op, arg1, arg2)]
    if op == "" and type(arg1) == int:
        assert arg2 == None
        result = arg1
    elif op == "" and type(arg1) == str:
        assert arg2 == None
        result = compute(arg1)
    elif op == "NOT":
        result = bitwise_not(compute(arg1))
    elif op.startswith("LSHIFT"):
        val = int(op.split()[1])
        result = compute(arg1) << val
    elif op.startswith("RSHIFT"):
        val = int(op.split()[1])
        result = compute(arg1) >> val
    elif op == "OR":
        result = compute(arg1) | compute(arg2)
    elif op == "AND":
        result = compute(arg1) & compute(arg2)
    else:
        assert False
    R[(op, arg1, arg2)] = result
    return result


r = compute("a")

D["b"] = ["", r, None]
R = {}
r = compute("a")

pr(r)
