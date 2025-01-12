import sys, itertools, math
from functools import reduce
input = list(map(int, sys.stdin.read().split('\n')))
target = sum(input) // 3
quantum_entanglement = None
for i in range(1, len(input)):
    for combo in itertools.combinations(input, i):
        if sum(combo) == target:
            quantum_entanglement = reduce(lambda x, y: x * y, combo)
            break
    if quantum_entanglement != None:
        break
print(quantum_entanglement)