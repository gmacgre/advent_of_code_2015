import sys
input = sys.stdin
lines = input.read().split('\n')
total = 0
for line in lines:
    charCount = 0
    isEscaped = False
    prevDigit = False
    isHex = False
    for character in line:
        if not isEscaped and character != '\\':
            charCount += 1
        elif isEscaped and character == '\\':
            isEscaped = False
        elif character == '\\':
            isEscaped = True
            charCount += 1
        elif character != 'x' and not isHex:
            isEscaped = False
        elif character == 'x':
            isHex = True
        else:
            if prevDigit:
                isHex = False
                prevDigit = False
                isEscaped = False
            else:
                prevDigit = True
    total += len(line) - charCount + 2
print(f'{total}')