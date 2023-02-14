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



def compileData(url):
    initialData = getData(url)
    compiledData = {}
    for game in initialData:
        if game == 'message':
            continue
        home_team = game['home_team']
        away_team = game['away_team']
        gameMatchup = f"{home_team} vs {away_team}"
        sport = game['sport_key']
        compiledData[gameMatchup] = {"sport": sport,
                    "homeOffers":{},
                    "awayOffers": {},
                    "Date of Event": game['commence_time']}
    
        sportsbook_offers = game['bookmakers']

        for offer in sportsbook_offers:
            sportsbook = offer['key']

            allOffers = offer['markets'][0]['outcomes']
            for element in allOffers:
                if element['name'] == home_team:
                    compiledData[gameMatchup]['homeOffers'][sportsbook] = element['price'] 
                elif element['name'] == away_team:
                    compiledData[gameMatchup]['awayOffers'][sportsbook] = element['price'] 

    return compiledData

def cleanData(url, betIncrement):
    dirtyData = compileData(url)
    keys = list(dirtyData.keys())
    bets = {}
    myaccounts = ['betus', 'draftkings', 'fanduel', 'sugarhouse']
    canPlace = False
    for key in keys:

        if len(dirtyData[key]['homeOffers'].values()) == 0 or len(dirtyData[key]['awayOffers'].values()) == 0:
            dirtyData.pop(key)

    for key in dirtyData.keys():
        home_offers = list(dirtyData[key]['homeOffers'].values())
        away_offers = list(dirtyData[key]['awayOffers'].values())


        bestBet = calculations2.findBestBet(home_offers, away_offers)
        if bestBet == []:
            continue
        
        for bet in bestBet:
            bettingAmounts, profits = calculations2.optimalBet(betIncrement, bet[0], bet[1])
            if not profits:
                continue 


            
    
            bets['Game'] = key
            bets['Sport'] = dirtyData[key].get('sport')

            bets['Home Team'] = key.split(' vs ')[0]
            bets['Away Team'] = key.split(' vs ')[1]
            bets['Home Odds'] = bet[0]
            bets['Away Odds'] = bet[1]

        
        

            bets['Home Bet'] = bettingAmounts[0]
            bets['Away Bet'] = bettingAmounts[1]
            
            bets['Home Profit'] = "$" + '{:,.2f}'.format(profits[0])
            bets['Away Profit'] = "$" + '{:,.2f}'.format(profits[1])
            
            bets['Home Sports Books'] = []
            for key1 in dirtyData[key]['homeOffers'].keys():
                if dirtyData[key]['homeOffers'][key1] == bet[0] and key1 in myaccounts:
                    bets['Home Sports Books'].append(key1)

            bets['Away Sports Books'] = []
            for key2 in dirtyData[key]['awayOffers'].keys():
                if dirtyData[key]['awayOffers'][key2] == bet[1] and key2 in myaccounts:
                    bets['Away Sports Books'].append(key2)
            if bets['Home Sports Books'] == [] or bets['Away Sports Books'] == []:
                return {}
            
            bets['Date of Event'] = dirtyData[key]['Date of Event']
    return bets
        
def writeToCsv(data):
    with open('possibleBets.csv', 'w', newline='') as csv_file:
        w = csv.DictWriter(csv_file, data[0].keys())
        w.writeheader()
        for i in data:
            w.writerow(i)
