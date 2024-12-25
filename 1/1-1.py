import sys
input = sys.stdin
line = input.read()
level = 0
for character in line:
    if character == '(':
        level += 1
    elif character == ')':
        level -= 1
print(level)