import time

# Better solution idea:
#   Algorithm first tries to make a condensed range list that
#   finds overlaps to reduce number of checks for each ingredient
#   
# The current solution feels like I just took advantage of a
# "library" to solve it as python makes it ez pz.
# If I was solving without the power of bignum in python, I would
# have to implement checking it digit by digit is my first idea.
#
# A compare function would look like this:
#   First check num of digits, easy teltale if it is less or not
#   Otherwise 
#       Check character by character from biggest digit (leftmost)
#       and compare to see if less than or not. If it is, then
#       we know it is less than the other number. 
#       what is after doesn't matter. If it is equal, then
#       continue down the chain of digits. BOOM SOLVED!

f = open("input/5.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()

result = 0

rangeList = []

for line in inputList:
    if line.find('-') != -1:
        split = line.split('-')
        rangeList.append((int(split[0]), int(split[1])))
    elif len(line) == 0:
        continue
    else:
        num = int(line)
        for range in rangeList:
            if num >= range[0] and num <= range[1]:
                result +=1
                break


end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")