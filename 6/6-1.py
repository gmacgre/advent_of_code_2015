import sys
class Action():
    ON = 0
    OFF = 1
    TOGGLE = 2
grid = []
for i in range(1000):
    grid.append([0] * 1000)
for line in sys.stdin.read().split('\n'):
    instructStart, end = line.split(' through ')
    start = tuple(list(map(int, instructStart.split(' ')[-1].split(','))))
    end = tuple(list(map(int, end.split(','))))
    action = None
    if instructStart.startswith('toggle'):
        action = Action.TOGGLE
    elif instructStart.startswith('turn on'):
        action = Action.ON
    elif instructStart.startswith('turn off'):
        action = Action.OFF
    
    for i in range(start[0],end[0] + 1):
        for j in range(start[1], end[1] + 1):
            match action:
                case Action.ON:
                    grid[i][j] = 1
                case Action.OFF:
                    grid[i][j] = 0
                case Action.TOGGLE:
                    grid[i][j] = 1 - grid[i][j]

print(sum([sum(i for i in line) for line in grid]))
