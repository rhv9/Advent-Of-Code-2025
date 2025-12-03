import time

f = open("input/3.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0

for line in inputList:
    left = 0
    right = 0

    for i in range(0, len(line)-1):
        elem = int(line[i])
        if elem > left:
            left = elem
            right = -1
        elif elem > right:
            right = elem

    if right == -1:
        right = int(line[-1])
    elif int(line[-1]) > right:
        right = int(line[-1])

    num = left * 10 + right
    result += num


end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")