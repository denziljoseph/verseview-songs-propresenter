import os
from config import SONGS_DIR

def save_file(content, file_name):
    file_path = os.path.join(SONGS_DIR, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    return file_path
