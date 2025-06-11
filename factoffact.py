import math
def fact_of_fact(number):
    factorials = []
    for i in range(1,number+1):
        factorials.append(math.factorial(i))
    currentNumber = 1
    for i in factorials:
        currentNumber = currentNumber*i
    print(currentNumber)
    
fact_of_fact(4)
# output = 288
# // 4! * 3! * 2! * 1! = 288

fact_of_fact(5)
# output = 34560

fact_of_fact(6)
# output = 24883200
