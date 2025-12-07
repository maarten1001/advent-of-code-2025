def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[i for i in j] for j in lines]
        return grid


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end='')
        print()
    print()


def solve():
    grid = process_input()
    grid_count = [[0 for _ in i] for i in grid]
    total = 0
    for y in range(len(grid) - 1):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                grid[y + 1][x] = '|'
                grid_count[y + 1][x] = 1
            elif grid[y][x] == '|':
                if grid[y + 1][x] == '.':
                    grid[y + 1][x] = '|'
                    grid_count[y + 1][x] += grid_count[y][x]
                elif grid[y + 1][x] == '^':
                    grid[y + 1][x - 1] = '|'
                    grid_count[y + 1][x - 1] += grid_count[y][x]
                    grid[y + 1][x + 1] = '|'
                    grid_count[y + 1][x + 1] += grid_count[y][x]
                    total += 1
    print(total)


if __name__ == "__main__":
    solve()

