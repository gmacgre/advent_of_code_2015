import sys
input = sys.stdin
directions = input.read()
sleigh = (0,0)
houses = set([sleigh])
mods = {
    'v': (0,-1),
    '^': (0,1),
    '<': (-1,0),
    '>': (1,0),
}
for dir in directions:
    mod = mods[dir]
    sleigh = (sleigh[0] + mod[0], sleigh[1] + mod[1])
    houses.add(sleigh)

print(len(houses))