def maximumSeating(list):
    seats = 0
    currentGap = 0
    newList = [2,2,*list,2,2]
    for item in newList:
        if item == 0:
            currentGap = currentGap + 1
            if currentGap > 4:
                seats = seats + 1
        elif item == 2: 
            currentGap = currentGap + 1
            if currentGap == 5:
                seats = seats + 1
        else:
            currentGap = 0
    print(seats)
    
maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
# output = 2
# [1, 0, 0, 1, 0, 0, 1, 0, 0, 1] 2 new people were seated!

maximumSeating([0, 0, 0, 0])
# output = 2
# [1, 0, 0, 1] 2 new people were seated!

maximumSeating([1, 0, 0, 0, 0, 1])
# output = 0
# There is no way to have a gap of at least 2 chairs when adding someone else.

maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
# output = 2

maximumSeating([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# output = 4
