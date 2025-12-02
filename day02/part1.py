def process_input():
    with open("input.txt") as f:
        entries = f.read()
        return entries.split(",")


def solve():
    ranges = process_input()
    total = 0
    for r in ranges:
        first, last = r.split("-")
        for i in range(int(first), int(last) + 1):
            pid = str(i)
            half = len(pid) // 2
            part1, part2 = pid[:half], pid[half:]
            if part1 == part2:
                total += i
    print(total)

if __name__ == "__main__":
    solve()
