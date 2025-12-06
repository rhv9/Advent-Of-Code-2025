import time

# Well turns out I did need to do the better idea by compressing anyway xD


def ReCheck(rangeList, skipIndex, left, right):
    shouldAdd = True
    for i in range(0, len(rangeList)):
        if i == skipIndex:
            continue
        rangeLeft =  rangeList[i][0]
        rangeRight =  rangeList[i][1]

        if left < rangeLeft:
            if right < rangeLeft:
                # Fully to the left
                continue
            else:
                newLeft = left
                newRight = 0
                if right > rangeRight:
                    newRight = right
                else:
                    newRight = rangeRight
                
                # Update and do it again
                rangeList[len(rangeList)-1][0] = newLeft
                rangeList[len(rangeList)-1][1] = newRight
                rangeList.remove(rangeList[i])
                return (1, len(rangeList)-1)

        else:
            if right <= rangeRight:
                return (-1, -1)
            elif left <= rangeRight:
                newLeft = rangeLeft
                newRight = right
                #Update and do it again
                rangeList[len(rangeList)-1][0] = newLeft
                rangeList[len(rangeList)-1][1] = newRight
                rangeList.remove(rangeList[i])
                return (1, len(rangeList)-1)
            else:
                continue
    if shouldAdd:
        return (0, -1)
    else:
        return (-1, -1)

f = open("input/5.txt")
inputText = f.read()
inputList = inputText.splitlines()


result = 0
rangeList = []
start = time.time()
for line in inputList:
    if line.find('-') != -1:
        split = line.split('-')
        left = int(split[0])
        right = int(split[1])
        rangeList.append([int(split[0]), int(split[1])])

        output = ReCheck(rangeList, len(rangeList)-1, left, right)
        if output[0] == 0:
            continue
        elif output[0] == 1:
            i = output[1]
            output = ReCheck(rangeList,i, rangeList[i][0], rangeList[i][1])
            while output[0] == 1:
                i = output[1]
                output = ReCheck(rangeList,i, rangeList[i][0], rangeList[i][1])

    elif len(line) == 0:
        break
print(rangeList)
for range in rangeList:
    result += range[1] - range[0]

end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")