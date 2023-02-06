import csv
import requests
from bs4 import BeautifulSoup
out = [{"id":"1ab961f9f82235240b8002931aba5539","sport_key":"basketball_ncaab","sport_title":"NCAAB","commence_time":"2023-02-06T22:00:00Z","home_team":"UT-Arlington Mavericks","away_team":"Tarleton State Texans","bookmakers":[{"key":"draftkings","title":"DraftKings","last_update":"2023-02-06T18:58:15Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:15Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"betonlineag","title":"BetOnline.ag","last_update":"2023-02-06T18:59:18Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:18Z","outcomes":[{"name":"Tarleton State Texans","price":-123},{"name":"UT-Arlington Mavericks","price":102}]}]},{"key":"bovada","title":"Bovada","last_update":"2023-02-06T18:59:46Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:46Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"williamhill_us","title":"William Hill (US)","last_update":"2023-02-06T18:58:15Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:15Z","outcomes":[{"name":"Tarleton State Texans","price":-130},{"name":"UT-Arlington Mavericks","price":110}]}]},{"key":"lowvig","title":"LowVig.ag","last_update":"2023-02-06T18:58:20Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:20Z","outcomes":[{"name":"Tarleton State Texans","price":-123},{"name":"UT-Arlington Mavericks","price":103}]}]},{"key":"betus","title":"BetUS","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"wynnbet","title":"WynnBET","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"pointsbetus","title":"PointsBet (US)","last_update":"2023-02-06T18:59:46Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:46Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"betmgm","title":"BetMGM","last_update":"2023-02-06T19:00:03Z","markets":[{"key":"h2h","last_update":"2023-02-06T19:00:03Z","outcomes":[{"name":"Tarleton State Texans","price":-120},{"name":"UT-Arlington Mavericks","price":100}]}]},{"key":"circasports","title":"Circa Sports","last_update":"2023-02-06T18:57:34Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:34Z","outcomes":[{"name":"Tarleton State Texans","price":-132},{"name":"UT-Arlington Mavericks","price":109}]}]},{"key":"superbook","title":"SuperBook","last_update":"2023-02-06T18:57:34Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:34Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"twinspires","title":"TwinSpires","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Tarleton State Texans","price":-127},{"name":"UT-Arlington Mavericks","price":104}]}]},{"key":"unibet_us","title":"Unibet","last_update":"2023-02-06T18:59:18Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:18Z","outcomes":[{"name":"Tarleton State Texans","price":-127},{"name":"UT-Arlington Mavericks","price":104}]}]},{"key":"barstool","title":"Barstool Sportsbook","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"sugarhouse","title":"SugarHouse","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"betrivers","title":"BetRivers","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Tarleton State Texans","price":-125},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"fanduel","title":"FanDuel","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Tarleton State Texans","price":-128},{"name":"UT-Arlington Mavericks","price":106}]}]},{"key":"foxbet","title":"FOX Bet","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Tarleton State Texans","price":-143},{"name":"UT-Arlington Mavericks","price":105}]}]},{"key":"mybookieag","title":"MyBookie.ag","last_update":"2023-02-06T19:00:05Z","markets":[{"key":"h2h","last_update":"2023-02-06T19:00:05Z","outcomes":[{"name":"Tarleton State Texans","price":-128},{"name":"UT-Arlington Mavericks","price":105}]}]}]},{"id":"561c0270d79c812011f60dea3aa2a5a7","sport_key":"basketball_ncaab","sport_title":"NCAAB","commence_time":"2023-02-06T23:00:00Z","home_team":"Hartford Hawks","away_team":"UMass Lowell River Hawks","bookmakers":[{"key":"draftkings","title":"DraftKings","last_update":"2023-02-06T18:58:15Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:15Z","outcomes":[{"name":"Hartford Hawks","price":900},{"name":"UMass Lowell River Hawks","price":-1700}]}]},{"key":"williamhill_us","title":"William Hill (US)","last_update":"2023-02-06T18:58:15Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:15Z","outcomes":[{"name":"Hartford Hawks","price":900},{"name":"UMass Lowell River Hawks","price":-1600}]}]},{"key":"pointsbetus","title":"PointsBet (US)","last_update":"2023-02-06T18:59:46Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:46Z","outcomes":[{"name":"Hartford Hawks","price":900},{"name":"UMass Lowell River Hawks","price":-1600}]}]},{"key":"twinspires","title":"TwinSpires","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Hartford Hawks","price":1000},{"name":"UMass Lowell River Hawks","price":-2500}]}]},{"key":"unibet_us","title":"Unibet","last_update":"2023-02-06T18:59:18Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:18Z","outcomes":[{"name":"Hartford Hawks","price":1000},{"name":"UMass Lowell River Hawks","price":-2500}]}]},{"key":"barstool","title":"Barstool Sportsbook","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Hartford Hawks","price":1000},{"name":"UMass Lowell River Hawks","price":-2500}]}]},{"key":"sugarhouse","title":"SugarHouse","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Hartford Hawks","price":1000},{"name":"UMass Lowell River Hawks","price":-2500}]}]},{"key":"betrivers","title":"BetRivers","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Hartford Hawks","price":1000},{"name":"UMass Lowell River Hawks","price":-2500}]}]},{"key":"bovada","title":"Bovada","last_update":"2023-02-06T18:59:46Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:46Z","outcomes":[{"name":"Hartford Hawks","price":850},{"name":"UMass Lowell River Hawks","price":-1800}]}]},{"key":"betus","title":"BetUS","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Hartford Hawks","price":910},{"name":"UMass Lowell River Hawks","price":-1700}]}]},{"key":"fanduel","title":"FanDuel","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Hartford Hawks","price":920},{"name":"UMass Lowell River Hawks","price":-1800}]}]},{"key":"foxbet","title":"FOX Bet","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Hartford Hawks","price":650},{"name":"UMass Lowell River Hawks","price":-1667}]}]},{"key":"wynnbet","title":"WynnBET","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Hartford Hawks","price":950},{"name":"UMass Lowell River Hawks","price":-2000}]}]},{"key":"superbook","title":"SuperBook","last_update":"2023-02-06T18:57:34Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:34Z","outcomes":[{"name":"Hartford Hawks","price":900},{"name":"UMass Lowell River Hawks","price":-1600}]}]},{"key":"mybookieag","title":"MyBookie.ag","last_update":"2023-02-06T19:00:05Z","markets":[{"key":"h2h","last_update":"2023-02-06T19:00:05Z","outcomes":[{"name":"Hartford Hawks","price":789},{"name":"UMass Lowell River Hawks","price":-1428}]}]},{"key":"betmgm","title":"BetMGM","last_update":"2023-02-06T19:00:03Z","markets":[{"key":"h2h","last_update":"2023-02-06T19:00:03Z","outcomes":[{"name":"Hartford Hawks","price":775},{"name":"UMass Lowell River Hawks","price":-1400}]}]}]},{"id":"001978ed51d5bbe8e6e2432ae9b9fea0","sport_key":"basketball_ncaab","sport_title":"NCAAB","commence_time":"2023-02-07T00:00:00Z","home_team":"Miami Hurricanes","away_team":"Duke Blue Devils","bookmakers":[{"key":"draftkings","title":"DraftKings","last_update":"2023-02-06T18:58:15Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:15Z","outcomes":[{"name":"Duke Blue Devils","price":145},{"name":"Miami Hurricanes","price":-170}]}]},{"key":"williamhill_us","title":"William Hill (US)","last_update":"2023-02-06T18:58:15Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:15Z","outcomes":[{"name":"Duke Blue Devils","price":143},{"name":"Miami Hurricanes","price":-170}]}]},{"key":"lowvig","title":"LowVig.ag","last_update":"2023-02-06T18:58:20Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:58:20Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-155}]}]},{"key":"betonlineag","title":"BetOnline.ag","last_update":"2023-02-06T18:59:18Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:18Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-156}]}]},{"key":"bovada","title":"Bovada","last_update":"2023-02-06T18:59:46Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:46Z","outcomes":[{"name":"Duke Blue Devils","price":140},{"name":"Miami Hurricanes","price":-165}]}]},{"key":"betus","title":"BetUS","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Duke Blue Devils","price":140},{"name":"Miami Hurricanes","price":-160}]}]},{"key":"wynnbet","title":"WynnBET","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-159}]}]},{"key":"betmgm","title":"BetMGM","last_update":"2023-02-06T19:00:03Z","markets":[{"key":"h2h","last_update":"2023-02-06T19:00:03Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-165}]}]},{"key":"pointsbetus","title":"PointsBet (US)","last_update":"2023-02-06T18:59:46Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:46Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-160}]}]},{"key":"circasports","title":"Circa Sports","last_update":"2023-02-06T18:57:34Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:34Z","outcomes":[{"name":"Duke Blue Devils","price":133},{"name":"Miami Hurricanes","price":-164}]}]},{"key":"superbook","title":"SuperBook","last_update":"2023-02-06T18:57:34Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:34Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-155}]}]},{"key":"twinspires","title":"TwinSpires","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Duke Blue Devils","price":133},{"name":"Miami Hurricanes","price":-162}]}]},{"key":"unibet_us","title":"Unibet","last_update":"2023-02-06T18:59:18Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:18Z","outcomes":[{"name":"Duke Blue Devils","price":133},{"name":"Miami Hurricanes","price":-162}]}]},{"key":"barstool","title":"Barstool Sportsbook","last_update":"2023-02-06T18:59:17Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:59:17Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-159}]}]},{"key":"sugarhouse","title":"SugarHouse","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-159}]}]},{"key":"betrivers","title":"BetRivers","last_update":"2023-02-06T18:57:33Z","markets":[{"key":"h2h","last_update":"2023-02-06T18:57:33Z","outcomes":[{"name":"Duke Blue Devils","price":135},{"name":"Miami Hurricanes","price":-159}]}]},{"key":"mybookieag","title":"MyBookie.ag","last_update":"2023-02-06T19:00:05Z","markets":[{"key":"h2h","last_update":"2023-02-06T19:00:05Z","outcomes":[{"name":"Duke Blue Devils","price":119},{"name":"Miami Hurricanes","price":-147}]}]}]}]

def getData():
    url = 'https://api.the-odds-api.com/v4/sports/basketball_ncaab/odds/?apiKey=1268ceecd3baff09507cfb926d3ce10c&regions=us&markets=h2h&oddsFormat=american'
    response = requests.get(url)
    responseContent = response.content
    responseText = BeautifulSoup(responseContent, 'html.parser')
    print(type(responseText))
    parseText = responseText.get_text()

    return parseText


def parseOutput(out):
    # books = out[0]['bookmakers']

    games = []
    for i in out:
        books = i['bookmakers']

        for j in books:
            data = {}
            offers = j['markets'][0]['outcomes']

            team1 = offers[0]['name']
            team2 = offers[1]['name']
            data['book'] = j['key']
            data['game'] = f"{team1} vs {team2}"
            data['team1'] = offers[0]['name']
            data['team1price'] = offers[0]['price']
            data['team2'] = offers[1]['name']
            data['team2price'] = offers[1]['price']

            games.append(data)

    return games