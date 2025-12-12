rolls = set()

with open("data/day05.txt") as f:
    ranges, _, ingredients = f.read().partition("\n\n")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges.split("\n")]
    ingredients = [int(i) for i in ingredients.split("\n")]

part1 = 0
for i in ingredients:
    for start, end in ranges:
        if start <= i <= end:
            part1 += 1
            break

print(f"Part 1: {part1}")


def consolidate(ranges):
    unique_ranges = []
    for start, end in ranges:
        for i, r in enumerate(unique_ranges):
            if r[0] <= start <= r[1]:
                unique_ranges[i] = (r[0], max(r[1], end))
                break
        else:
            unique_ranges.append((start, end))
    return unique_ranges


def valid_count(ranges):
    return sum(e - s + 1 for s, e in ranges)


ranges.sort()
part2 = valid_count(ranges)

while True:
    ranges, overlap = consolidate(ranges)
    count = valid_count(ranges)
    if count == part2:
        break
    part2 = count

print(f"Part 2: {part2}")
