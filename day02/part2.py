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
            for length in range(1, len(pid) // 2 + 1):
                if len(pid) % length == 0:
                    for k in range(len(pid) // length - 1):
                        current_sequence = pid[k * length:(k + 1) * length]
                        next_sequence = pid[(k + 1) * length:(k + 2) * length]
                        if current_sequence != next_sequence:
                            break
                    else:
                        total += i
                        break
    print(total)

if __name__ == "__main__":
    solve()
