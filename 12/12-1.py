import sys, json
input = sys.stdin
object = json.loads(input.read())

def findNumbers(object):
    if type(object) == type(1):
        return object
    if type(object) == type('ads'):
        return 0
    sum = 0
    isObj = type(object) == type({})
    for i in object:
        sum += findNumbers(object[i] if isObj else i)
    return sum

print(findNumbers(object))