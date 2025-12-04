import copy

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


def count_neighbours(grid, x, y):
    neighbours = 0
    for yy in range(max(0, y - 1), min(len(grid), y + 2)):
        for xx in range(max(0, x - 1), min(len(grid[yy]), x + 2)):
            if x == xx and y == yy:
                continue
            if grid[yy][xx] == '@':
                neighbours += 1
    return neighbours


def remove_rolls(grid):
    new_grid = copy.deepcopy(grid)
    removed = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                neighbours = count_neighbours(grid, x, y)
                if neighbours < 4:
                    new_grid[y][x] = 'x'
                    removed += 1
    return new_grid, removed


def solve():
    grid = process_input()
    total = 0
    while True:
        grid, removed = remove_rolls(grid)
        total += removed
        if removed == 0:
            break
    print(total)


if __name__ == "__main__":
    solve()

