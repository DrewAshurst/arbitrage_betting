import csv
import requests
import json
import calculations2

def getData(url):
    url = url
    response = requests.get(url)
    if 'soccer_usa_mls' in url:
        print('Remaining requests', response.headers['x-requests-remaining'])
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
                    "underOffers": {},
                    "Date of Event": game['commence_time']}
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
    myaccounts = ['betus', 'draftkings', 'fanduel', 'sugarhouse']
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

        
            if bestBet == []:
                continue
            
            for bet in bestBet:
                bettingAmounts, profits = calculations2.optimalBet(betIncrement, bet[0], bet[1])
                if not profits:
                    continue 
                
                bets['Game'] = key
                bets['Sport'] = dirtyData[key]['sport']
                bets['Total'] = total 
                bets['Over Odds'] = bet[0]
                bets['Under Odds'] = bet[1]

                bets['Over Odds'] = bet[0]
                bets['Under Odds'] = bet[1]

                bets['Over Bet'] = "$" + '{:,.2f}'.format(bettingAmounts[0])
                bets['Under Bet'] = "$" + '{:,.2f}'.format(bettingAmounts[1])
            
                bets['Over Profit'] = "$" + '{:,.2f}'.format(profits[0])
                bets['Under Profit'] = "$" + '{:,.2f}'.format(profits[1]) 

                bets['Over Sportsbook'] = []
                bets['Under Sportsbook'] = []

                bets['Date of Event'] = dirtyData[key]['Date of Event']

                for key1 in list(over_offers[total].keys()):
                    if over_offers[total][key1] == bet[0] and key1 in myaccounts:
                        bets['Over Sportsbook'].append(key1)
                for key2 in list(under_offers[total].keys()):
                    if under_offers[total][key2] == bet[1] and key2 in myaccounts:
                        bets['Under Sportsbook'].append(key2)
                
                if bets['Over Sportsbook'] == [] or bets['Under Sportsbook'] == []:
                    return {}

    return bets


def writeToCsv(data):
    with open('overUnderBets.csv', 'w', newline='') as csv_file:
        w = csv.DictWriter(csv_file, data[0].keys())
        w.writeheader()
        for i in data:
            w.writerow(i)