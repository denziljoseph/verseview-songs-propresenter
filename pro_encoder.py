import subprocess
import os
from config import PROTOC_PATH, PROTO_DIR, PROTO_FILE

def encode_to_pro(input_file):
    name, _ = os.path.splitext(input_file)
    output_file = f"{name}.pro"
    command = f'{PROTOC_PATH} --encode="rv.data.Presentation" {PROTO_FILE} < "{input_file}"'
    
    os.chdir(PROTO_DIR)
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        result = subprocess.run(command, stdin=infile, stdout=outfile, stderr=subprocess.PIPE, shell=True, text=True)
        
        if result.returncode != 0:
            print(f"Error encoding: {result.stderr}")
        else:
            print(f"Encoded file: {output_file}")
