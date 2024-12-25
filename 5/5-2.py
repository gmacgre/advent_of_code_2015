import sys
input = sys.stdin
lines = input.read().split('\n')

def isNice(line):
    pairs = {}
    hasDoublePair = False
    hasSandwich = False
    for i in range(len(line) - 1):
        pair = line[i:i+2]
        if pair in pairs and pairs[pair] < i-1:
            hasDoublePair = True
        elif pair not in pairs:
            pairs[pair] = i
        if i < len(line) - 2 and line[i] == line[i+2]:
            hasSandwich = True
    return 1 if hasDoublePair and hasSandwich else 0

print(sum(map(isNice, lines)))