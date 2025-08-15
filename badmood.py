def greatestImpact(list):
    mood = sum([item[0] for item in list])/len(list)
    differences = { # finding how far all are from mood on avg
        "Weather": mood-sum([item[1] for item in list])/len(list),
        "Meals": mood-sum([item[2] for item in list])/len(list)*3,
        "Sleep": mood-sum([item[3] for item in list])/len(list),
    }
    if mood == 10:
        print("Nothing")
        return
    print(max(differences,key=differences.get)) # finds the factor closest to mood on avg

greatestImpact([
  [1, 1, 3, 10],
  [1, 1, 3, 10],
  [1, 1, 3, 10]
])
# output = "Weather"
# Weather was always low but all others were high.

greatestImpact([
  [10, 10, 3, 10],
  [10, 10, 3, 10],
  [10, 10, 3, 10]
])
# output = "Nothing"

# Great days! all values were high.

greatestImpact([
  [8, 9, 3, 10],
  [2, 10, 1, 9],
  [1, 9, 1, 8]
])
# output = "Meals"

greatestImpact([
  [10, 9, 3, 9],
  [1, 8, 3, 4],
  [10, 9, 2, 8],
  [2, 9, 3, 2]
])
# output = "Sleep"
