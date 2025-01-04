import sys, re
input = sys.stdin.read().split('\n')
trueSue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def matchesTrueSue(countKey, count):
    match countKey:
        case 'pomeranians' | 'goldfish':
            return count < trueSue[countKey]
        case 'cats' | 'trees':
            return count > trueSue[countKey]
        case _:
            return count == trueSue[countKey]


for potentialAunt in input:
    parts = list(filter(lambda x: x != ':' and x != ',',re.split('(:|,)\\s', potentialAunt)))
    sue = parts.pop(0)
    for i in range(0, len(parts), 2):
        count = int(parts[i+1])
        if not matchesTrueSue(parts[i], count):
            break
    else:
        print(sue)
        break