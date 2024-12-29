import sys, math
conns = {}
connections = sys.stdin.read().split('\n')
for c in connections:
    src, _, dst, _ , l = c.split(' ')
    l = int(l)
    if src not in conns:
        conns[src] = {}
    if dst not in conns:
        conns[dst] = {}
    conns[src][dst] = l
    conns[dst][src] = l

def findPath(inPath, conns, node, builtLength):
    if node in inPath:
        return 0
    inPath.add(node)
    if len(inPath) == len(conns):
        inPath.remove(node)
        return builtLength
    toRet = 0
    for c in conns[node]:
        possible = findPath(inPath, conns, c, builtLength + conns[node][c])
        if possible > toRet:
            toRet = possible
    inPath.remove(node)
    return toRet

smallestPath = 0
for start in conns:
    groupSmallest = findPath(set(), conns, start, 0)
    if groupSmallest > smallestPath:
        smallestPath = groupSmallest
print(smallestPath)