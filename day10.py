import time
import math
from collections import deque


f = open("input/10.txt")
inputText = f.read()
inputList = inputText.splitlines()

start = time.time()
result = 0
lightGoal = []

def applyButtonToState(statew, button):
    global lightGoal
    moveDoesGood = False
    for lightPos in button:
        statew[lightPos] = not statew[lightPos] 
        if statew[lightPos] == lightGoal[lightPos]:
            moveDoesGood = True
    
    return (statew, moveDoesGood)

def lightMatches(state, goalState):
    for i in range(0, len(state)):
        if state[i] != goalState[i]:
            return False
    return True

def printConverted(state):
    print(str(['.' if elem == False else '#' for elem in state]))


for input in inputList:
    split = input.split()
    lightGoal = [False if elem == '.' else True for elem in split[0][1:-1]]

    buttonsUnprocessed = split[1:-1]
    buttons = []
    for text in buttonsUnprocessed:
        lis = text[1:-1].split(',')
        buttons.append([int(elem) for elem in lis])

    button_options = [i for i in range(0, len(buttons))]
    firstItem = ([False for _ in lightGoal], button_options)
    queue = deque()
    queue.append(firstItem)
    found = False
    while not found:
        item = queue.popleft()
        state = item[0]
        buttonsLeft = item[1]
        for buttonPos in buttonsLeft:
            res = applyButtonToState(state[:], buttons[buttonPos])
            if lightMatches(res[0], lightGoal):
                count = len(buttons) - len(buttonsLeft) + 1
                result += count
                found = True
                break
            if res[1] == True:
                newItem = (res[0], [elem for elem in buttonsLeft if elem != buttonPos])
                queue.append(newItem)

end = time.time()
print("Result: ", result)
print((end - start) * 1000, "ms")