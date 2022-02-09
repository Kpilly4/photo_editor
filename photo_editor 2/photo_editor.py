import glob 
import shutil
import os
from PIL import Image, ImageOps, ImageEnhance, ImageFont, ImageDraw

#Basic photo editing abilities via python file and pillow library
class PhotoEditor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = Image.open(filepath).convert("RGBA")
    #Function to save the file. 
    def save(self, output_filepath):
        # shutil.copyfile(self.filepath, output_filepath)
        print("this has saved@!!@!!")

        if self.filepath.endswith(".jpg"):
            self.img = self.img.convert("RGB")
        
        self.img.save(output_filepath)
    #Function to rotate pictures 
    def make_upside_down(self, rotate= (180)):
        self.img = self.img.rotate(rotate)

    #Function to Resize
    def make_resize(self, size = (128, 128)):
        self.img.thumbnail(size)

    #Function to add watermark text
    def add_watermark(self):
        font = ImageFont.truetype("ibm-plex-mono.ttf", 24)
        drawer = ImageDraw.Draw(self.img)
        drawer.multiline_text(
            (32, 32),
             "Insert Watermark",
              font = font,
               fill = (255, 0, 0, 100)
        )

    #Function to make a square so you can use as a thumbnail
    def make_square(self, size=200):

        (w,h) = self.img.size
       
        if w > h:
           print("landscape")
           x = (w - h) * 0.5
           y = 0 
           box = (x, y, h + x, h + y)
        else: 
            print('potrait')
            x = 0 
            y = (h - w) * 0.5
            box = (x, y, x + w , y + w)
        
        self.img = self.img.resize((size, size), box = box)

    #Filter with a greyscale
    def grey_scale(self):
        self.img = ImageOps.grayscale(self.img)
        self.img = self.img.convert("RGB")

    #Change contrast
    def contrast(self, amount = 1.5):
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(amount)
        

#where are the files coming from    
inputs = glob.glob("inputs/*")

#tells it where to save the files and if its ok to overwrite
os.makedirs("outputs", exist_ok=True)

#where you tell it what to do 
for filepath in inputs:
    output = filepath.replace("inputs", "outputs")

    image = PhotoEditor(filepath)
    image.contrast()
    image.grey_scale()
    image.make_square()
    image.save(output)
   
