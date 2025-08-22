def sameUpsidedown(string):
    newString = ""
    for character, i in zip(string, range(len(string))):
        if character == "0":
            newString = newString + "0"
        if character == "6":
            newString = newString + "9"
        if character == "9":
            newString = newString + "6"
    if newString[::-1] == string:
        print(True)
    else:
        print(False)

sameUpsidedown("6090609")
# output = true

sameUpsidedown("9669")
# output = false
# Becomes 6996 when upside down.

sameUpsidedown("9")
# output = false

sameUpsidedown("0")
# output = true

sameUpsidedown("6090609")
# output = true

sameUpsidedown("60906096090609")
# output = true

sameUpsidedown("966909669")
# output = false
# Becomes 699606699 when upside down.

sameUpsidedown("96666660999999")
# output = false
