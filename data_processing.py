import pandas as pd
from database import get_connection

def load_data():
    conn = get_connection()
    query = "SELECT * FROM sm;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def filter_data(df, categories, songs):
    return df[(df['cat'].isin(categories)) & (df['name'].isin(songs))]

def process_lyrics(lyrics):
    return list(filter(lambda x: x != "", lyrics.split('<slide>')))

def count_verses(lyrics_list):
    return len(lyrics_list)

def count_lines(lyrics_list):
    return [len(list(filter(lambda x: x != "", verse.split('<BR>')))) for verse in lyrics_list]
