import time

f = open("input/6.txt")
inputText = f.read()
inputList = inputText.splitlines()
start = time.time()
nums = []

result = 0

for i in range(0, len(inputList)):
    if i != len(inputList)-1:
        nums.append(inputList[i].split())
    else:
        operators = inputList[i].split()
        
        for j in range(0, len(operators)):
            operator = operators[j]
            sum = 0
            if operator == '+':
                sum = 0
                for numList in nums:
                    sum += int(numList[j])
            elif operator == '*':
                sum = 1
                for numList in nums:
                    sum *= int(numList[j])

            result += sum

end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")