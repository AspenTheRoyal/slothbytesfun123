def is_valid_hex_code(string):
    possibles = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","a","b","c","d","e","f"]
    if string[0] == "#" and len(string) == 7:
        for char in string[1:7]:
            if char not in possibles:
                print("False")
                return
        print("True")
        return
    print("False")


is_valid_hex_code("#CD5C5C")
# output = True

is_valid_hex_code("#EAECEE")
# output = True

is_valid_hex_code("#eaecee")
# output = True

is_valid_hex_code("#CD5C58C")
# output = False
# Length exceeds 6

is_valid_hex_code("#CD5C5Z")
# output = False
# Not all alphabetic characters in A-F

is_valid_hex_code("#CD5C&C")
# output = False
# Contains unacceptable character

is_valid_hex_code("CD5C5C")
# output = False
# Missing #
