def findBestBet(homeList, awayList):
    bestBet = []
    for x in homeList:
        for y in awayList:
            decimalOddsHome = moneyToDecimal(x)
            decimalOddsAway = moneyToDecimal(y) 
            if (1/decimalOddsHome) + (1/decimalOddsAway) <= 1 and [x,y] not in bestBet:
                bestBet.append([x, y])

    

    return bestBet

def moneyToDecimal(num):
    if num > 0:
        odds = 1 + (num / 100)

    else:
        odds = 1 - (100 / num)

    return odds 

def optimalBet(betIncrement, homeOdds, awayOdds):
    homeOdds = moneyToDecimal(homeOdds)
    awayOdds = moneyToDecimal(awayOdds)


    homeArbPercent = (1/homeOdds)
    awayArbPercent = (1/awayOdds)

    totalArbPercent = homeArbPercent + awayArbPercent

    if homeOdds > awayOdds:
        homeBet = round(betIncrement * (awayOdds / homeOdds))
        # awayBet = round(betIncrement * (awayOdds / homeOdds))
        awayBet = betIncrement
    elif awayOdds > homeOdds:
        awayBet = round(betIncrement * (homeOdds / awayOdds))
        homeBet = betIncrement
    else:
        homeBet = 0
        awayBet = 0
    

    homeProfit = (homeBet * homeOdds) - (homeBet + awayBet)
    awayProfit = (awayBet * awayOdds) - (homeBet + awayBet)
    
    if homeProfit > 0 and awayProfit > 0:
        profit = [homeProfit, awayProfit]

    else:
        profit = False


    return [homeBet, awayBet], profit

def calcProfit(homeBet, homeOdds, awayBet, awayOdds):
    homeProfit = (homeBet * homeOdds) - homeBet - awayBet
    awayProfit = (awayBet * awayOdds) - awayBet - homeBet
    
    if homeProfit > 0 and awayProfit > 0:

        return [homeProfit, awayProfit]
    else:
        return False
