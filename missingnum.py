def missingNum(newlist):
    newlist.sort()
    newlist.append(11)
    print(newlist)
    correctorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, (wrong, right) in enumerate(zip(newlist,correctorder),start=1):
        if wrong != right:
            print(correctorder[index-1])
            return

missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10])
#output = 5

missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8])
#output 10

missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9])
#output = 7
