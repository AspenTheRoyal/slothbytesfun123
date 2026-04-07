# Better late than never?

vowels = ["a","e","i","o","u"]
def removeLastVowel(sentence):
    listofwords = sentence.split(" ")
    newlist = []
    for word in listofwords:
        listword = list(word)
        latestindex = 0
        for index, letter in enumerate(listword):
            if letter in vowels:
                latestindex = index
        newword = [value for index, value in enumerate(listword) if index != latestindex]
        newlist.append("".join(newword))
    newsentence = " ".join(newlist)
    print(newsentence)

removeLastVowel("Those who dare to fail miserably can achieve greatly.")
#output = "Thos wh dar t fal miserbly cn achiev gretly."

removeLastVowel("Love is a serious mental disease.")
#output = "Lov s  serios mentl diseas"

removeLastVowel("Get busy living or get busy dying.")
#output = "Gt bsy livng r gt bsy dyng"

removeLastVowel("If you want to live a happy life, tie it to a goal, not to people.")
#output = "f yo wnt t liv  hppy lif, ti t t  gol, nt t peopl."
