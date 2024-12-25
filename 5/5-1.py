import sys
input = sys.stdin
lines = input.read().split('\n')
notAllowed = ['ab', 'cd', 'pq', 'xy']

def isNice(line):
    for ban in notAllowed:
        if ban in line:
            return 0
    hasRepeat = False
    vowelCount = 0
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            hasRepeat = True
        if line[i] in 'aeiou':
            vowelCount += 1
    if line[len(line) - 1] in 'aeiou':
        vowelCount += 1
    return 1 if hasRepeat and vowelCount > 2 else 0

print(sum(map(isNice, lines)))