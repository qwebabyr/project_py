import sys
import json
import os

data_file = "interect_data.json"

def load_data():
    if not os.path.exists(data_file):
        return {"categories":[]}
    
    with open(data_file, "r", encoding="utf-8") as gg:
        data = json.load(gg)
        
        if "categories" not in data:
            data["categories"] = []
        return data