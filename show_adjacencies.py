# Import some modules for JSON operations and utilities

import json
from collections import OrderedDict
from util import create_image

# Define the colors of the nodes
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 64, 255)
}

# Open the condensed adjacency file and load it into a variable
with open("condensed.json", "r") as json_file:
    condensed = json.load(json_file)

# Open the verbose adjacency file and load it into a variable
with open("verbose.json", "r") as json_file:
    verbose = json.load(json_file)

sorted_verbose = OrderedDict()

# most constrained first heuristic
# change it to most constrained first heuristic: set reverse=True
for key in sorted(verbose, key=lambda k: len(verbose[k]), reverse=True):
    sorted_verbose[key] = verbose[key]

# print sorted verbose
for key, value in sorted_verbose.items():
    print(f"{key}: {value}")

nodes = {node: None for node in sorted_verbose.keys()}
node_names = list(nodes.keys())
images = []

for node, adjs in sorted_verbose.items():
    nodes = {node: None for node in sorted_verbose.keys()}
    nodes[node] = "red"
    for adj in adjs:
        nodes[adj] = "green"
    img = create_image(nodes, colors)
    img.show()