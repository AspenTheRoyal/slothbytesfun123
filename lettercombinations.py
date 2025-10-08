def letterCombinations(digits):
    dictionaryOfLetters = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }
    listOfPossibles = []
    if len(digits) > 0:
        listOfPossibles.extend(dictionaryOfLetters[digits[0]])
        for digit in digits[1:]:
            tempList = []
            for letter in dictionaryOfLetters[digit]: 
                for item in listOfPossibles:
                    tempList.append(item+letter)
            listOfPossibles = list(tempList)
    print(listOfPossibles)

letterCombinations("23")
# output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

letterCombinations("")
# output = []

letterCombinations("2")
# output = ["a","b","c"]

letterCombinations("27")
# output = ["ap","aq","ar","as","bp","bq","br","bs","cp","cq","cr","cs"]

letterCombinations("234")
# output = [
  #  "adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
   # "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
   # "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"
# ]

letterCombinations("79")
# output = [ "pw","px","py","pz","qw","qx","qy","qz", "rw","rx","ry","rz", "sw","sx","sy","sz"]
