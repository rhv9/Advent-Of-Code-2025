import time

f = open("input/7.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0
map = []

memoize = []
for input in inputList:
    map.append(list(input))
    memoize.append([-1 for _ in range(0, len(input))])

sIndex = inputList[0].find('S')
print(inputList[0][sIndex])


def followBeam(map, y, x):
    global result
    global memoize
    if y+1 >= len(map):
        return 0
    
    char = map[y+1][x]
    if char == '.':
        return followBeam(map, y+1, x)
    elif char == '^':
        if memoize[y+1][x] != -1:
            return memoize[y+1][x]
        timelines = 1 + followBeam(map, y+1, x+1)
        timelines += followBeam(map, y+1, x-1)
        memoize[y+1][x] = timelines
        return timelines

result = followBeam(map, 0, sIndex) + 1

end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")
