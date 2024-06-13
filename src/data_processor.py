import pandas as pd

def process_data(df):
    "Process raw data to extract relevant columns and features."
    df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HST', 'AST', 'HBP', 'ABP', 'B365H', 'B365D', 'B365A']]
    df.columns = ['Date', 'HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals', 'FullTimeResult', 'HomeShotsOnTarget', 'AwayShotsOnTarget', 'HomeBooking', 'AwayBooking', 'HomeWinOdds', 'DrawOdds', 'AwayWinOdds']
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    return df

def add_match_outcomes(df):
    """Add match outcome columns to the DataFrame."""
    df['HomeWin'] = df['FullTimeResult'] == 'H'
    df['AwayWin'] = df['FullTimeResult'] == 'A'
    df['Draw'] = df['FullTimeResult'] == 'D'
    return df
