import sqlite3
import csv
import pandas as pd
from jinja2 import Template
import uuid
import templates.template_text as tt
import subprocess
import os

def read_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('verseview_db/default.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to retrieve data
    cur.execute('SELECT * FROM sm where cat="VV Malayalam 2021" and name="Unarvin varam labhippaan"')

    # Fetch all rows from the executed query
    rows = cur.fetchall()

    # Process and print the retrieved data
    for row in rows:
        print(f'name: {row[1]}, lyrics: {row[11]}, lyrics2: {row[12]}, cat: {row[3]}')
        break

    # Close the connection
    conn.close()

def list_tables():
    # Connect to the SQLite database
    conn = sqlite3.connect('verseview_db/default.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to retrieve all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all results from the executed query
    tables = cur.fetchall()

    # Process and print the table names
    for table in tables:
        print(table[0])

    # Close the connection
    conn.close()    

def export_data_csv():

    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect('verseview_db/default.db')

    cursor = conn.cursor()

    # Step 2: Retrieve data from the database
    query = "SELECT * FROM sm;"  # Replace 'your_table' with the name of your table
    cursor.execute(query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Get the column names from the cursor description
    column_names = [description[0] for description in cursor.description]

    # Step 3: Write data to a CSV file
    csv_file_path = 'output.csv'  # Replace 'output.csv' with the desired output CSV file path
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the column headers
        csv_writer.writerow(column_names)
        
        # Write the data rows
        csv_writer.writerows(rows)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    print(f"Data has been written to {csv_file_path}")

def export_data_dataframe():

    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect('verseview_db/default.db')

    conn.cursor()

    # Step 2: Retrieve data from the database
    query = "SELECT * FROM sm;"  # Replace 'your_table' with the name of your table
    # Execute the query and load the data into a pandas DataFrame
    pd.options.display.max_colwidth = 10000
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Display the DataFrame
    #print(df)

    categories_to_include = ['VV Malayalam 2021']
    songs_to_debug = ['Aashisekanam vadhuvararkkinnu','En lamghanangal njaan avanodariyichappol','Mele koodarathill','Yeshuvin veerare purrappeduveen','Yohannaan chaariya thirumaarvvil']
    df = df[(df['cat'].isin(categories_to_include))]
    df = df[(df['name'] == 'Unarvin varam labhippaan')]
    #df = df[(df['name'].isin(songs_to_debug))]



    df["list_lyrics"] = df.apply(process_lyrics,axis=1)
    df["lyrics_verses_count"] = df.apply(count_verses,axis=1)
    df["lyrics_lines_per_verse"] = df.apply(count_lines,axis=1)

    df["list_lyrics2"] = df.apply(process_lyrics2,axis=1)
    df["lyrics2_verses_count"] = df.apply(count_verses2,axis=1)
    df["lyrics2_lines_per_verse"] = df.apply(count_lines2,axis=1)   

    df = df[(df['lyrics_verses_count'] == df['lyrics2_verses_count'])] 


    #print(df)
    # Export DataFrame to CSV
    df.to_csv('output2.csv',columns=['id', 'name', 'cat', 'font', 'font2', 'yvideo', 'copy', 'notes', 'lyrics', 'lyrics2', 'title2', 'tags', 'list_lyrics', 'lyrics_verses_count', 'lyrics_lines_per_verse', 'list_lyrics2', 'lyrics2_verses_count', 'lyrics2_lines_per_verse'], index=False)

    df = df[['id', 'name', 'cat', 'font', 'font2', 'yvideo', 'copy', 'notes', 'lyrics', 'lyrics2', 'title2', 'tags', 'list_lyrics', 'lyrics_verses_count', 'lyrics_lines_per_verse', 'list_lyrics2', 'lyrics2_verses_count', 'lyrics2_lines_per_verse']]

    generate_template(df)

def remove_empty_strings(string):
    return string != ""

def process_lyrics(row):
    song_list = row['lyrics'].split('<slide>')

    filtered_list = filter(remove_empty_strings, song_list)

    return list(filtered_list)

def count_verses(row):
    song = row['list_lyrics']
    return len(song)

def count_lines(row):
    song = row['list_lyrics']
    lines = []
    for verse in song:
        verse_lines = verse.split('<BR>')
        verse_lines = filter(remove_empty_strings, verse_lines)

        lines.append(len(list(verse_lines)))

    return lines

def process_lyrics2(row):
    song_list = row['lyrics2'].split('<slide>')
    filtered_list = filter(remove_empty_strings, song_list)

    return list(filtered_list)

def count_verses2(row):
    song = row['list_lyrics2']
    return len(song)

def count_lines2(row):
    song = row['list_lyrics2']
    lines = []
    for verse in song:
        verse_lines = verse.split('<BR>')
        verse_lines = filter(remove_empty_strings, verse_lines)

        lines.append(len(list(verse_lines)))

    return lines

def generate_template(df):


    cue_groups_template = Template(tt.cue_groups_template)
    cues_template = Template(tt.cues_template)
    base_slide_rtf_data_template = Template(tt.base_slide_rtf_data_template)
    base_slide_rtf_additional_line_template = Template(tt.base_slide_rtf_additional_line_template)
    base_slide_rtf_first_line_template = Template(tt.base_slide_rtf_first_line_template)
    notes_rtf_data_template = Template(tt.notes_rtf_data_template)
    notes_additional_line_template = Template(tt.notes_additional_line_template)
    notes_first_line_template = Template(tt.notes_first_line_template)
    main_template = Template(tt.main_template)
    


    for index, row in df.iterrows():
        lyrics_verses_count = row['lyrics_verses_count']
        lyrics2_verses = row['list_lyrics2']
        lyrics_verses = row['list_lyrics']
        song_name = row['name']
        song_guid = uuid.uuid4()
        

        intro_guid = uuid.uuid4()
        outro_guid = uuid.uuid4()
        intro_group_guid = uuid.uuid4()
        outro_group_guid = uuid.uuid4()
        arrangement_guid = uuid.uuid4()

        cue_groups_template_str = ''
        cues_template_str = ''
        main_template_str = ''



        for i in range(0,lyrics_verses_count):  
            #print("i::",i)  
            #print("lyrics2_verses::", lyrics2_verses)

            verse_guid = uuid.uuid4()
            cue_group_guid = uuid.uuid4()
            actions_guid = uuid.uuid4()
            element1_guid = uuid.uuid4()
            element2_guid = uuid.uuid4()
            presentation_guid = uuid.uuid4()

            lines = lyrics2_verses[i].split('<BR>')
            base_slide_rtf_first_line_template_str = ''
            base_slide_rtf_additional_line_template_str = ''

            if cue_groups_template_str != '':
                cue_groups_template_str = cue_groups_template_str + '\n'
            if cues_template_str != '':
                cues_template_str = cues_template_str + '\n'

            for index,line in enumerate(lines):
                #print("index,line::",index,line)
                if index == 0:
                    base_slide_rtf_first_line_template_str = base_slide_rtf_first_line_template.render(verseview_lyrics2_line=line).replace("\n", "").lstrip().rstrip()
                    #print('first line::',line)
                    #print('base_slide_rtf_first_line_template::',base_slide_rtf_first_line_template_str)
                else:
                    base_slide_rtf_additional_line_template_str = base_slide_rtf_additional_line_template_str + base_slide_rtf_additional_line_template.render(verseview_lyrics2_line=line).replace("\n", "").lstrip().rstrip()
                    
                    #print('next line::',line)
                    #print('base_slide_rtf_additional_line_template::',base_slide_rtf_additional_line_template_str)

            base_slide_rtf_data_template_str = base_slide_rtf_data_template.render(first_line_template=base_slide_rtf_first_line_template_str, additional_line_template=base_slide_rtf_additional_line_template_str)
            #print("base_slide_rtf_data_template_str::",base_slide_rtf_data_template_str)


            lines = lyrics_verses[i].split('<BR>')
            notes_first_line_template_str = ''
            notes_additional_line_template_str = ''
            for index,line in enumerate(lines):
                #print("index,line::",index,line)
                if index == 0:
                    notes_first_line_template_str = notes_first_line_template.render(verseview_lyrics_line=line).replace("\n", "").lstrip().rstrip()
                    #print('first line::',line)
                    #print('notes_first_line_template::',notes_first_line_template_str)
                else:
                    notes_additional_line_template_str = notes_additional_line_template_str + notes_additional_line_template.render(verseview_lyrics_line=line).replace("\n", "").lstrip().rstrip()
                    
                    #print('next line::',line)
                    #print('notes_additional_line_template::',notes_additional_line_template_str)

            notes_rtf_data_template_str = notes_rtf_data_template.render(first_line_template=notes_first_line_template_str, additional_line_template=notes_additional_line_template_str)
            #print("notes_rtf_data_template_str::",notes_rtf_data_template_str)

            cue_groups_template_str = cue_groups_template_str + cue_groups_template.render(cue_group_guid=cue_group_guid,verse_guid=verse_guid)
            
            cues_template_str = cues_template_str + cues_template.render(verse_guid=verse_guid,actions_guid=actions_guid,element1_guid=element1_guid,element2_guid=element2_guid,base_slide_rtf_data_template=base_slide_rtf_data_template_str,presentation_guid=presentation_guid,notes_rtf_data_template=notes_rtf_data_template_str)
        
        main_template_str = main_template.render(song_guid=song_guid,song_name=song_name,arrangement_guid=arrangement_guid,intro_group_guid=intro_group_guid,outro_group_guid=outro_group_guid,intro_guid=intro_guid,cue_groups_template=cue_groups_template_str,outro_guid=outro_guid,cues_template=cues_template_str)
        #print(main_template_str)
        fp = create_file(main_template_str,song_name)
        encode_to_pro(fp)

def create_file(string_to_write,file_name):
    # Define the file path
    file_path = f"songs/{file_name}"
    songs_dir = r"C:/Projects/verseview-songs-propresenter/"

    os.chdir(songs_dir)

    # Open the file in write mode and write the string to it
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(string_to_write)
    
    return file_path

def encode_to_pro(file_path):
    # Define the command and arguments
    protoc_path = r"C:/Projects/verseview-songs-propresenter/protoc/protoc.exe"
    encode_arg = '--encode="rv.data.Presentation"'
    proto_file = 'propresenter.proto'
    proto_dir = r"C:/Projects/verseview-songs-propresenter/proto"

    # Save the current working directory
    original_dir = os.getcwd()
    input_file = f'{original_dir}\{file_path}'
    output_file = f'{original_dir}\{file_path}.pro'


    # Build the full command
    command = f'{protoc_path} {encode_arg} {proto_file} < "{input_file}"'
    print("command::",command)

    os.chdir(proto_dir)

    # Open the input and output files
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        try:
            # Execute the command with redirected input and output
            result = subprocess.run(command, stdin=infile, stdout=outfile, stderr=subprocess.PIPE, shell=True, text=True)
            
            # Check for errors
            if result.returncode != 0:
                print(f"Error executing protoc: {result.stderr}")
            else:
                print(f"Successfully encoded data from {input_file} to {output_file}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    export_data_dataframe()