import pandas as pd
import calculations


def findBestBets(df):

    pd.to_numeric(df['team1price'])
    pd.to_numeric(df['team2price'])

    team1PricingPos = [i for i in df['team1price'] if i > 0]
    team1PricingNeg = [i for i in df['team1price'] if i < 0]
    team2PricingPos = [i for i in df['team2price'] if i > 0]
    team2PricingNeg = [i for i in df['team2price'] if i < 0]

    if team1PricingPos == [] and team1PricingNeg == []:
        team1pricing = [0, 0]
    elif team1PricingPos == []:
        team1pricing = [min(team1PricingNeg), 0]
    elif team1PricingNeg == []:
        team1pricing = [0, max(team1PricingPos)]
    else:
        team1pricing = [min(team1PricingNeg), max(team1PricingPos)]

    if team2PricingPos == [] and team2PricingNeg == []:
        team2pricing = [0, 0]
    elif team2PricingPos == []:
        team2pricing = [min(team2PricingNeg), 0]
    elif team2PricingNeg == []:
        team2pricing = [0, max(team2PricingPos)]
    else:
        team2pricing = [min(team2PricingNeg), max(team2PricingPos)]

    if team1pricing[1] > 0 and team2pricing[1] > 0:
        df1 = df.loc[df['team1price'] == team1pricing[1]]
        df2 = df.loc[df['team2price'] == team2pricing[1]]
    elif team1pricing[1] > 0 and team2pricing[0] < 0:
        df1 = df.loc[df['team1price'] == team1pricing[1]]
        df2 = df.loc[df['team2price'] == team2pricing[0]]
    elif team1pricing[0] < 0 and team2pricing[1] > 0:
        df1 = df.loc[df['team1price'] == team1pricing[0]]
        df2 = df.loc[df['team2price'] == team2pricing[1]]
    else:
        df1 = df.loc[df['team1price'] == team1pricing[0]]
        df2 = df.loc[df['team2price'] == team2pricing[0]]

    first = f"First bet is for {df1['team1'].values[0]} at {df1['team1price'].values[0]} on {df1['book'].values[0]}."
    second = f"Second bet is for {df2['team2'].values[0]} at {df2['team2price'].values[0]} on {df2['book'].values[0]}."

    return df1, df2


def findGames():
    data = {}
    betIncrement = 1
    df = pd.read_csv('outputCSV.csv')
    games = df['game'].unique()
    for i in games:
        df1, df2 = findBestBets(df.loc[df['game'] == i])
        data[i] = {'team1':df1['team1'].values[0], 'team2': df2['team2'].values[0],
                   'team1odds': df1['team1price'].values[0], 'team2odds': df2['team2price'].values[0],
                   'team1book': df1['book'].values[0], 'team2book': df2['book'].values[0]}
        
        if data[i]['team1odds'] > 0:
            data[i]['team1bet'] = betIncrement
            data[i]['team2bet'] = calculations.betCalc(data[i]['team1odds'], data[i]['team2odds'], betIncrement)
            data[i]['team1profit'], data[i]['team2profit'] = calculations.profitCalc(data[i]['team1odds'], data[i]['team1bet'], data[i]['team2odds'], data[i]['team2bet'])

    return data 
