import time

f = open("input/11.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0
map = dict()
memoize = dict()

for input in inputList:
    split = input.split(":")
    splitOutput = split[1].split()
    map[split[0]] = splitOutput
    memoize[split[0]] = -1


def check(key):
    global map
    global memoize
    if key == 'out':
        return 1

    outputs = map[key]

    if memoize[key] != -1:
        return memoize[key]

    sum = 0
    for output in outputs:
        sum += check(output)
    
    if memoize[key] == -1:
        memoize[key] = sum
    
    return sum

for output in map["you"]:
    result += check(output)

end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")
