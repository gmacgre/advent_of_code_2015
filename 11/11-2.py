import sys
seed = sys.stdin.read()
allowedChars = 'abcdefghjkmnpqrstuvwxyz'
increasingChars = 'abcdefghijklmnopqrstuvwxyz'
idxs = [0] * len(seed)
for i in range(len(idxs)):
    idxs[i] = allowedChars.index(seed[i])

def incSeed(seed: list[int]) -> list[int]:
    for i in range(len(seed) - 1, -1, -1):
        seed[i] = (seed[i] + 1) % len(allowedChars)
        if seed[i] != 0:
            break
    return seed

def convSeedToStr(seed: list[int]) -> str:
    toRet = ''
    for s in seed:
        toRet += allowedChars[s]
    return toRet

def isValidPassword(password: str):
    pairs = set()
    for i in range(0, len(password) - 1):
        if password[i] == password[i+1]:
            if i-1 in pairs:
                continue
            pairs.add(i)
        if len(pairs) > 1:
            break
    if len(pairs) < 2:
        return False
    for i in range(0, len(password) - 2):
        if password[i:i+3] in increasingChars:
            return True
    return False
    

while True:
    idxs = incSeed(idxs)
    toTest = convSeedToStr(idxs)
    if isValidPassword(toTest):
        break

while True:
    idxs = incSeed(idxs)
    toTest = convSeedToStr(idxs)
    if isValidPassword(toTest):
        break

print(toTest)