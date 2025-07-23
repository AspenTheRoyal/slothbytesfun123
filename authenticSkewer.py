from collections import Counter

def is_authentic_skewer(skewerString):
    listOfVowels = ["A","E","I","O","U","Y"] # We're pretending Y is a vowel here
    if any(letter.isupper() for letter in skewerString) and ("-" in skewerString) and not skewerString[(len(skewerString)-1)] in listOfVowels: # Makes sure letters and - are present in skewerString. Also makes sure last letter is not a vowel.
        lastLetterStatus = True # basically tells the code theres a vowel before the first letter, so that it returns false if the first letter is a vowel
        listOfHyphenCounts = Counter()
        for letter in skewerString:
            if letter == "-":
                hyphenCount += 1
                continue
            else:
                if "hyphenCount" in locals(): # if hyphenCount is a variable
                    listOfHyphenCounts[hyphenCount] += 1
                hyphenCount = 0
            if (letter in listOfVowels) ^ lastLetterStatus: # This is making sure that only the current letter or the letter before it is a vowel. If both are vowels or neither are vowels, it is false
                lastLetterStatus = not lastLetterStatus # If they're different, then the current letter is the opposite type of the last letter so it sets lastLetterStatus to reflect that.
            else:
                return False
        if len(listOfHyphenCounts) == 1: # Only one amount of hyphens between letters
            return True
    return False
            
        
print(is_authentic_skewer("B--A--N--A--N--A--S"))
# output = True

print(is_authentic_skewer("A--X--E"))
# output = False
# Should start and end with a consonant.

print(is_authentic_skewer("C-L-A-P"))
# output = False
# Should alternate between consonants and vowels.

print(is_authentic_skewer("M--A---T-E-S"))
# output = False
# Should have consistent spacing between letters.
