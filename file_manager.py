import json
from task_manager import task_list
from notes_manager import notes_list
from statistics_manager import statistics_list

def load():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}
    return data

list_with_saves = load()

def save(t_list, key):
    with open("data.json","w") as f:
        if key == "*":
            list_with_saves["tasks"] = task_list
            list_with_saves["notes"] = notes_list
            list_with_saves["statistics"] = statistics_list
        elif key in list_with_saves:
            list_with_saves[key] = t_list
        json.dump(list_with_saves, f, indent=4)