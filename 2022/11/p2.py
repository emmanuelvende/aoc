import sys
import itertools

with open(sys.argv[1], "r") as f:
    input_ = f.read()

monkeys_text = input_.split("\n" * 2)


class Monkey:
    def __init__(
        self,
        items,
        op,
        is_div_by_val,
        true_case_monkey_id,
        false_case_monkey_id,
    ):
        self.items = items
        self.op = op
        self.is_div_by_val = is_div_by_val
        self.true_case_monkey_id = true_case_monkey_id
        self.false_case_monkey_id = false_case_monkey_id
        self.inspections = 0


monkeys = []

for monkey_text in monkeys_text:
    # print(monkey_text)
    infos = [info.strip() for info in monkey_text.split("\n")]
    id_, items, op, is_div_by_val, true_case_monkey_id, false_case_monkey_id = infos
    items = [int(x) for x in items.split(":")[1].split(",")]
    op = op.split(":")[1].strip()  # retrieve "new = old * 19"
    op = op.split()
    op = "".join(op[-3:])  # retrieve "old * 19"
    # print(f"{op=}")
    is_div_by_val = int(is_div_by_val.split(":")[1].split()[-1])
    # print(f"{is_div_by_val=}")
    true_case_monkey_id = int(true_case_monkey_id.split(":")[1].split()[-1])
    # print(f"{true_case_monkey_id=}")
    false_case_monkey_id = int(false_case_monkey_id.split(":")[1].split()[-1])
    monkeys.append(
        Monkey(items, op, is_div_by_val, true_case_monkey_id, false_case_monkey_id)
    )
    # print("-" * 40)

divisors = [monkey.is_div_by_val for monkey in monkeys]
ppcm = list(itertools.accumulate(divisors, lambda x, y: x * y))[-1]
# print(ppcm)

NB_ROUNDS = 10000
for round in range(NB_ROUNDS):
    # print(f"{round=}")
    for i, monkey in enumerate(monkeys):
        # print(f"Monkey {i}")
        for item in monkey.items:
            # print(f"  inspecting item of value {item}")
            # print(monkey.op)
            worry_level = (lambda old, operation: eval(operation))(item, monkey.op)
            # print(f"    new worry level : {worry_level}")
            worry_level %= ppcm
            print(f"{round:02d} m{i:01d} w{worry_level:08d}", end="\r")
            if worry_level % monkey.is_div_by_val == 0:
                # print(f"  throws to monkey {monkey.true_case_monkey_id}")
                monkeys[monkey.true_case_monkey_id].items.append(worry_level)
            else:
                # print(f"    throws to monkey {monkey.false_case_monkey_id}")
                monkeys[monkey.false_case_monkey_id].items.append(worry_level)
            monkey.inspections += 1
        monkey.items = []
        # print("-"*40)
print()

# for i, monkey in enumerate(monkeys):
#     print(i, monkey.inspections)

inspections = sorted([m.inspections for m in monkeys])
print(inspections[-1] * inspections[-2])
