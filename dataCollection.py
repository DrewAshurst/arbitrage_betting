import requests
from bs4 import BeautifulSoup
import csv
import outputParser

fullOut = [{"id":"98235f33b2e4e22ef073588d0c3af6d8","sport_key":"americanfootball_nfl","sport_title":"NFL","commence_time":"2023-02-12T23:35:00Z","home_team":"Philadelphia Eagles","away_team":"Kansas City Chiefs","bookmakers":[{"key":"draftkings","title":"DraftKings","last_update":"2023-02-06T05:12:27Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:27Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"barstool","title":"Barstool Sportsbook","last_update":"2023-02-06T05:15:25Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:15:25Z","outcomes":[{"name":"Kansas City Chiefs","price":100},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"twinspires","title":"TwinSpires","last_update":"2023-02-06T05:12:53Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:53Z","outcomes":[{"name":"Kansas City Chiefs","price":100},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"sugarhouse","title":"SugarHouse","last_update":"2023-02-06T05:07:29Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:07:29Z","outcomes":[{"name":"Kansas City Chiefs","price":108},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"unibet_us","title":"Unibet","last_update":"2023-02-06T05:15:25Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:15:25Z","outcomes":[{"name":"Kansas City Chiefs","price":100},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"pointsbetus","title":"PointsBet (US)","last_update":"2023-02-06T05:12:27Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:27Z","outcomes":[{"name":"Kansas City Chiefs","price":100},{"name":"Philadelphia Eagles","price":-120}]}]},{"key":"betmgm","title":"BetMGM","last_update":"2023-02-06T05:13:55Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:13:55Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"fanduel","title":"FanDuel","last_update":"2023-02-06T05:12:32Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:32Z","outcomes":[{"name":"Kansas City Chiefs","price":104},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"betus","title":"BetUS","last_update":"2023-02-06T05:12:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:33Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"williamhill_us","title":"William Hill (US)","last_update":"2023-02-06T05:15:08Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:15:08Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"betrivers","title":"BetRivers","last_update":"2023-02-06T05:12:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:33Z","outcomes":[{"name":"Kansas City Chiefs","price":108},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"lowvig","title":"LowVig.ag","last_update":"2023-02-06T05:15:42Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:15:42Z","outcomes":[{"name":"Kansas City Chiefs","price":106},{"name":"Philadelphia Eagles","price":-126}]}]},{"key":"wynnbet","title":"WynnBET","last_update":"2023-02-06T05:12:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:33Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"betonlineag","title":"BetOnline.ag","last_update":"2023-02-06T05:15:34Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:15:34Z","outcomes":[{"name":"Kansas City Chiefs","price":106},{"name":"Philadelphia Eagles","price":-127}]}]},{"key":"superbook","title":"SuperBook","last_update":"2023-02-06T05:12:54Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:54Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"mybookieag","title":"MyBookie.ag","last_update":"2023-02-06T05:14:55Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:14:55Z","outcomes":[{"name":"Kansas City Chiefs","price":106},{"name":"Philadelphia Eagles","price":-130}]}]},{"key":"circasports","title":"Circa Sports","last_update":"2023-02-06T05:15:25Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:15:25Z","outcomes":[{"name":"Kansas City Chiefs","price":101},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"bovada","title":"Bovada","last_update":"2023-02-06T05:14:23Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:14:23Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"foxbet","title":"FOX Bet","last_update":"2023-02-06T05:12:27Z","markets":[{"key":"h2h","last_update":"2023-02-06T05:12:27Z","outcomes":[{"name":"Kansas City Chiefs","price":110},{"name":"Philadelphia Eagles","price":-133}]}]}]}]


def createCsv():
    games = outputParser.parseOutput(fullOut)
    with open('outputCSV.csv', 'w') as csvfile:
        fieldnames = ['book', 'game', 'team1', 'team1price','team2', 'team2price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(games)


def getData():
    url = 'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=1268ceecd3baff09507cfb926d3ce10c&regions=us&markets=h2h&oddsFormat=american'
    response = requests.get(url)
    responseContent = response.content
    responseText = BeautifulSoup(responseContent, 'html.parser')
    parseText = responseText.get_text()


    return parseText






    



