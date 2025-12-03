def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def solve():
    banks = process_input()
    total = 0
    for bank in banks:
        maximum = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                joltage = int(bank[i] + bank[j])
                if joltage > maximum:
                    maximum = joltage
        total += maximum
    print(total)

if __name__ == "__main__":
    solve()
