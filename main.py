import sys
import json
import os

data_file = "ispenses_data.json"

def load_data(): 
    if not os.path.exists(data_file): 
        return {"categories":[], "expenses":[]} 
    
    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        
        if "categories" not in data:
            data["categories"] = []
        if "expenses" not in data:
            data["expenses"] = []
        return data
        
def save_data(data):
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
def main():
    try:
        data = load_data()
        if len(sys.argv) < 2:
            print("Usage: python3 main.py command [arguments]")
            return

        command = sys.argv[1]

        if command == "inputcat":
            new_cat = sys.argv[2]

            if new_cat not in data["categories"]:
                data["categories"].append(new_cat)
                save_data(data)
                print(f"New category {new_cat} added")
            else:
                print("This category already there")
                
        elif command == "add":
            amount = float(sys.argv[2])
            category = sys.argv[3]
            description = " ".join(sys.argv[4:])

            if category not in data["categories"]:
                print(f"Error: Category '{category}' not in file. Please, add.")
                return

            data["expenses"].append({
                "amount": amount,
                "category": category,
                "description": description
            })
            save_data(data)
            print(f"Rashod '{description}' for the summa {amount} add.")
        
        elif command == "list":
            if len(sys.argv) > 2:
                category_filter = sys.argv[2]
            else:
                category_filter = None

            print(f"{'Name':<20} | {'Summa':<10} | {'Category':<15}")
            print("-" * 50)

            for exp in data["expenses"]:
                if not category_filter or exp["category"] == category_filter:
                    print(f"{exp['description']:<20} | {exp['amount']:<10} | {exp['category']:<15}")
                    
        elif command == "total":
            if len(sys.argv) > 2: 
                category_filter = sys.argv[2] 
            else:
                category_filter = None
            
            total = sum(exp["amount"] for exp in data["expenses"]
                        if not category_filter or exp["category"] == category_filter)

            scope = f"in category '{category_filter}'" if category_filter else "all"
            print(f"Total expenses {scope}: {total}")

        else:
            print(f"Unknown command: {command}")
        
    except (IndexError, ValueError):
        print("Error: Check this out.")

if __name__ == "__main__":
    main()
        