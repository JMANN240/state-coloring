import json

with open("condensed.json", "r") as json_file:
    condensed = json.load(json_file)

verbose = {node_name: [] for node_name in condensed.keys()}

for key, value in condensed.items():
    for county in value:
        verbose[key].append(county)
        verbose[county].append(key)

with open("verbose.json", "w") as json_file:
    json.dump(verbose, json_file, indent=4)