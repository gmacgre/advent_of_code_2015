import sys, math
input = sys.stdin.read().split('\n')
ingres = []
for ingredient in input:
    _, _, cap, _, dur, _, flav, _, text, _, calor = ingredient.split(' ')
    cap = cap[:-1]
    flav = flav[:-1]
    text = text[:-1]
    dur = dur[:-1]
    ingres.append([int(cap), int(dur), int(flav), int(text), int(calor)])

def incAmts(amts: list[int]) -> list[int]:
    for i in range(len(amts) - 1, -1, -1):
        amts[i] = (amts[i] + 1) % 101
        if amts[i] != 0:
            break
    return amts

def getVal(ingres: list[list[int]], amts: list[int]) -> int:
    value = 1
    for i in range(len(ingres[0]) - 1):
        subValue = 0
        for j in range(len(amts)):
            subValue += ingres[j][i] * amts[j]
        if subValue <= 0:
            return 0
        value *= subValue
    return value
    

amts = [0] * len(ingres)
largest = -math.inf
while True:
    amts = incAmts(amts)
    if sum(amts) != 100:
        continue
    largest = max(largest, getVal(ingres, amts))
    if amts[0] == 100:
        break
print(largest)


