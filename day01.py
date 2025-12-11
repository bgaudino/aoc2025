with open("data/day01.txt") as f:
    rotations = f.readlines()

dial = 50
part1 = 0
part2 = 0


def rotate(dial, rotation):
    direction, clicks = rotation[0], int(rotation[1:])

    if direction == "R":
        next_pos = dial + clicks
        return next_pos % 100, next_pos // 100
    elif direction == "L":
        offset = dial % 100
        if offset == 0:
            offset = 100
        hits = 0 if clicks < offset else 1 + (clicks - offset) // 100
        return (dial - clicks) % 100, hits
    else:
        raise ValueError(f'Invalid direction "{direction}".')


for rotation in rotations:
    dial, hits = rotate(dial, rotation)
    if dial == 0:
        part1 += 1
    part2 += hits

print("Part 1:", part1)
print("Part 2:", part2)
