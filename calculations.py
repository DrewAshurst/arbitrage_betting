def moneyToDecimal(num):
    if num > 0:
        odds = 1 + (num / 100)

    else:
        odds = 1 - (100 / num)

    return odds 

def betCalc():
    betIncrement = 5
    odd1 = int(input("Enter positive odds: "))
    odd2 = int(input("Enter negative odds: ")) * -1
    pos = moneyToDecimal(odd1)
    neg = moneyToDecimal(odd2)
    
    posProfit = (betIncrement * pos) - betIncrement 
    
    initNegBet = (betIncrement / 100) * (float(odd2) * -1)
    value = 0
    minDif = 999
    while initNegBet < posProfit:
        if abs(((initNegBet * neg) - initNegBet - betIncrement) - (posProfit - initNegBet)) < minDif:
            minDif = abs(((initNegBet * neg) - initNegBet - betIncrement) - (posProfit - initNegBet))
            value = initNegBet

        
        initNegBet += 0.01

    print(value)

while True:
    betCalc()