import sys
input = sys.stdin.read().split('\n')

def distanceTraveled(reindeer, time):
    #Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
    name,     _,  _, speed, _, _, runTime, _, _,  _,   _,   _,  _, restTime, _ = reindeer.split(' ')
    runTime = int(runTime)
    speed = int(speed)
    restTime = int(restTime)
    cycle = runTime + restTime
    completeCycles = time // cycle
    otherRuntime = min(runTime, time % cycle)
    totalTimeRunning = (completeCycles * runTime)+ otherRuntime
    return totalTimeRunning * speed


print(max([distanceTraveled(line, 2503) for line in input]))