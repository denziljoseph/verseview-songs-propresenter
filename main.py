from pathlib import Path
import pandas as pd

from data_processing import (
    load_data, filter_data, process_lyrics,
    count_verses, count_lines
)
from template_generator import generate_template
from file_handler import save_file
from pro_encoder import encode_to_pro

def main():
    categories = ['VV Malayalam 2021']
    songs = ['Unarvin varam labhippaan']

    df = load_data()
    df = filter_data(df, categories, songs)

    # Process original lyrics
    df.loc[:, 'list_lyrics'] = df['lyrics'].apply(process_lyrics)
    df.loc[:, 'lyrics_verses_count'] = df['list_lyrics'].apply(count_verses)
    df.loc[:, 'lyrics_lines_per_verse'] = df['list_lyrics'].apply(count_lines)

    # Process secondary lyrics
    df.loc[:, 'list_lyrics2'] = df['lyrics2'].apply(process_lyrics)
    df.loc[:, 'lyrics2_verses_count'] = df['list_lyrics2'].apply(count_verses)
    df.loc[:, 'lyrics2_lines_per_verse'] = df['list_lyrics2'].apply(count_lines)

    # Keep only songs where verse count matches
    df = df[df['lyrics_verses_count'] == df['lyrics2_verses_count']]

    output_columns = [
        'id', 'name', 'cat', 'font', 'font2', 'yvideo', 'copy',
        'notes', 'lyrics', 'lyrics2', 'title2', 'tags',
        'list_lyrics', 'lyrics_verses_count', 'lyrics_lines_per_verse',
        'list_lyrics2', 'lyrics2_verses_count', 'lyrics2_lines_per_verse'
    ]
    df[output_columns].to_csv('output.csv', index=False)

    df = df[output_columns]

    for song_data in generate_template(df):
        file_path = save_file(song_data["rendered_template"], f"{song_data['song_name']}.txt")
        encode_to_pro(file_path)

if __name__ == '__main__':
    main()
