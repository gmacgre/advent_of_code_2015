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
    if isObj and 'red' in object.values():
        return 0
    for i in object:
        sum += findNumbers(object[i] if isObj else i)
    return sum


print(findNumbers(object))