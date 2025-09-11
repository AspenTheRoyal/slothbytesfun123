def evalAlgebra(string):
    indexOfX = string.find("x")
    xSign = "+"
    if indexOfX > 1 and string[indexOfX-2] == "-":
        xSign = "-"
    indexOfEqualSign = string.find("=")
    numberOnRight = int(string[indexOfEqualSign+1:])
    theNumberOnTheLeft = ""
    firstDigitIndex = -1
    for index, character in enumerate(string[:indexOfEqualSign]):
        if character.isdigit():
            if firstDigitIndex == -1:
                firstDigitIndex = index
            theNumberOnTheLeft = theNumberOnTheLeft + character
    if firstDigitIndex == 1:
        theNumberOnTheLeft = int(theNumberOnTheLeft)/-1
    else:
        if string[firstDigitIndex-2] == "-":
            theNumberOnTheLeft = int(theNumberOnTheLeft)/-1
        else:
            theNumberOnTheLeft = int(theNumberOnTheLeft)
    numberOnRight = numberOnRight-theNumberOnTheLeft
    if xSign == "-":
        numberOnRight = numberOnRight/-1
    print(numberOnRight)
            
evalAlgebra("2 + x = 19")
# output = 17

evalAlgebra("4 - x = 1")
# output = 3

evalAlgebra("x + 10 = 53")
# output = 43

evalAlgebra("-23 + x = -20")
# output = 3

evalAlgebra("10 + x = 5")
# output = -5

evalAlgebra("-49 - x = -180")
# output = 131

evalAlgebra("x - 22 = -56")
# output = -34
