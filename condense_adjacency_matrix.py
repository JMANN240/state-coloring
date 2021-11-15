import json

with open("adjacency.json", "r") as json_file:
    data = json.load(json_file)

adjacency = data["adjacency"]
condensed = {}
for row_node, row in adjacency.items():
    condensed[row_node] = [col_node for col_node, adj in row.items() if adj == 1]

if (input("Are you sure you want to overwrite your condensed adjacency matrix? (y/N): ").lower() == "y"):
    with open("condensed.json", "w") as json_file:
        json.dump(condensed, json_file, indent=4)