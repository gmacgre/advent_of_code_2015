import sys
input = sys.stdin
lines = input.read().split('\n')
states = {}
while len(lines) > 0:
    toCalc = lines.pop(0)
    combination, res = toCalc.split(' -> ')
    combination = combination.split(' ')
    if len(combination) == 1:
        # Direct Transfer from other wire or number
        if combination[0].isnumeric():
            states[res] = int(combination[0])
        else:
            if combination[0] in states:
                states[res] = states[combination[0]]
            else:
                # Base needs to be resolved
                lines.append(toCalc)
    elif len(combination) == 2:
        # NOT
        combination = combination[1]
        if combination not in states:
            lines.append(toCalc)
        else:
            states[res] = states[combination] ^ 65535
    elif len(combination) == 3 and combination[2].isnumeric():
        # LSHIFT and RSHIFT
        if combination[0] not in states:
            lines.append(toCalc)
            continue
        toPlace = 0
        match combination[1]:
            case 'LSHIFT':
                toPlace = states[combination[0]] << int(combination[2])
            case 'RSHIFT':
                toPlace = states[combination[0]] >> int(combination[2])
            case _:
                print('err')
        states[res] = toPlace
    else:
        # OR and AND
        if (not combination[0].isnumeric() and combination[0] not in states) or (not combination[2].isnumeric() and combination[2] not in states):
            lines.append(toCalc)
            continue
        toPlace = 0
        left = int(combination[0]) if combination[0].isnumeric() else states[combination[0]]
        right = int(combination[2]) if combination[2].isnumeric() else states[combination[2]]
        match combination[1]:
            case 'AND':
                toPlace = left & right
            case 'OR':
                toPlace = left | right
        states[res] = toPlace
print(states['a'])