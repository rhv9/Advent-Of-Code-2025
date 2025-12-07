import time

f = open("input/7.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0
map = []

for input in inputList:
    map.append(list(input))

sIndex = inputList[0].find('S')
print(inputList[0][sIndex])

def followBeam(map, y, x):
    global result
    if y+1 >= len(map):
        return 0
    
    char = map[y+1][x]
    if char == '.':
        map[y+1][x] = '|'
        followBeam(map, y+1, x)
        return
    elif char == '^':
        result += 1
        if map[y+1][x+1] == '.':
            map[y+1][x+1] = '|'
            followBeam(map, y+1, x+1)
        if map[y+1][x-1] == '.':
            map[y+1][x+1] = '|'
            followBeam(map, y+1, x-1)

followBeam(map, 0, sIndex)




end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")
