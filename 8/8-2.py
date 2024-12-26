import sys
input = sys.stdin
lines = input.read().split('\n')
total = 0
for line in lines:
    increase = 2
    for char in line:
        if char in '\\"':
            increase += 1
    total += increase
print(f'{total}')