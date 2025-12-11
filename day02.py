def parse_range(s):
    start, _, end = s.partition("-")
    return int(start), int(end)


def is_invalid_part1(id):
    id = str(id)
    middle = len(id) // 2
    return id[:middle] == id[middle:]


def is_invalid_part2(id):
    id = str(id)
    middle = len(id) // 2
    for i in range(1, middle + 1):
        n = len(id) // i
        sequence = id[:i] * n
        if sequence == id:
            return True
    return False


with open("data/day02.txt") as f:
    id_ranges = [parse_range(r) for r in f.read().split(",")]

part1 = part2 = 0
for start, end in id_ranges:
    for id in range(start, end + 1):
        if is_invalid_part1(id):
            part1 += id
            part2 += id
        elif is_invalid_part2(id):
            part2 += id

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
