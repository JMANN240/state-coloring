# utils.py
# Utility functions for coloring CSP

# Import some modules for image creation and manipulation

from PIL import Image
from PIL.ImageOps import colorize

# Check the validity of a state.
# Input: state of nodes, adjacency of nodes
# Output: validity of the state

def check_validity(state, adjacency):

    # For every row node and row in the adjacency matrix
    for row_node, row in adjacency.items():

        # For every column node in the row
        for col_node in row:

            # If the row node and the column node have the same color and aren't None, return False
            if state[row_node]["color"] == state[col_node]["color"] and state[row_node]["color"] is not None and state[col_node]["color"] is not None:
                return False
    
    # If we make it through the loop, return True
    return True

def check_validity_quick(state, adjacency, node):
    for adj in adjacency[node]:
        if state[node]["color"] == state[adj]["color"]:
            return False
    return True

# Create the image of the coloring given a state
# Input: state of nodes, color definitions
# Output: a PIL image of the colored nodes

def create_image(state, colors):

    # Create a new PIL image of the given size, solid white background
    img = Image.new("RGBA", (1056, 1159), (255, 255, 255))

    # For every node and its color in items
    for node, info in state.items():

        # Try to add the node's overlay
        try:
            # Open the node's image
            overlay = Image.open(f"images/{node}.png").convert("L")

            # Colorize the node's image to the node's color
            overlay_colored = colorize(overlay, (0,0,0), colors.get(info["color"], (255, 255, 255)))

            # overlay the node's image onto the existing image
            img.paste(overlay_colored, (0, 0), overlay)
        
        # If we couldn't open the file
        except FileNotFoundError:
            print(f"image \"{node}.png\" not found!")
    
    # Return the completed node
    return img

# Song:
# was thinking to implement bidirectional search
# this function checks if the goal state is reached
def check_uncolored(nodes):
    for node in nodes:
        if nodes[node] == None:
            return False
    return True