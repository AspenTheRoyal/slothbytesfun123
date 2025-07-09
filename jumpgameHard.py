# This took me quite a while because I couldn't even figure out how to do it in pseudocode, had 4 different functions, but I got it down to this!!

def medium_jump_game(currentIndex,maxJumpLength,indexNeeded):
    listToReturn = [] 
    for i in range(1,maxJumpLength+1): 
        if currentIndex + i == indexNeeded:
            return True # If it gets to the last index, awesome!
        if currentIndex + i < indexNeeded:
            listToReturn.append(i+currentIndex) # And it adds to the list that it will return if it jumps to somewhere before the current index.
    return listToReturn

def jump_game(nums):
    indexNeeded = len(nums) - 1 # the number its trying to get to
    currentIndexList = [0]
    while currentIndexList != []:
        maxJumpLengthList = [nums[i] for i in currentIndexList]
        tempSet = set()
        for indexPosition, maxJump in zip(currentIndexList, maxJumpLengthList):
            # for each index it can be at after however many jumps, it calls medium_jump_game
            # if it makes it to the last index, it just returns True
            tempList = medium_jump_game(indexPosition,maxJump,indexNeeded)
            if tempList == True:
                return True
            tempSet.update(tempList) # then updates a list with indexes it can be at
        currentIndexList = list(tempSet)
    return False
            
    
print(jump_game([3,2,1,0,4]))
print(jump_game([2,3,1,1,4]))
