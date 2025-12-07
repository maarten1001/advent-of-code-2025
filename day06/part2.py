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
    total = 0
    numbers = []
    operator = ''
    for i in range(len(grid[0])):
        number = []
        for j in range(len(grid)):
            number += grid[j][i]
        number = ''.join(number)
        if number.strip() == '':
            # we are done, process the equation
            if operator == '+':
                total += sum(numbers)
            elif operator == '*':
                product = numbers[0]
                for k in range(1, len(numbers)):
                    product *= numbers[k]
                total += product
            else:
                print(f"Failed to define operator in column {i}")
            numbers = []
            operator = ''
        elif number[-1] == '+' or number[-1] == '*':
            operator = number[-1]
            number = number[:-1]
            numbers.append(int(number.strip()))
        else:
            numbers.append(int(number.strip()))
    else:
        # we are done, process the equation
        if operator == '+':
            total += sum(numbers)
        elif operator == '*':
            product = numbers[0]
            for k in range(1, len(numbers)):
                product *= numbers[k]
            total += product
        else:
            print(f"Failed to define operator in final column")
    print(total)


if __name__ == "__main__":
    solve()
