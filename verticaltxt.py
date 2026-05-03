def vertical_txt(sentence):
    output = []
    longestword = 0
    sentence = sentence.split(" ")
    for word in sentence:
        if len(word) > longestword:
            longestword = len(word)
    for i in range(longestword):
        output.append([]) # this is output[i]
        for word in sentence:
            try:
                output[i].append(word[i])
            except IndexError:
                output[i].append("")
    print(output)

vertical_txt("Holy bananas")
"""output = [
  ["H", "b"],
  ["o", "a"],
  ["l", "n"],
  ["y", "a"],
  [" ", "n"],
  [" ", "a"],
  [" ", "s"]
]"""

vertical_txt("Hello fellas")
"""output= [
  ["H", "f"],
  ["e", "e"],
  ["l", "l"],
  ["l", "l"],
  ["o", "a"],
  [" ", "s"]
]"""
