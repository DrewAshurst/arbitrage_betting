import pandas as pd


def findBestBets():
    df = pd.read_csv('outputCSV.csv')
    df['team1price'] = pd.to_numeric(df['team1price'])
    df['team2price'] = pd.to_numeric(df['team2price'])

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

    first = f"First bet is for {df1['team1'].values} at {df1['team1price'].values} on {df1['book'].values}."
    second = f"Second bet is for {df2['team2'].values} at {df2['team2price'].values} on {df2['book'].values}."











    return [first, second]