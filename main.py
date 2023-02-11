import outputParser3
import os 

print("Gathering data now... let's get weird")


with open('sports.txt', 'r') as f:
        lines = [i.split() for i in f.readlines()]
        sports = [i[len(i) - 1] for i in lines]
with open('Config.txt', 'r') as f:
    lines = [i.strip() for i in f.readlines()]
    APIKEY = lines[0]
    BETINCREMENT = float(lines[1])


def main():
    #dataCollection.createCsv()
    

    data = []
    count = 0
    for i in sports:
        url = f'https://api.the-odds-api.com/v4/sports/{i}/odds/?apiKey={APIKEY}&regions=us&markets=h2h&oddsFormat=american'
        betIncrement = BETINCREMENT

        sport = outputParser3.cleanData(url, betIncrement)
        
        if sport != {}:
            data.append(sport)
        
        if count == 5:
            print(f"""{len(data)} possible bets found. 
            Why is every poo-poo time pee-pee time, 
            but not every pee-pee time is poo-poo time?""")
        count += 1
    
    if len(data) > 0:
        outputParser3.writeToCsv(data)
        
        os.startfile('possibleBets.csv')
    else:
        print("No bets found")
    
    

main()

