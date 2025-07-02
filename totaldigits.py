def digits(n):
    coolString = ""
    for i in range(1,n):
        coolString = coolString + str(i)
    length = len(coolString)
    print(length)
        

digits(1)
# output = 0

digits(10)
# output = 9

digits(100)
# output = 189

digits(2020)
# output = 6969
