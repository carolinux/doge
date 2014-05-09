from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
#TEH PNG EXPORT#
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf", 25)
img = Image.new("RGBA", (200, 200), (120, 20, 20))
draw = ImageDraw.Draw(img)
draw.text((0, 0), "This is a test", (255, 255, 0), font=font)
draw = ImageDraw.Draw(img)
draw = ImageDraw.Draw(img)
img.save("a_test.png")

from Tkinter import *
import PIL
from PIL import ImageTk

#root = ImageTk.Tk()
#root.title('captcha')
image_file = "/home/carolinux/Projects/doge/doge/doge.jpg"
img = PIL.Image.open(image_file)
width, height = img.size

canvas = Canvas(width=width, height=height, bg='blue')

image = ImageTk.PhotoImage(file=image_file)
draw = ImageDraw.Draw(img)
draw.text((0, 0), "This is a test", (255, 255, 0), font=font)
draw = ImageDraw.Draw(img)
img.save("foo.png")

canvas.create_image(0, 0, image=image, anchor=NW)
canvas.pack(expand=YES, fill=BOTH)

mainloop()
