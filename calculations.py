def moneyToDecimal(num):
    if num > 0:
        odds = 1 + (num / 100)

    else:
        odds = 1 - (100 / num)

    return odds 

def betCalc(o1, o2, increment):
    betIncrement = increment

    if o1 > 0:

        odd1 = o1
        odd2 = o2
    else:
        odd2 = o1 
        odd1 = o2
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

    return value

def profitCalc(odd1, bet1, odd2, bet2):
    team1profit = (bet1 * moneyToDecimal(odd1)) - bet1 - bet2 
    team2profit = (bet2 * moneyToDecimal(odd2)) - bet1 - bet2
    return team1profit, team2profit