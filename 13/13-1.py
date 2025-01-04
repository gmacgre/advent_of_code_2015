import sys, itertools
input = sys.stdin.read().split('\n')
visitors = set()
points = {}
for line in input:
    # A would g/l      X happiness units by sitting next to B.
    src,    _, op, count,        _,    _, _,      _,   _, _, dst = line.split(' ')
    dst = dst[:-1]
    count = int(count)
    visitors.add(src)
    visitors.add(dst)
    if src not in points:
        points[src] = {}
    points[src][dst] = count if op == 'gain' else -count

def getPointVal(config, points):
    toRet = 0
    for i in range(len(config)):
        sitter = config[i]
        next = config[(i+1)%len(config)]
        prev = config[(i-1)%len(config)]
        toRet += points[sitter][next] + points[sitter][prev]
    return toRet

print(max([getPointVal(config, points) for config in itertools.permutations(list(visitors))]))