from PIL import ImageFilter, Image


class ColorPicker:
    @classmethod
    def get_color(cls, image):
        """
        Process whole image into one color
        :param image: PIL.Image object
        :return: rgb color
        """
        raise NotImplementedError('Overwrite this method in custom color pickers.')


class ResizeAndBlurPicker(ColorPicker):
    @classmethod
    def get_color(cls, image):
        transformed = image.resize((5, 5)).filter(ImageFilter.BLUR)
        rgb = transformed.getpixel((2, 2))  # center of resized image
        return tuple(rgb)


class ResizePicker(ColorPicker):
    @classmethod
    def get_color(cls, image):
        transformed = image.resize((1, 1))
        rgb = transformed.getpixel((0, 0))
        return tuple(rgb)


class PickerFactory:
    PICKERS = {
        'resize': ResizePicker,
        'resize_blur': ResizeAndBlurPicker,
    }

    @classmethod
    def select(cls, name):
        return cls.PICKERS[name]
