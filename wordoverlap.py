def overlap(word1, word2):
    if word1 == word2:
        return word1 # Just a quickie check
    for i in range(len(word2)-1,1,-1): # so it basically checks if the first i letters of word2 equals the last i letters of word1. it starts at most specific, e.g. does "sweden" equal "denmar", then does "weden" equal "denma". it does this until it finds a match.
        if word2[:i] == word1[-i:]: # if first i letters of word2 equals last i letters of word1
            return word1+word2[i:] # word1 + word2 without the matching characters
    return word1+word2 # if they didnt overlap, just combine word1 and word2
    
print(overlap("sweden", "denmark"))
# output = "swedenmark"

print(overlap("honey", "milk"))
# output = "honeymilk"

print(overlap("dodge", "dodge"))
# output = "dodge"

print(overlap("commitment","mention"))
# output = "commitmention"

print(overlap("horizon","zoning"))
# output = "horizoning"
