def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[i for i in j] for j in lines]
        return grid


def print_grid(grid, grid_count):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end=' ')
        print('  ', end='')
        for x in range(len(grid_count[y])):
            if grid_count[y][x] == 0:
                print('.', end=' ')
            else:
                print(grid_count[y][x], end=' ')
        print()
    print()


def solve():
    grid = process_input()
    grid_count = [[0 for _ in i] for i in grid]
    for y in range(len(grid) - 1):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                grid[y + 1][x] = '|'
                grid_count[y + 1][x] = 1
            elif grid[y][x] == '|':
                if grid[y + 1][x] == '.' or grid[y + 1][x] == '|':
                    grid[y + 1][x] = '|'
                    grid_count[y + 1][x] += grid_count[y][x]
                elif grid[y + 1][x] == '^':
                    grid[y + 1][x - 1] = '|'
                    grid_count[y + 1][x - 1] += grid_count[y][x]
                    grid[y + 1][x + 1] = '|'
                    grid_count[y + 1][x + 1] += grid_count[y][x]
    print(sum([int(i) for i in grid_count[-1]]))


if __name__ == "__main__":
    solve()
