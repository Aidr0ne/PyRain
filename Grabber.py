import os
import json

def Read_File(File: str) -> dict:
    with open(File, "r") as file:
        data = json.load(file)
        
    return data

def read_binary(file: str) -> str:
    with open(file, "rb") as File:
        data = File.read()
    return data

def replace_single_quotes(input_string):
    return input_string.replace("'", '"')

def Check_For_Key(File: str) -> bool:
    Dir = os.listdir('.')
    for file in Dir:
        if file == File:
            return True
    return False

def add_json(name: str) -> str:
    return name + ".json"

def Write_key(File: str, content: str) -> None:
    File = add_json(File)
    with open(File, "w") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
