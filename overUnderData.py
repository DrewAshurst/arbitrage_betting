import csv
import requests
import json
import calculations2

def getData(url):
    url = url
    response = requests.get(url)
    responseContent = response.content
    a = json.loads(responseContent) 

    return a

def compilePointsData(url):
    initialData = getData(url)
    compiledData = {}
    
    for game in initialData:
        if game in ['message', []]:
            continue
    
        home_team = game['home_team']
        away_team = game['away_team']
        gameMatchup = f"{home_team} vs {away_team}"
        sport = game['sport_key']
        compiledData[gameMatchup] = {"sport": sport,
                    "overOffers":{},
                    "underOffers": {}}
        sportsbook_offers = game['bookmakers']
        if len(sportsbook_offers) == 0:
            continue
        total = str(sportsbook_offers[0]['markets'][0]['outcomes'][0]['point'])
        

        overOffers = {}
        underOffers = {}
        overOffers[total] = {}
        underOffers[total] = {}
        for listing in sportsbook_offers:
            outcomes = listing['markets'][0]['outcomes']
            for outcome in outcomes:
                if outcome['name'] == 'Over':
                    overOffers[total][listing['key']] = outcome['price']
                if outcome['name'] == 'Under':
                    underOffers[total][listing['key']] = outcome['price']
        compiledData[gameMatchup]['overOffers'].update(overOffers)
        compiledData[gameMatchup]['underOffers'].update(underOffers)
        
            


    return compiledData

def cleanData(url, betIncrement):
    dirtyData = compilePointsData(url)
    keys = list(dirtyData.keys())
    bets = {}
    for key in keys:

        if len(dirtyData[key]['overOffers'].values()) == 0 or len(dirtyData[key]['underOffers'].values()) == 0:
            dirtyData.pop(key)
        
    for key in dirtyData.keys():
        over_offers = dirtyData[key]['overOffers']
        under_offers = dirtyData[key]['underOffers']
        
        for total in list(over_offers.keys()):

            overOdds = list(over_offers[total].values())
            underOdds = list(under_offers[total].values())
            
            bestBet = calculations2.findBestBet(overOdds, underOdds)

        
            if bestBet == [1, 1]:
                continue

            bettingAmounts, profits = calculations2.optimalBet(betIncrement, bestBet[0], bestBet[1])
            if not profits:
                continue 

            bets['Game'] = key
            bets['Sport'] = dirtyData[key].get('sport')
            bets['Total'] = total 
            bets['Over Odds'] = bestBet[0]
            bets['Under Odds'] = bestBet[1]

            bets['Over Odds'] = bestBet[0]
            bets['Under Odds'] = bestBet[1]

            bets['Over Bet'] = "$" + '{:,.2f}'.format(bettingAmounts[0])
            bets['Under Bet'] = "$" + '{:,.2f}'.format(bettingAmounts[1])
        
            bets['Over Profit'] = "$" + '{:,.2f}'.format(profits[0])
            bets['Under Profit'] = "$" + '{:,.2f}'.format(profits[1]) 

            bets['Over Sportsbook'] = []
            bets['Under Sportsbook'] = []

            for key in list(over_offers[total].keys()):
                if over_offers[total][key] == bestBet[0]:
                    bets['Over Sportsbook'].append(key)

            for key in list(under_offers[total].keys()):
                if under_offers[total][key] == bestBet[1]:
                    bets['Under Sportsbook'].append(key)

    return bets


def writeToCsv(data):
    with open('overUnderBets.csv', 'w', newline='') as csv_file:
        w = csv.DictWriter(csv_file, data[0].keys())
        w.writeheader()
        for i in data:
            w.writerow(i)