def bingo_check(array):
    downslopecount = 0
    upslopecount = 0
    verticalcounts = [0,0,0,0,0]
    for index1, row in enumerate(array):
        horizontalcount = 0
        for index2, element in enumerate(row): # horizontal check
            if element == "x":
                horizontalcount += 1
            if index1 == index2 and element == "x":
                downslopecount += 1
            if index1 + index2 == 5 and element == "x":
                upslopecount += 1
            if element == "x":
                verticalcounts[index2] += 1
        if horizontalcount == 5:
            print("True")
            return
    if upslopecount == 5:
        print("True")
        return
    if downslopecount == 5:
        print("True")
        return
    if 5 in verticalcounts:
        print("True")
        return
    print("False")

bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
])
#output = True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) 
#output = True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) 
#output = True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) 
#output = False
