import pandas as pd

def process_data(df):
    "Process raw data to extract relevant columns and features."
    df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
    df.columns = ['Date', 'HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals', 'FullTimeResult']
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    return df
