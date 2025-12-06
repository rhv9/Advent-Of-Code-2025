import time

f = open("input/6.txt")
inputText = f.read()
nums = inputText.splitlines()
start = time.time()

result = 0
operatorIndex = len(nums)-1
numFound = []
for i in range(0, len(nums[0])):
    index = -i - 1
    num = ""
    operator = ""

    for j in range(0, len(nums)):
        char = nums[j][index]
        if char == ' ':
            continue
        elif char.isdigit():
            num += char
        else:
            operator = char

    if num != "":
        numFound.append(int(num))

    if operator != "":
        sum = 0
        if operator == '+':
            sum = 0
            for numeral in numFound:
                sum += numeral
        else:
            sum = 1
            for numeral in numFound:
                sum *= numeral
        numFound = []
        result += sum


end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")