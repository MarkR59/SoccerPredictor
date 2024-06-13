def calculate_team_form(df, team, num_matches=5):
    team_matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)]
    team_matches = team_matches.sort_values(by='Date', ascending=False).head(num_matches)
    
    team_matches['Points'] = team_matches.apply(
        lambda row: 3 if (row['HomeTeam'] == team and row['HomeWin']) or (row['AwayTeam'] == team and row['AwayWin'])
        else 1 if row['Draw']
        else 0,
        axis=1
    )
    return team_matches['Points'].sum()

def add_match_outcomes(df):
    """Add match outcome columns to the DataFrame."""
    df['HomeWin'] = df['FullTimeResult'] == 'H'
    df['AwayWin'] = df['FullTimeResult'] == 'A'
    df['Draw'] = df['FullTimeResult'] == 'D'
    return df
