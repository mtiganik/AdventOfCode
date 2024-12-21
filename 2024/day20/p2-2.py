from pathlib import Path
from collections import deque, defaultdict
 
 
def parse(input: str) -> tuple[complex, complex, set[complex]]:
    start, end = 0j, 0j
    track: set[complex] = set()
    for y, row in enumerate(input.splitlines()):
        for x, c in enumerate(row):
            p = complex(x, y)
            if c == "S":
                start = p
            elif c == "E":
                end = p
            if c != "#":
                track.add(p)
    return start, end, track
 
 
def costs(start: complex, track: set[complex]) -> dict[complex, int]:
    work: deque[tuple[complex, int]] = deque([(start, 0)])
    result: dict[complex, int] = {start: 0}
    while work:
        point, c = work.popleft()
        c += 1
        for p in (point + 1, point - 1, point + 1j, point - 1j):
            if p in track and p not in result:
                result[p] = c
                work.append((p, c))
    return result
 
 
def part1(saving: int, start: complex, end: complex, track: set[complex]) -> int:
    forward = costs(start, track)
    backward = costs(end, track)
    cheats: dict[int, int] = defaultdict(int)
    fair_route = forward[end]
    for p in forward:
        for d in (1, -1, 1j, -1j):
            if p + 2 * d in backward and p + d not in track:
                cheatcost = forward[p] + 2 + backward[p + 2 * d]
                if cheatcost < fair_route:
                    cheats[fair_route - cheatcost] += 1
    return sum(cheats[s] for s in cheats if s >= saving)
 
 
# TEST = parse(Path("input/day20-test.txt").read_text())
# assert part1(38, *TEST) == 3
 
INPUT = parse(Path("input.txt").read_text())
part1_total = part1(100, *INPUT)
print(f"{part1_total=:,}")  # 1,404
 
 
def cheat_points(distance: int) -> dict[complex, int]:
    result: dict[complex, int] = {}
    for y in range(-distance, distance + 1):
        for x in range(-distance, distance + 1):
            if 2 <= abs(x) + abs(y) <= distance:
                result[complex(x, y)] = abs(x) + abs(y)
    return result
 
 
def part2(
    saving: int, distance: int, start: complex, end: complex, track: set[complex]
) -> int:
    forward = costs(start, track)
    backward = costs(end, track)
    cheats: dict[int, int] = defaultdict(int)
    fair_route = forward[end]
    possible_cheats: list[complex] = cheat_points(distance)
    for p in [q for q in forward if forward[q] < fair_route - saving]:
        for d in possible_cheats:
            if p + d in backward:
                cheatcost = forward[p] + possible_cheats[d] + backward[p + d]
                if cheatcost < fair_route:
                    cheats[fair_route - cheatcost] += 1
 
    return sum(cheats[s] for s in cheats if s >= saving)
 
 
# print(f"{part2(50, 20, *TEST)}")
print("Part 1 works for part 2?", part2(100, 2, *INPUT))
part2_total = part2(100, 20, *INPUT)
print(f"{part2_total=:,}")  # 1,010,981
 