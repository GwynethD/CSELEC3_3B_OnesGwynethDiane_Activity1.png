from PIL import Image, ImageDraw, ImageFont
import random


width, height = 500, 700
trophy = Image.new("RGB", (width, height), color="black")
draw = ImageDraw.Draw(trophy)


title_font = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 36)
category_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 28)
tagline_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)


for _ in range(150):
    x = random.randint(0, width)
    y = random.randint(0, height)
    w = random.randint(5, 15)
    h = random.randint(5, 15)
    color = random.choice(["pink", "yellow", "blue", "green", "orange", "purple"])
    draw.ellipse((x, y, x + w, y + h), fill=color)


for i in range(150, 250, 5): 
    fill_color = (255, 200 + (i-150)//2, 0)
    draw.ellipse((150, i, 350, i+100), fill=fill_color)


draw.polygon([(150, 200), (150, 400), (350, 400), (350, 200)], fill="gold", outline="darkred")


draw.arc((110, 180, 180, 350), start=90, end=270, fill="gold", width=10)  
draw.arc((320, 180, 390, 350), start=-90, end=90, fill="gold", width=10)  


draw.polygon([(110, 250), (80, 330), (100, 350), (130, 270)], fill="darkred")   
draw.polygon([(390, 250), (420, 330), (400, 350), (370, 270)], fill="darkred") 


draw.rectangle((180, 400, 320, 500), fill="darkred", outline="gold", width=4)
draw.rectangle((150, 500, 350, 520), fill="darkred", outline="gold", width=4)


def draw_star(cx, cy, size=40, color="yellow"):
    points = [
        (cx, cy-size),
        (cx+size//3, cy-size//3),
        (cx+size, cy-size//3),
        (cx+size//2, cy+size//6),
        (cx+2*size//3, cy+size),
        (cx, cy+size//2),
        (cx-2*size//3, cy+size),
        (cx-size//2, cy+size//6),
        (cx-size, cy-size//3),
        (cx-size//3, cy-size//3),
    ]
    draw.polygon(points, fill=color)


draw_star(250, 300, size=40, color="darkred")


for _ in range(12):
    x = random.randint(100, 400)
    y = random.randint(150, 450)
    size = random.randint(10, 20)   
    draw_star(x, y, size=size, color=random.choice(["yellow", "yellow"]))

draw.text((80, 70), "PAUGNAT UG PASUNDAYAG ", font=title_font, fill="gold")
draw.text((105, 540), "  OVERALL CHAMPION   ", font=category_font, fill="darkred")
draw.text((105, 570), " College of Criminal Justice ", font=tagline_font, fill="gold")


trophy.save("trophy.png")
trophy.show()