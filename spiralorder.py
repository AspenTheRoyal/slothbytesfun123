import itertools
def spiralOrder(listOriginal):
    output = []
    listTemporary = listOriginal
    for i in listTemporary[0]: # top
        output.append(i)
    listTemporary.pop(0)
    if listTemporary != []: # right side
        for i in listTemporary:
            output.append(i[-1])
            i.pop(-1)
    else:
        return output
    if listTemporary != []:
        listTemporary[-1].reverse()
        for i in listTemporary[-1]:
            output.append(i)
        listTemporary.pop(-1)
    else:
        return output
    theRest = spiralOrder(listTemporary)
    for i in theRest:
        output.append(i)
    print(output)
    
    
spiralOrder([
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
])

spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
