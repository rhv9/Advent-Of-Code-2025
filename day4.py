import time

f = open("input/4.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0

height = len(inputList)
width = len(inputList[0])

for y in range(0, height):
    for x in range(0, width):
        if inputList[y][x] == '.':
            continue

        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if count >= 4:
                    break
                offsetx = x+j
                offsety = y+i
                if offsetx < 0 or offsetx >= width or offsety < 0 or offsety >= height:
                    continue

                if inputList[offsety][offsetx] == '@':
                    count+=1
                    
            if count >= 4:
                break

        if count < 4:
            result += 1


end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")