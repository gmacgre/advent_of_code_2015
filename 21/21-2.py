import sys, itertools as it

def resolveCombat(hp: int, dmg: int, arm: int, php: int, w: tuple, a: tuple, rs: list[tuple]) -> bool:
    pdmg = sum([r[1] for r in rs] + [w[1]])
    parm = sum([r[2] for r in rs] + [a[1]])
    pdmgPerTurn = max(pdmg - arm, 1)
    edmgPerTurn = max(dmg - parm, 1)
    isPlayerTurn = True
    while True:
        if isPlayerTurn: hp -= pdmgPerTurn 
        else: php -= edmgPerTurn
        if php < 0 or hp < 0:
            return isPlayerTurn
        isPlayerTurn = not isPlayerTurn
        


hp, dmg, arm = list(map(lambda x: int(x.split()[-1]), sys.stdin.read().split('\n')))
php = 100
weapons = {
    (8,4),
    (10,5),
    (25,6),
    (40,7),
    (74,8),
}
armor = {
    (0,0),
    (13,1),
    (31,2),
    (53,3),
    (75,4),
    (102,5),
}
rings = {
    (0,0,0),
    (25,1,0),
    (50,2,0),
    (100,3,0),
    (20,0,1),
    (40,0,2),
    (80,0,3),
}

maxCost = 0
for w in weapons:
    for a in armor:
        for rs in list(it.permutations(rings, 2)):
            if not resolveCombat(hp, dmg, arm, php, w, a, rs):
                maxCost = max(maxCost, w[0] + a[0] + sum([r[0] for r in rs]))
print(maxCost)