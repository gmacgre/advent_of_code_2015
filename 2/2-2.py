import sys
input = sys.stdin
lines = input.read().split('\n')

def wrapAmt(line):
    dims = sorted(list(map(int,line.split('x'))))
    return  dims[2]*dims[0]*dims[1] + 2*dims[0] + 2*dims[1]

print(sum([wrapAmt(line) for line in lines]))