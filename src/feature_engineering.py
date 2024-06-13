import pandas as pd

def calculate_team_form(df, team, num_matches=5):
    team_matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)] #get matches that team is playing in
    team_matches = team_matches.sort_values(by='Date', ascending=False).head(num_matches)
    
    team_matches['Points'] = team_matches.apply(
        lambda row: 3 if (row['HomeTeam'] == team and row['HomeWin']) or (row['AwayTeam'] == team and row['AwayWin'])
        else 1 if row['Draw']
        else 0,
        axis=1
    )
    return team_matches['Points'].sum()

def calculate_avg_scored(df, team, num_matches=5):
    team_matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)] #get matches that team is playing in
    team_matches = team_matches.sort_values(by='Date', ascending=False).head(num_matches)

    goals_scored = 0
    for index, row in team_matches.iterrows():
        if row['HomeTeam'] == team:
            goals_scored += row['HomeGoals']
        else:
            goals_scored += row['AwayGoals']
    
    avg_scored = goals_scored / num_matches
    return avg_scored

def calculate_avg_conceded(df, team, num_matches=5):
    team_matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)] #get matches that team is playing in
    team_matches = team_matches.sort_values(by='Date', ascending=False).head(num_matches)

    goals_conceded = 0
    for index, row in team_matches.iterrows():
        if row['HomeTeam'] == team:
            goals_conceded += row['AwayGoals']
        else:
            goals_conceded += row['HomeGoals']
    
    avg_condeded = goals_conceded / num_matches
    return avg_condeded

def add_avg_scored(df, num_matches=5):
    """Add average goals scored columns to the DataFrame."""
    df['AvgHomeScored'] = df.apply(lambda row: calculate_avg_scored(df, row['HomeTeam'], num_matches), axis=1)
    df['AvgAwayScored'] = df.apply(lambda row: calculate_avg_scored(df, row['AwayTeam'], num_matches), axis=1)
    return df

def add_avg_condeded(df, num_matches=5):
    """Add average goals scored columns to the DataFrame."""
    df['AvgHomeConceded'] = df.apply(lambda row: calculate_avg_conceded(df, row['HomeTeam'], num_matches), axis=1)
    df['AvgAwayConceded'] = df.apply(lambda row: calculate_avg_conceded(df, row['AwayTeam'], num_matches), axis=1)
    return df

