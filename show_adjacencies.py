# Import some modules for JSON operations and utilities

import json
from util import create_image

# Define the colors of the nodes
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 64, 255)
}

# Open the verbose adjacency file and load it into a variable
with open("verbose.json", "r") as json_file:
    verbose = json.load(json_file)

node_names = list(verbose.keys())

for node, adjs in verbose.items():
    nodes = {node: {"color": None} for node in node_names}
    nodes[node]["color"] = "red"
    for adj in adjs:
        nodes[adj]["color"] = "green"
    img = create_image(nodes, colors)
    img.show()