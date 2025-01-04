import sys
input = sys.stdin.read().split('\n')
def distanceTraveled(reindeer, time):
    cycle = reindeer['runTime'] + reindeer['restTime']
    completeCycles = time // cycle
    otherRuntime = min(reindeer['runTime'], time % cycle)
    totalTimeRunning = (completeCycles * reindeer['runTime'])+ otherRuntime
    return totalTimeRunning * reindeer['speed']

allReindeer = {}
for line in input:
    name,     _,  _, speed, _, _, runTime, _, _,  _,   _,   _,  _, restTime, _ = line.split(' ')
    reindeer = {}
    reindeer['speed'] = int(speed)
    reindeer['restTime'] = int(restTime)
    reindeer['runTime'] = int(runTime)
    allReindeer[name] = reindeer

points = {}
for r in allReindeer:
    points[r] = 0

for i in range(1,2504):
    scores = {}
    for r in allReindeer:
        score = distanceTraveled(allReindeer[r], i)
        if score not in scores:
            scores[score] = []
        scores[score].append(r)
    leader = max(list(scores.keys()))
    for r in scores[leader]:
        points[r] += 1

print(max(list(points.values())))