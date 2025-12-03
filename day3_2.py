import time

f = open("input/3.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0

for line in inputList:
    maxList = [-1 for _ in range(12)]
    startIndex = 0

    for i in range(0, len(line)):
        elem = int(line[i])
        startIndex = max(0, i-len(line) + 12)
        for currentIndex in range(startIndex, 12):
            if elem > maxList[currentIndex]:
                maxList[currentIndex] = elem
                
                # reset the digits after
                for j in range(currentIndex+1, 12):
                    maxList[j] = -1
                break
    multiplier = 1        
    num = 0   
    for digit in reversed(maxList):
        num += multiplier * digit
        multiplier *= 10
    
    result += num


end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")