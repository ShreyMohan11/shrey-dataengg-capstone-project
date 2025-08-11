import pandas as pd

def load_players(file_path):
    return pd.read_csv(file_path)

def load_matches(file_path):
    return pd.read_csv(file_path)

def merge_players_matches(players_df, matches_df):
    return pd.merge(players_df, matches_df, on='PlayerID')

def total_runs_per_team(merged_df):
    return merged_df.groupby('Team')['Runs'].sum().reset_index()

def calculate_strike_rate(merged_df):
    df = merged_df.copy()
    df['StrikeRate'] = (df['Runs'] / df['Balls']) * 100
    return df[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]

def runs_agg_per_player(merged_df):
    return merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'max', 'min']).reset_index()

def avg_age_by_role(players_df):
    return players_df.groupby('Role')['Age'].mean().reset_index()

def total_matches_per_player(matches_df):
    df = matches_df.groupby('PlayerID').size().reset_index(name='MatchCount')
    return df[['PlayerID', 'MatchCount']]

def top_wicket_takers(merged_df):
    df = merged_df.groupby(['PlayerID', 'Name'])['Wickets'].sum().reset_index()
    top_3_df = df.sort_values(by='Wickets', ascending=False).head(3)
    return top_3_df[['PlayerID', 'Name', 'Wickets']]

def avg_strike_rate_per_team(merged_df):
    df = merged_df.copy()
    df['StrikeRate'] = (df['Runs'] / df['Balls']) * 100
    return df.groupby('Team')['StrikeRate'].mean().reset_index()

def catch_to_match_ratio(merged_df):
    
    total_catches = merged_df.groupby('PlayerID')['Catches'].sum()
    total_matches = merged_df.groupby('PlayerID')['MatchID'].count()
    catch_ratio = total_catches / total_matches
    
    return catch_ratio.reset_index(name='CatchToMatchRatio')
