import outputParser3
import os 
import keyboard
import overUnderData

print("Gathering data now...")

with open('sports.txt', 'r') as f:
        lines = [i.split() for i in f.readlines()]
        sports = [i[len(i) - 1] for i in lines]
with open('Config.txt', 'r') as f:
    lines = [i.strip() for i in f.readlines()]
    APIKEY = lines[0]
    BETINCREMENT = float(lines[1])

def dataVisLoop():
    pass

def main():
    dataMoneyLine = []
    dataTotal = []
    count = 0
    for i in sports:
        if 'soccer' not in i:
            urlMoneyline = f'https://api.the-odds-api.com/v4/sports/{i}/odds/?apiKey={APIKEY}&regions=us&markets=h2h&oddsFormat=american'
            urlTotal = f'https://api.the-odds-api.com/v4/sports/{i}/odds/?apiKey={APIKEY}&regions=us&markets=totals&oddsFormat=american'
            betIncrement = BETINCREMENT

            sportMoneyline = outputParser3.cleanData(urlMoneyline, betIncrement)
            sportTotal = overUnderData.cleanData(urlTotal, betIncrement)
        else:
            urlTotal = f'https://api.the-odds-api.com/v4/sports/{i}/odds/?apiKey={APIKEY}&regions=us&markets=totals&oddsFormat=american'
            betIncrement = BETINCREMENT

            sportMoneyline = {}
            sportTotal = overUnderData.cleanData(urlTotal, betIncrement)

        
        if sportMoneyline != {}:
            dataMoneyLine.append(sportMoneyline)

            
        if sportTotal != {}:
            dataTotal.append(sportTotal)
            
    if len(dataMoneyLine) > 0:
        print(len(dataMoneyLine), "money line bets found.")
        outputParser3.writeToCsv(dataMoneyLine)
        os.startfile('possibleBets.csv')
    if len(dataTotal) > 0:
        print(len(dataTotal), "over under bets found.")
        overUnderData.writeToCsv(dataTotal)
        os.startfile('overUnderBets.csv')
    else:
        print("No bets found")

main()

