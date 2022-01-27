import os

from PIL import Image

from colors.comparison import CollationFactory
from colors.pickers import PickerFactory


class ColorPalette:
    def __init__(self, path, picker, collation):
        self.path = path
        self.picker = PickerFactory.select(picker)
        self.collation = CollationFactory.select(collation)
        self.data = {}
        self.prepare()

    def prepare(self):
        for i, image_name in enumerate(os.listdir(self.path)):
            image_path = os.path.join(self.path, image_name)
            image = Image.open(image_path)
            color = self.picker.get_color(image)
            self.data[color] = image.filename

    def get(self, lab):
        deltas = [(self.collation.compare(lab, clr), clr) for clr in self.data.keys()]
        closest_color = min(deltas)[1]
        image = Image.open(self.data.get(closest_color))
        return image
