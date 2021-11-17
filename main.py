import json
from PIL import Image
from PIL.ImageOps import colorize


colorings = {"red": (255, 0, 0), "green": (0, 255, 0), "yellow": (255, 255, 0), "blue": (0, 64, 255)}

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

print(check_validity(colors, condensed))

def color_states(node_index):
    if node_index == len(nodes):
        return True
    for c in colorings.keys():
        print(f"trying to color {nodes[node_index]} {c}")
        colors[nodes[node_index]] = c
        if check_validity(colors, condensed):
            if color_states(node_index+1):
                return True
        else:
            colors[nodes[node_index]] = ""
    else:
        return False

color_states(0)
print(json.dumps(colors, indent=4))

size = (1056, 1159)
img = Image.new("RGBA", size, (255, 255, 255))


for county, color in colors.items():
    try:
        overlay = Image.open(f"images/{county}.png").convert("L")
        overlay_colored = colorize(overlay, (0,0,0), colorings[color])
        img.paste(overlay_colored, (0, 0), overlay)
    except:
        print(f"image \"{county}.png\" not found!")

img.show()