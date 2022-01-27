import colour
from PIL import Image

from colors import ColorPalette


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


class ImageSticker:
    def __init__(self, image_path, dir_path, color_picker, color_collation, scale=20):
        self.image = Canvas(image_path)
        self.scale = scale
        self.colors = ColorPalette(dir_path, color_picker, color_collation)
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
