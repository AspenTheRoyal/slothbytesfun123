def findPath(nestedlist):
    useduplist = nestedlist
    travelpath = ["A"]
    startFromHere = [["A","A"]]
    for i in range(len(useduplist)):
        startFromHere = sorted([sublist for sublist in useduplist if sublist[0] == startFromHere[0][1]],key=lambda x: x[1])
        useduplist.remove(startFromHere[0])
        travelpath.append(startFromHere[0][1])
    print(travelpath)
        


findPath([["C", "F"], ["A", "C"], ["I", "Z"], ["F", "I"]])
#output = ["A", "C", "F", "I", "Z"]

findPath([["A","C"],["A","B"],["C","B"],["B","A"],["B","C"]])
#output = ["A","B","A","C","B","C"]
# Another valid route is ["A","C","B","A","B","C"],
# but it comes later alphabetically.

findPath([["Y", "L"], ["D", "A"], ["A", "D"], ["R", "Y"], ["A", "R"]])
#output = ["A", "D", "A", "R", "Y", "L"]
