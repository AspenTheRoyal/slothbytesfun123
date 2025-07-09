def findBrokenKeys(correctStr,wrongStr):
    brokenKeys = set()
    for correctLetter, wrongLetter in zip(correctStr,wrongStr):
        if correctLetter != wrongLetter:
            brokenKeys.add(correctLetter)
    print(list(brokenKeys))

findBrokenKeys("happy birthday", "hawwy birthday") 
# ["p"]

findBrokenKeys("starry night", "starrq light")
# ["y", "n"]

findBrokenKeys("beethoven", "affthoif5")
# ["b", "e", "v", "n"]
