import time

f = open("input/2.txt")
inputText = f.read()
inputList = inputText.split(",")

result = 0

def odd(stringInput:str) -> bool:
    return len(stringInput) % 2 == 1

start = time.time()
for input in inputList:
    numStr = input.split('-')
    lowerStr:str = numStr[0]
    upperStr:str = numStr[1]
    lowerNum:int = int(lowerStr)
    upperNum:int = int(upperStr)
    
    initialHalf = ""
    if odd(lowerStr):
        initialHalf = str(10 ** (int((len(lowerStr)+1)/2)-1))
    else:
        initialHalf = lowerStr[:len(lowerStr)//2]
        while int(initialHalf + initialHalf) < lowerNum:
            initialHalf = str(int(initialHalf)+1)
    
    lowerStr = initialHalf + initialHalf

    while (int(lowerStr) <= upperNum):
        if odd(lowerStr):
            firstHalf = str(10 ** (int((len(lowerStr)+1)/2)-1))
            lowerStr = firstHalf + firstHalf
            continue
        firstHalf = lowerStr[:len(lowerStr)//2]
        secondHalf = lowerStr[len(lowerStr)//2:]

        if firstHalf == secondHalf:
            result += int(lowerStr)
            #print("Invalid: ", int(lowerStr))
        
        firstHalf = str(int(firstHalf) + 1)
        lowerStr = firstHalf + firstHalf
        

    # if 232, then next lowest possible one is 1000
    # length = 3 then 10 ** 3 = 1000 which is good
    
end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")