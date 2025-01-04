import itertools, sys
bottles = list(map(int, sys.stdin.read().strip().split('\n')))
total = 0
for i in range(len(bottles)):
    subtotal = 0
    for combination in itertools.combinations(bottles, i):
        if sum(combination) == 150:
            subtotal += 1
    total += subtotal
    if subtotal != 0:
        print(subtotal)
        break
