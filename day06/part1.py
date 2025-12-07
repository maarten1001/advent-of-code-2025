def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[i for i in j.split()] for j in lines]
        return grid


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end='')
        print()
    print()


def solve():
    grid = process_input()
    total = 0
    for i in range(len(grid[0])):
        result = int(grid[0][i])
        for j in range(1, len(grid) - 1):
            if grid[-1][i] == '+':
                result += int(grid[j][i])
            else:
                result *= int(grid[j][i])
        total += result
    print(total)


if __name__ == "__main__":
    solve()
