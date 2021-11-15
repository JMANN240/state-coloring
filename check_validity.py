import json

with open("adjacency.json", "r") as json_file:
    data = json.load(json_file)

with open("condensed.json", "r") as json_file:
    condensed = json.load(json_file)

nodes = data["nodes"]
adjacencies = data["adjacency"]
colors = {node: "" for node in nodes}

def check_validity(colors, condensed):
    for row_node, row in condensed.items():
        for col_node in row:
            if colors[row_node] == colors[col_node] and colors[row_node] != '' and colors[col_node] != '':
                return False
    return True

colors["defiance"] = "red"
colors["henry"] = "red"

print(check_validity(colors, condensed))