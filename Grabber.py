import os
import json

def Read_File(File: str) -> dict:
    with open(File, "r") as file:
        data = json.load(file)
        
    return data

def Check_For_Key(File: str) -> bool:
    Dir = os.listdir('.')
    for file in Dir:
        if file == File:
            return True
    return False
