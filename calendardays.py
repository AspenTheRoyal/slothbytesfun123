def dayOfYear(date):
    listOfMonths = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    month, day, year = [int(x) for x in date.split("/")]
    if year % 4 == 0:
        listOfMonths[2] = 29
        if year % 100 == 0:
            listOfMonths[2] = 28
            if year % 400 == 0:
                listOfMonths[2] = 29
    numberOfDays = 0
    for i in range(1,month):
        numberOfDays += listOfMonths[i]
    numberOfDays += day
    print(numberOfDays)
    

dayOfYear("12/13/2020")
#output = 348

dayOfYear("11/16/2020")
#output = 321

dayOfYear("1/9/2019")
#output = 9

dayOfYear("3/1/2004")
#output = 61

dayOfYear("12/31/2000")
#output = 366 # leap year
dayOfYear("12/31/2019")
#output = 365 #non leap year    
