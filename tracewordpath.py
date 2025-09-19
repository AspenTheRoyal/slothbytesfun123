def checkAdjacents(word, array, numberOfRow, numberOfColumn,positionToCheck,currentPath): 
    currentList = []
    if numberOfRow != 0 and array[numberOfRow-1][numberOfColumn] == word[positionToCheck] and (not [numberOfRow-1,numberOfColumn] in currentPath): # going up
            currentList.append([numberOfRow-1, numberOfColumn])
    if numberOfRow < len(array)-1 and array[numberOfRow+1][numberOfColumn] == word[positionToCheck] and (not [numberOfRow+1,numberOfColumn] in currentPath): # down
            currentList.append([numberOfRow+1,numberOfColumn])
    if numberOfColumn < len(array[0])-1 and array[numberOfRow][numberOfColumn+1] == word[positionToCheck] and (not [numberOfRow,numberOfColumn+1] in currentPath): # right
            currentList.append([numberOfRow,numberOfColumn+1])
    if numberOfColumn != 0 and array[numberOfRow][numberOfColumn-1] == word[positionToCheck] and (not [numberOfRow,numberOfColumn-1] in currentPath): # left
            currentList.append([numberOfRow,numberOfColumn-1])
    babyPathList = []
    for item in currentList:
        babyPathList.append([*currentPath,item]) 
    return currentList,babyPathList 

def trace_word_path(word, array):
    for numberOfRow, row in enumerate(array):
        for numberOfColumn, letter in enumerate(row):
            if letter == word[0]:
                listOfCoordinatesToTry = [[numberOfRow,numberOfColumn]]
                tempCurrentPaths = [[[numberOfRow,numberOfColumn]]]
                for index, letter in enumerate(word[1:]):
                    tempList = []
                    for item, path in zip(listOfCoordinatesToTry, tempCurrentPaths):
                        addToList, newPaths = checkAdjacents(word,array,item[0],item[1],index+1,path) 
                        if addToList != []:
                            tempCurrentPaths = [] 
                            tempList.extend(addToList)
                            tempCurrentPaths.extend(newPaths)
                    listOfCoordinatesToTry = list(tempList)
                thePath = tempCurrentPaths[0]
                if len(thePath) == len(word):
                    print(thePath)
                    return
    print("Not present")

trace_word_path("BISCUIT", [
    ["B","I","T","R"],
    ["I","U","A","S"],
    ["S","C","V","W"],
    ["D","O","N","E"]
])
# output = [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [0, 1], [0, 2]]
trace_word_path("HELPFUL", [
    ["L","I","T","R"],
    ["U","U","A","S"],
    ["L","U","P","O"],
    ["E","F","E","H"]
])
# output = "Not present"
trace_word_path("UKULELE", [
    ["N","H","B","W"],
    ["E","X","A","D"],
    ["L","A","U","U"],
    ["E","L","U","K"]
])
# output = [[2, 3], [3, 3], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0]]
trace_word_path("SURVIVAL", [
    ["V","L","R","L"],
    ["V","A","I","V"],
    ["I","O","S","C"],
    ["V","R","U","F"]
])
# output = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [0, 1]]    
    
    
