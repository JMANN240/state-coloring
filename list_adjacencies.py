import json

with open("adjacency.json", "r") as json_file:
    data = json.load(json_file)

adjacencies = data["adjacency"]
for row_county, row in adjacencies.items():
    for col_county in row:
        if (adjacencies[row_county][col_county] == 1):
            print(f"{row_county} is adjacent to {col_county}")