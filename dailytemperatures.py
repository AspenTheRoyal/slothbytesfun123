def daily_temperatures(array):
    output = []
    lastindex = len(array)-1
    for index, temp in enumerate(array):
        for index2, temp2 in enumerate(array):
            if temp2 > temp and index2 > index:
                output.append(index2-index)
                break
            elif index2 == lastindex:
                output.append(0)
    print(output)

daily_temperatures([30,38,30,36,35,40,28])
#output = [1,4,1,2,1,0,0]

daily_temperatures([22,21,20])
#output = [0,0,0]
