# storage.py
# Create a function save_numbers(numbers, filename="data.json")
# It should save the list of numbers to a JSON file as a dictionary: {"numbers": numbers}
# Use indent=2 for readable formatting
# Overwrite the file if it exists
# Do not print anything in this function

import json


def save_numbers(numbers, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump({"numbers": numbers}, f, indent=2)


def load_numbers(filename="data.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data.get("numbers", [])
    except FileNotFoundError:
        return []
    
def save_report(numbers, results, filename="report.txt"):
    from datetime import datetime
    with open(filename, "a") as f:
        f.write(f"Report generated on {datetime.now()}\n")
        f.write(f"Numbers entered: {numbers}\n")
        f.write("Analysis Results:\n")
        for key, value in results.items():
            f.write(f"  {key}: {value}\n")
        f.write("\n")
    print((f"Analysis report saved to {filename}"))