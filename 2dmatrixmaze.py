def moveOneSpot(array,numberOfRow,numberOfColumn,currentPath):
    currentList = [] # this stores possible forks in path
    if numberOfRow != 0 and array[numberOfRow-1][numberOfColumn] == 0 and (not [numberOfRow-1,numberOfColumn] in currentPath): # going up
            currentList.append([numberOfRow-1, numberOfColumn])
    if numberOfRow < len(array)-1 and array[numberOfRow+1][numberOfColumn] == 0 and (not [numberOfRow+1,numberOfColumn] in currentPath): # down
            currentList.append([numberOfRow+1,numberOfColumn])
    if numberOfColumn < len(array[0])-1 and array[numberOfRow][numberOfColumn+1] == 0 and (not [numberOfRow,numberOfColumn+1] in currentPath): # right
            currentList.append([numberOfRow,numberOfColumn+1])
    if numberOfColumn != 0 and array[numberOfRow][numberOfColumn-1] == 0 and (not [numberOfRow,numberOfColumn-1] in currentPath): # left
            currentList.append([numberOfRow,numberOfColumn-1])
    babyPathList = []
    for item in currentList:
        babyPathList.append([*currentPath,item]) 
    return babyPathList 

def canExit(array):
    bottomRightCorner = [len(array)-1,len(array[0])-1]
    listOfCoordinatesToTry = [[0,0]]
    tempCurrentPaths = [[[0,0]]]
    tempList = [1]
    while tempList != []:
        tempList = []
        for item, path in zip(listOfCoordinatesToTry, tempCurrentPaths):
            newPaths = moveOneSpot(array,item[0],item[1],path) 
            if bottomRightCorner in [path[-1] for path in newPaths]:
                print("True")
                return
            if newPaths != []:
                tempCurrentPaths = [] 
                tempList.extend([path[-1] for path in newPaths])
                tempCurrentPaths.extend(newPaths)
                listOfCoordinatesToTry = [path[-1] for path in newPaths]
    print("False")

canExit([
    [0,1,1,1,1,1,1],
    [0,0,1,1,0,1,1],
    [1,0,0,0,0,1,1],
    [1,1,1,1,0,0,1],
    [1,1,1,1,1,0,0]
])
# output = True

canExit([
    [0,1,1,1,1,1,1],
    [0,0,1,0,0,1,1],
    [1,0,0,0,0,1,1],
    [1,1,0,1,0,0,1],
    [1,1,0,0,1,1,1]
])
# output = False

canExit([
    [0,1,1,1,1,0,0],
    [0,0,0,0,1,0,0],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1]
])
# output = False

canExit([
    [0,1,1,1,1,0,0],
    [0,0,0,0,1,0,0],
    [1,1,1,0,0,0,0],
    [1,0,0,0,1,1,0],
    [1,1,1,1,1,1,0]
])
# output = True
# basically when it hits 2,5 it decides to stop working?
