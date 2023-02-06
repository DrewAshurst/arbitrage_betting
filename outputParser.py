import csv


def parseOutput():
    out = [{"id":"98235f33b2e4e22ef073588d0c3af6d8","sport_key":"americanfootball_nfl","sport_title":"NFL","commence_time":"2023-02-12T23:35:00Z","home_team":"Philadelphia Eagles","away_team":"Kansas City Chiefs","bookmakers":[{"key":"draftkings","title":"DraftKings","last_update":"2023-02-06T03:41:44Z","markets":[{"key":"h2h","last_update":"2023-02-06T03:41:44Z","outcomes":[{"name":"Kansas City Chiefs","price":105},{"name":"Philadelphia Eagles","price":-125}]}]},{"key":"barstool","title":"Barstool Sportsbook","last_update":"2023-02-06T03:41:18Z","markets":[{"key":"h2h","last_update":"2023-02-06T03:41:18Z","outcomes":[{"name":"Kansas City Chiefs","price":100},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"twinspires","title":"TwinSpires","last_update":"2023-02-06T03:42:07Z","markets":[{"key":"h2h","last_update":"2023-02-06T03:42:07Z","outcomes":[{"name":"Kansas City Chiefs","price":100},{"name":"Philadelphia Eagles","price":-122}]}]},{"key":"sugarhouse","title":"SugarHouse","last_update":"2023-02-06T03:41:52Z","markets":[{"key":"h2h","last_update":"2023-02-06T03:41:52Z","outcomes":[{"name":"Kansas City Chiefs","price":108},{"name":"Philadelphia Eagles","price":-122}]}]}]}]



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

games = parseOutput()
with open('outputCSV.csv', 'w') as csvfile:
    fieldnames = ['book', 'game', 'team1', 'team1price','team2', 'team2price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(games)