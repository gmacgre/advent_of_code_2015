import sys
import hashlib
input = sys.stdin
start = input.read()
counter = 0
while True:
    toHash = f'{start}{counter}'
    if hashlib.md5(str.encode(toHash)).hexdigest()[:5] == '00000':
        break
    counter += 1
print(counter)
