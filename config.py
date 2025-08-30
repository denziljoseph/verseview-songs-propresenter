import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'verseview_db', 'default.db')
SONGS_DIR = os.path.join(BASE_DIR, 'songs')
PROTOC_PATH = os.path.join(BASE_DIR, 'protoc','protoc.exe')
PROTO_DIR = os.path.join(BASE_DIR, 'proto')
PROTO_FILE = 'propresenter.proto'
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
