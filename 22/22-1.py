import sys, math
def fightboss(ehp: int, edmg: int, php: int, pmana: int, actions: str) -> bool:
    poison = 0
    shield = 0
    recharge = 0
    isPlayerTurn = True
    spent = 0
    idx = 0
    while True:
        if idx >= len(actions):
            return -1
        a = actions[idx]
        pdef = 0
        if poison:
            ehp -= 3
            poison = max(poison - 1, 0)
        if shield:
            pdef = 7
            shield = max(shield - 1, 0)
        if recharge:
            pmana += 101
            recharge = max(recharge - 1, 0)
        if isPlayerTurn:
            match a:
                case 'M':
                    spent += 53
                    ehp -= 4
                    pmana -= 53
                case 'D':
                    spent += 73
                    ehp -= 2
                    php += 2
                    pmana -= 73
                case 'S':
                    spent += 113
                    if shield:
                        return -1
                    shield = 6
                    pmana -= 113
                case 'P':
                    spent += 173
                    if poison:
                        return -1
                    poison = 6
                    pmana -= 173
                case 'R':
                    spent += 229
                    if recharge:
                        return -1
                    recharge = 5
                    pmana -= 229
            if pmana < 0:
                return -1
        else:
            php -= max(edmg - pdef, 1)
            idx += 1
        if ehp <= 0:
            return spent
        elif php <= 0:
            return -1
        isPlayerTurn = not isPlayerTurn

def iterate_actions(pos):
    actions[pos] = 'DSPRM'['MDSPR'.index(actions[pos])]
    if actions[pos] == 'M':
        if pos+1 <= len(actions):
            iterate_actions(pos+1)


ehp, edmg = list(map(lambda x: int(x.split()[-1]), sys.stdin.read().split('\n')))
php = 50
pmana = 500
actions = ['M'] * 20
min_spent = math.inf
for i in range(1000000):
    result = fightboss(ehp, edmg, php, pmana, actions)
    if result != -1:
        min_spent = min(result, min_spent)
    iterate_actions(0)    
print(min_spent)