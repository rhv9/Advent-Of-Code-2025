import time
import math
from functools import cmp_to_key

f = open("input/8.txt")
inputText = f.read()
inputList = inputText.splitlines()

start = time.time()
result = 0
nums = []

for input in inputList:
    split = input.split(',')
    nums.append([int(elem) for elem in split])

shortestDistances = []

for i in range(0, len(nums)):
    shortestDist = 999999999999
    index = -1
    p1 = nums[i]
    for j in range(i+1, len(nums)):
        dist = math.dist(p1, nums[j])
        if dist < shortestDist:
            shortestDist = dist
            index = j
    shortestDistances.append((i, index, shortestDist))

#shortestDistances.sort()

def compare(item1, item2):
    return item1[2] - item2[2]

sortedNums = sorted(shortestDistances, key=cmp_to_key(compare))

#for i in range(0, len(nums)):
#    print(nums[sortedNums[i][0]], "--", nums[sortedNums[i][1]], "--distance:", sortedNums[i][2])

end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")
