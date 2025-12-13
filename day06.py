import re
from math import prod


def solve(numbers, operators):
    return sum(sum(n) if o == "+" else prod(n) for n, o in zip(numbers, operators))


with open("data/day06.txt") as f:
    lines = f.read().split("\n")

numbers = [list(map(int, re.split(r"\s+", line.strip()))) for line in lines[:-1]]
operators = re.split(r"\s+", lines[-1].strip())
columns = list(zip(*numbers))
part1 = solve(columns, operators)
print(f"Part 1: {part1}")

# Rearrange in right-to-left in columns
columns = []
column = []
for i in range(len(lines[0]) - 1, -1, -1):
    n = ""
    for j, line in enumerate(lines):
        ch = line[i]
        if ch.isdigit():
            n += ch
    if n:
        column.append(int(n))
    else:
        columns.append(column)
        column = []
columns.append(column)

part2 = solve(reversed(columns), operators)

print(f"Part 2: {part2}")
