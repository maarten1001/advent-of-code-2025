def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def solve():
    banks = process_input()
    total = 0
    for bank in banks:
        bank = [int(b) for b in bank]
        joltage = ""
        start = 0
        for i in range(12, 0, -1):
            digits = bank[start:len(bank) - i + 1]
            maximum = 0
            index = 0
            for k, v in enumerate(digits):
                if v > maximum:
                    maximum = v
                    index = k
            start += index + 1
            joltage += str(maximum)
        total += int(joltage)
    print(total)

if __name__ == "__main__":
    solve()
