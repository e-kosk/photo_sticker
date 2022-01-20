import os

import colour
from PIL import Image


class PhotoSticker:
    def __init__(self, photos_dir_path, main_photo_path, scale):
        self.photos_dir_path = os.path.abspath(photos_dir_path)
        self.main_photo_path = os.path.abspath(main_photo_path)
        self.colors = {}
        self.scale = scale

    def prepare(self):
        for i, image_name in enumerate(os.listdir(self.photos_dir_path)):
            image_path = os.path.join(self.photos_dir_path, image_name)
            image = Image.open(image_path)
            image.resize((1, 1))
            rgb = image.getpixel((0, 0))
            lab = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(rgb))
            self.colors[tuple(lab)] = image_path

    def compare(self, color1, color2):
        delta_e = colour.delta_E(color1, color2)
        return delta_e

    def run(self):
        base_image = Image.open(self.main_photo_path)
        canvas = Image.new('RGB', (base_image.width * self.scale, base_image.height * self.scale))
        i = 0
        total_size = base_image.width * base_image.height
        for x in range(base_image.width):
            for y in range(base_image.height):
                rgb = base_image.getpixel((x, y))
                lab = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(rgb))
                deltas = [(self.compare(lab, clr), clr) for clr in self.colors.keys()]
                closest_color = min(deltas)[1]
                image_path = self.colors.get(closest_color)
                image = Image.open(image_path)
                image.resize((self.scale, self.scale))
                canvas.paste(image, (x * self.scale, y * self.scale))
                print(f'[{(i/total_size)*100:>3.0f}%] {i/total_size}')
                i += 1
        canvas.save('sticked.jpg')
