rolls = set()

with open("data/day04.txt") as f:
    for y, row in enumerate(f):
        for x, val in enumerate(row):
            if val == "@":
                rolls.add((x, y))

deltas = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)


def is_accessible(roll):
    x, y = roll
    neighbors = 0
    for dx, dy in deltas:
        neighbor = x + dx, y + dy
        if neighbor in rolls:
            neighbors += 1
        if neighbors >= 4:
            return False
    return True


part1 = len([r for r in rolls if is_accessible(r)])
part2 = 0
while True:
    accessible_rolls = {r for r in rolls if is_accessible(r)}
    if accessible_rolls:
        part2 += len(accessible_rolls)
        rolls -= accessible_rolls
    else:
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
