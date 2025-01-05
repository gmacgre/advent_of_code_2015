import sys, math, re
conversions, toConvert = sys.stdin.read().split('\n\n')
convs = {}
for conv in conversions.split('\n'):
    src, out = conv.split(' => ')
    if out not in convs:
        convs[out] = []
    convs[out].append(src)

def collapseMedicine(convs: dict[list[str]], toCollapse: str, movesMade: int) -> int:
    if toCollapse == 'e':
        return movesMade
    fewestMoves = math.inf
    for collapsable in convs:
        idxs = [match.start() for match in re.finditer(collapsable, toCollapse)]
        for idx in idxs:
            for replacement in convs[collapsable]:
                collapsed = toCollapse[:idx] + replacement + toCollapse[idx+len(collapsable):]
                totalMoves = collapseMedicine(convs, collapsed, movesMade + 1)
                if totalMoves != math.inf:
                    return totalMoves
    return fewestMoves
        


print(collapseMedicine(convs, toConvert, 0))