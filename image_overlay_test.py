from PIL import Image
from PIL.ImageOps import colorize

allen = Image.open("allen.png").convert("L")
auglaize = Image.open("auglaize.png").convert("L")

allen_colored = colorize(allen, (0,0,0), (255, 0, 0))
auglaize_colored = colorize(auglaize, (0,0,0), (0, 255, 0))

size = allen.size
print(size)
img = Image.new("RGBA", size, (0,0,0,0))

img.paste(allen_colored, (0, 0), allen)
img.paste(auglaize_colored, (0, 0), auglaize)

img.show()