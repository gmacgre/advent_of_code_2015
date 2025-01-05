import sys
conversions, toConvert = sys.stdin.read().split('\n\n')
convs = {}
for conv in conversions.split('\n'):
    src, out = conv.split(' => ')
    if src not in convs:
        convs[src] = []
    convs[src].append(out)

converted = set()
for i in range(len(toConvert)):
    if toConvert[i] in convs:
        for replacement in convs[toConvert[i]]:
            convert = toConvert[:i] + replacement + toConvert[i+1:]
            converted.add(convert)
    if i == len(toConvert) - 1:
        continue
    if toConvert[i:i+2] in convs:
        for replacement in convs[toConvert[i:i+2]]:
            convert = toConvert[:i] + replacement + toConvert[i+2:]
            converted.add(convert)
print(len(converted))