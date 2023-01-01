import json

with open("data_dump.json", "r") as f:
    data = json.load(f)
with open("formatted_data.json", "w") as f:
    json.dump(data, f, indent = 4)
