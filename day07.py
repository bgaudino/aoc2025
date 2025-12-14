from functools import cache

start = None
beams = set()
splitters = set()

with open("data/day07.txt") as f:
    for y, line in enumerate(f):
        for x, ch in enumerate(line):
            if ch == 'S':
                start = x, y
                beams.add(start)
            elif ch == '^':
                splitters.add((x, y))
    max_y = y

part1 = 0
for _ in range(max_y + 1):
    new_beams = set()
    for x, y in beams:
        y += 1
        if (x, y) in splitters:
            part1 += 1
            new_beams.update(((x - 1, y), (x + 1, y)))
        else:
            new_beams.add((x, y))
    beams = new_beams

print(f"Part 1: {part1}")

@cache
def traverse(x, y):
    if y == max_y:
        return 1
    if (x, y) in splitters:
        return traverse(x - 1, y + 1) + traverse(x + 1, y + 1)
    return traverse(x, y + 1)

part2 = traverse(*start)
print(f"Part 2: {part2}")
