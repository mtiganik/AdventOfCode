from collections import defaultdict
from functools import cache
import re
def parse_data(my_file) -> tuple:
    with open(my_file) as f:
        patterns, designs = tuple(re.findall('\w+', part) for part in f.read().split('\n\n'))
        patterns_dict = defaultdict(list)
        for pat in patterns:
            patterns_dict[pat[0]].append(pat)
        return patterns_dict, designs
@cache
def check_des(design: str) -> int:
    global patterns
    if not design:
        return 1
    total = 0
    for pat in patterns.get(design[0],[]):
        if design.startswith(pat):
            total+= check_des(design.removeprefix(pat))
    return total
def part1(designs: list) -> int:
    return sum(check_des(des)>0 for des in designs)
def part2(designs:list) -> int:
    return sum(check_des(des) for des in designs)

data = parse_data('input.txt')
patterns = data[0]
print('Part 1: ', part1(data[1]))
print('Part 2: ', part2(data[1]))
