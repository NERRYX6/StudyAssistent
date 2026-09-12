from json import dump, load, JSONDecodeError

all_list = {}

def load_data(key):
    try:
        with open('task_list.json', 'r') as f:
            task_list = load(f)
        return task_list[key]
    except FileNotFoundError:
        return {}
    except JSONDecodeError:
        return {}

def save(save_list, key):
    all_list[key] = save_list
    with open('task_list.json', 'w') as f:
        dump(all_list, f, indent=4)