from PIL import Image, ImageDraw, ImageFont
img = Image.new("RGB", (500, 300), color="purple")  # Creates image object
font = ImageFont.truetype("arial.ttf", 16)  # Sets font and font size
user_txt = input("Give some text:")
draw = ImageDraw.Draw(img)  # Creates drawer object
txt_color = 0
polygon_color = 0
ellipse_color = 0
colors = {1: "green",
          2: "blue",
          3: "orange",
          4: "white"}

print("Available colors:")  # Prints all available colors
for color in colors.items():
    print(f"{color[0]} - {color[1]}")

# Choosing the color of figures
txt_color = int(input(f"Choose color for your text: "))
polygon_color = int(input(f"Choose color for triangle: "))
ellipse_color = int(input(f"Choose color for circle: "))

draw.text((50, 250), user_txt, fill=colors[txt_color], font=font)  # Draws text on image
draw.polygon((150, 50, 500, 50, 325, 250), fill=colors[polygon_color])  # Draws triangle
draw.ellipse((250, 50, 400, 200), fill=colors[ellipse_color])  # Draws circle

img.save("image8_3.png")
