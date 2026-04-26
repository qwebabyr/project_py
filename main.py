import sys
import json
import os

data_file = "ispenses_data.json"

def load_data():
    if not os.path.exists(data_file):
        return {"categories":[]}
    
    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        
        if "categories" not in data:
            data["categories"] = []
        return data
def save_data(data):
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def main():
    data = load_data()
    if len(sys.argv) <= 2:
        print("Usage: python3 interest.py inputcat <new category>")
        return

    command = sys.argv[1]

    if command == "inputcat":
        new_cat = sys.argv[2]

        if new_cat not in data["categories"]:
            data["categories"].append(new_cat)
            save_data(data)
            print(f"New category {new_cat} added")

        elif not new_cat:
            print("Error: name category cannot be empty")

        else:
            print("This category already there")

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
        