import sys
input = sys.stdin.read()

def repeat(input):
    toRet = ''
    count = 0
    val = None
    for c in input:
        if val == None:
            val = c
        if c != val:
            toRet += f'{count}{val}'
            count = 1
            val = c
        else:
            count += 1
    toRet += f'{count}{val}'
    return toRet

for i in range(40):
    input = repeat(input)

print(len(input))