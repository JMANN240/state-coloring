# Import some modules for JSON operations and utilities

import json
from util import check_validity, create_image

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

# The node names and colors (initialized to none)
nodes = {node: None for node in condensed.keys()}
node_names = list(nodes.keys())

# Color states recursively with backtracking
# Input: the node index (optional)
# Output: success of coloring

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

# Color the states and print out the final configuration
if color_states():
    print(json.dumps(nodes, indent=4))
else:
    print("Could not find a valid state")

# Create the image of the state, save it, and show it
img = create_image(nodes, colors)
img.save("output.png")
img.show()