def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def solve():
    rotations = process_input()
    dial = 50
    zeroes = 0
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == 'L':
            dial -= distance
        elif direction == 'R':
            dial += distance
        else:
            print(f"Invalid direction {direction}!")
        dial = dial % 100
        if dial < 0:
            dial += 100
        if dial == 0:
            zeroes += 1
    print(zeroes)


if __name__ == "__main__":
    solve()
