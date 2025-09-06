import math
def convert_to_title(number):
    alphabet = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    finalThing = []
    finalThing.insert(0,alphabet[number%26-1])
    if number%26 != 0:
        number2 = number-number%26
    else:
        number2 = number-26
    while number2 > 25:
        number2 = number2/26
        finalThing.insert(0,alphabet[int(number2%26-1)])
        number2 = math.floor(number2-1)
    print(finalThing)
    
convert_to_title(1)
# output = "A"

convert_to_title(18)
# output = "R"

convert_to_title(28)
# output = "AB"

convert_to_title(52)
# output = "AZ"

convert_to_title(701)
# output = "ZY"
convert_to_title(229704)
# output = "MATT"
convert_to_title(209380622941)
# output = "ZATOICHI"
