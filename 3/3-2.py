import sys
input = sys.stdin
directions = input.read()
sleigh = (0,0)
robot = (0,0)
isSanta = True
houses = set([sleigh])
mods = {
    'v': (0,-1),
    '^': (0,1),
    '<': (-1,0),
    '>': (1,0),
}
for dir in directions:
    mod = mods[dir]
    if isSanta:
        sleigh = (sleigh[0] + mod[0], sleigh[1] + mod[1])
        houses.add(sleigh)
    else:
        robot = (robot[0] + mod[0], robot[1] + mod[1])
        houses.add(robot)
    isSanta = not isSanta

print(len(houses))