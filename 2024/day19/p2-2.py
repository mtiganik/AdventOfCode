from functools import cache

P, _,*T = open('input.txt').read().split('\n')
P = P.split(', ')

@cache
def count(t):
    return sum(count(t.removeprefix(p)) for p in P
        if t.startswith(p)) or t == ''

for t in bool, int:
    print(sum(map(t, map(count, T))))