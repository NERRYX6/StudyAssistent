from json import dump, load, JSONDecodeError

all_list = {}

def load_data():
    defaults = {
        "task_ID": 0,
        "tasks": {}
    }

    try:
        with open("task_list.json", "r") as f:
            data = load(f)
            return data

    except (FileNotFoundError, JSONDecodeError):
        return defaults

def save(value, key):
    all_list[key] = value

    with open('task_list.json', 'w') as f:
        dump(all_list, f, indent=4)