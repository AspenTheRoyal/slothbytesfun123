from collections import Counter

def isValid(string):
    letterCounter = Counter(string)
    numberCounter = Counter(letterCounter.values())
    if len(numberCounter) == 1:
        print("YES") 
        return
    if len(numberCounter) == 2:
        keyList = list(numberCounter.keys())
        if numberCounter[keyList[0]] > numberCounter[keyList[1]]:
            keyList.reverse()
        # key list puts the key with the most occurences in the last position
        # therefore the first one is the outlier and must be one higher than second one to continue
        if keyList[0] - 1 == keyList[1]: 
            if numberCounter[keyList[0]] == 1:
                print("YES")
                return
    print("NO")
            
isValid("abc")
# output = "YES"

isValid("abcc")
# output = "YES"

isValid("abccc")
# output = "NO"

isValid("aabbcd")
# output = "NO"

isValid("aabbccddeefghi")
# output = "NO"

isValid("abcdefghhgfedecba")
# output = "YES"
