import os

import colour
from PIL import Image, ImageFilter


class Pixel:
    def __init__(self, x, y, rgb):
        self.x = x
        self.y = y
        self.rgb = rgb
        self.lab = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(self.rgb))


class Canvas:
    def __init__(self, path):
        self.image = Image.open(path)
        self.width = int(self.image.width)
        self.height = int(self.image.height)
        self.size = self.width * self.height

    def __iter__(self):
        for y in range(self.image.height):
            for x in range(self.image.width):
                yield Pixel(x, y, self.image.getpixel((x, y)))


class ColorPalette:
    def __init__(self, path):
        self.path = path
        self.data = {}
        self.prepare()

    def prepare(self):
        for i, image_name in enumerate(os.listdir(self.path)):
            image_path = os.path.join(self.path, image_name)
            image = Image.open(image_path)
            transformed = image.resize((5, 5)).filter(ImageFilter.BLUR)
            rgb = transformed.getpixel((2, 2))  # center of resized image
            lab = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(rgb))
            self.data[tuple(lab)] = image.filename

    def compare(self, lab1, lab2):
        delta_e = colour.delta_E(lab1, lab2)
        return delta_e

    def get(self, lab):
        deltas = [(self.compare(lab, clr), clr) for clr in self.data.keys()]
        closest_color = min(deltas)[1]
        image = Image.open(self.data.get(closest_color))
        return image


class ImageSticker:
    def __init__(self, image_path, dir_path, scale=20):
        self.image = Canvas(image_path)
        self.scale = scale
        self.colors = ColorPalette(dir_path)
        self.pixels = None
        self.converted_image = Image.new('RGB', (self.image.width * self.scale, self.image.height * self.scale))

    def convert(self):
        i = 0
        for pixel in self.image:
            image = self.colors.get(pixel.lab)
            image = image.resize((self.scale, self.scale))
            self.converted_image.paste(image, (pixel.x * self.scale, pixel.y * self.scale))

            print(f'[{(i/self.image.size)*100:>3.2f}%]')
            i += 1

    def save(self, path):
        self.converted_image.save(path)
