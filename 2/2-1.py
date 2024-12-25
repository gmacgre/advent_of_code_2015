import sys
input = sys.stdin
lines = input.read().split('\n')

def wrapAmt(line):
    dims = sorted(list(map(int,line.split('x'))))
    return  3*dims[0]*dims[1] + 2*dims[0]*dims[2] + 2*dims[1]*dims[2]

print(sum([wrapAmt(line) for line in lines]))
    