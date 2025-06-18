def birthdayCakeCandles(listUsed):
    if len(listUsed) == 0:
        print(0)
        return
    highestNumber = 0
    for i in listUsed:
        if i > highestNumber:
            highestNumber = i
    howMany = 0
    for i in listUsed:
        if i == highestNumber:
            howMany += 1
    print(howMany)
    return
    

birthdayCakeCandles([4,4,1,3])
birthdayCakeCandles([1,1,1,1])
birthdayCakeCandles([])
