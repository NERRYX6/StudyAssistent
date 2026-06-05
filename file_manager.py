import json


def save(t_list):
    with open("data.json","w") as f:
        json.dump(t_list, f, indent=4)

def load(key):
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}
    return data[key] if key in data else {}