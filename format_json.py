import json


def format_name(name):
    return "".join(ch for ch in name.lower() if ch not in [" ", "-"])


with open("countries.json", "r") as file:
    data = json.load(file)

for dt_point in data:
    dt_point["formated name"] = format_name(dt_point["name"])
    dt_point["state"] = "not guessed"


with open("countries.json", "w") as file:
    json.dump(data, file)
