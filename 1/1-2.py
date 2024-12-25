import sys
input = sys.stdin
line = input.read()
level = 0
for i in range(len(line)):
    character = line[i]
    if character == '(':
        level += 1
    elif character == ')':
        level -= 1
    if level < 0:
        print(i+1)
        break