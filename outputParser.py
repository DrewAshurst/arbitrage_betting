import csv
import requests 
from bs4 import BeautifulSoup

def getData():
    url = 'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=1268ceecd3baff09507cfb926d3ce10c&regions=us&markets=h2h&oddsFormat=american'
    response = requests.get(url)
    responseContent = response.content
    responseText = BeautifulSoup(responseContent, 'html.parser')
    print(type(responseText))
    parseText = responseText.get_text()


    return parseText

def parseOutput(out):
    books = out[0]['bookmakers']

    games = []
    for i in books:
        data = {}
        offers = i['markets'][0]['outcomes']

        team1 = offers[0]['name']
        team2 = offers[1]['name']
        data['book'] = i['key']
        data['game'] = f"{team1} vs {team2}"
        data['team1'] = offers[0]['name']
        data['team1price'] = offers[0]['price']
        data['team2'] = offers[1]['name']
        data['team2price'] = offers[1]['price']

        games.append(data)

    return games

# data = getData()
# print(data)
# print(type(data))




