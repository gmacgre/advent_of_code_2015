import sys, re
def runInstr(instr: str, a: int, b: int, idx: int) -> list[int]:
    cutup = re.split(r' |, ', instr)
    match cutup[0]:
        case 'hlf':
            a = a / 2 if cutup[1] == 'a' else a
            b = b / 2 if cutup[1] == 'b' else b
        case 'tpl':
            a = a * 3 if cutup[1] == 'a' else a
            b = b * 3 if cutup[1] == 'b' else b
        case 'inc':
            a = a + 1 if cutup[1] == 'a' else a
            b = b + 1 if cutup[1] == 'b' else b
        case 'jmp':
            idx += int(cutup[1])
        case 'jie':
            if  cutup[1] == 'a' and a % 2 == 0 or \
                cutup[1] == 'b' and b % 2 == 0:
                idx += int(cutup[2])
            else:
                idx += 1
        case 'jio':
            if  cutup[1] == 'a' and a == 1 or \
                cutup[1] == 'b' and b == 1:
                idx += int(cutup[2])
            else:
                idx += 1
    
    if cutup[0] not in ['jmp', 'jie', 'jio']:
        idx += 1
    return a, b, idx

instr = sys.stdin.read().split('\n')
idx = 0
a, b = [0,0]
while idx < len(instr) and idx >= 0:
    a, b, idx = runInstr(instr[idx], a, b, idx)
print(b)