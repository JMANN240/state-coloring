# Import some modules for JSON operations and utilities

import json
from collections import OrderedDict
from util import check_validity, create_image, check_uncolored

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

sorted_condensed = OrderedDict()

# most constrained first heuristic
# change it to least constrained first heuristic: set reverse=True
for key in sorted(condensed, key=lambda k: len(condensed[k]), reverse=False):
    sorted_condensed[key] = condensed[key]

# print sorted condensed
for key in sorted_condensed:
    print(f"{key}: {sorted_condensed[key]}")
    #print(f"{key}: {condensed[key]}")

nodes = {node: None for node in sorted_condensed.keys()}
node_names = list(nodes.keys())

# Color states recursively with backtracking
# Input: the node index (optional)
# Output: success of coloring

def color_states(node_index=0):
    node_name = node_names[node_index]

    for c in colors.keys():
        nodes[node_name] = c
        if check_validity(nodes, sorted_condensed):
            if check_uncolored(nodes) or color_states(node_index+1):
                return True
        else:
            nodes[node_name] = None

    return False

"""
def color_states(node_index=0):

    # Initialize some variables to reduce code reuse
    node_name = node_names[node_index]
    last_node = node_index == len(nodes) - 1

    # Try every defined color
    for c in colors.keys():

        # Try to color the current node the current color
        nodes[node_name] = c

        # If we are still in a valid state after that
        if check_validity(nodes, condensed):

            # Return True if we are on the last node or if we could successfully color the subsequent nodes
            if last_node or color_states(node_index+1):
                return True
        
        # Otherwise undo the coloring
        else:
            nodes[node_name] = None
    
    # If we have tried every color and still not returned True, it is impossible to be valid given the previous state
    else:
        return False
"""

# Color the states and print out the final configuration
if color_states():
    print(json.dumps(nodes, indent=4))

    # Create the image of the state, save it, and show it
    img = create_image(nodes, colors)
    img.save("output.png")
    img.show()
else:
    print("Could not find a valid state")