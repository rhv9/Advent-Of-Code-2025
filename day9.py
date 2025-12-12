import time
import math
from functools import cmp_to_key

f = open("input/9.txt")
inputText = f.read()
inputList = inputText.splitlines()

start = time.time()
result = 0

nums = []

for line in inputList:
    split = line.split(',')
    nums.append([int(elem) for elem in split])



for i in range(0, len(nums)):
    p1 = nums[i]
    for j in range(i, len(nums)):
        p2 = nums[j]

        width = abs(p1[0] - p2[0]) + 1
        height = abs(p1[1] - p2[1]) + 1

        area = width * height

        if area > result:
            result = area

#..............  
#.......#...#..
#..............
#..#....#......
#..............
#..#......#....
#..............
#.........#.#..
#..............


end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")
