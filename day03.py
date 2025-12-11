with open("data/day03.txt") as f:
    banks = [list(map(int, line.strip())) for line in f]


def joltage(bank, n):
    batteries = []
    start = 0
    while len(batteries) < n:
        end = len(bank) - n + 1 + len(batteries)
        segment = bank[start:end]
        battery = max(segment)
        batteries.append(battery)
        start += segment.index(battery) + 1
    return int("".join(map(str, batteries)))


part1 = sum(joltage(b, 2) for b in banks)
part2 = sum(joltage(b, 12) for b in banks)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
