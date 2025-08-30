import pandas as pd
from database import get_connection

def load_data():
    conn = get_connection()
    query = "SELECT * FROM sm;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def filter_categories(df, categories):
    if categories:
        return df[(df['cat'].isin(categories))]
    return df

def filter_songs(df, songs):
    if songs:
        return df[(df['name'].isin(songs))]
    return df


def process_lyrics(lyrics):
    return list(filter(lambda x: x != "", lyrics.split('<slide>')))

def count_verses(lyrics_list):
    return len(lyrics_list)

def count_lines(lyrics_list):
    return [len(list(filter(lambda x: x != "", verse.split('<BR>')))) for verse in lyrics_list]
