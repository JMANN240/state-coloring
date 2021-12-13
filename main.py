# Import some modules for JSON operations and utilities

import json
from util import create_image, check_validity_quick

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

# The node names and colors (initialized to none)
node_names = list(verbose.keys())
nodes = {node: {"color": None} for node in node_names}

def get_next_node():
    for node, info in nodes.items():
        if info["color"] is None:
            return node
    return None

def color_node(node_name, color):
    nodes[node_name]["color"] = color

def uncolor_node(node_name):
    nodes[node_name]["color"] = None

# Color states recursively with backtracking
# Input: the node index (optional)
# Output: success of coloring

def complete():
    for info in nodes.values():
        if info["color"] is None:
            return False
    return True

def color_states():

    # Initialize some variables to reduce code reuse
    node_name = get_next_node()
    if complete():
        return True

    # Try every defined color
    for c in colors.keys():

        # Try to color the current node the current color
        color_node(node_name, c)

        # If we are still in a valid state after that
        if check_validity_quick(nodes, verbose, node_name):

            # Return True if we are on the last node or if we could successfully color the subsequent nodes
            if color_states():
                return True
        uncolor_node(node_name)
    
    # If we have tried every color and still not returned True, it is impossible to be valid given the previous state
    else:
        # Undo current node's color and return false
        return False

# Color the states and print out the final configuration
if color_states():
    print(json.dumps(nodes, indent=4))

    # Create the image of the state, save it, and show it
    img = create_image(nodes, colors)
    img.save("output.png")
    img.show()
else:
    print("Could not find a valid state")