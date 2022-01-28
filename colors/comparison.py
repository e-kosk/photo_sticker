import math

import colour


class ColorCollation:
    @classmethod
    def prepare(cls, color):
        """
        Prepare color for further comparison
        :param color: rgb color in list
        :return: prepared color in hashable format
        """
        return color


class DeltaE(ColorCollation):
    @classmethod
    def prepare(cls, color):
        lab = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(color))
        return tuple(lab)

    @classmethod
    def compare(cls, color1, color2):
        delta_e = colour.delta_E(color1, color2)
        return delta_e


class EuclideanDistance(ColorCollation):
    @classmethod
    def compare(cls, color1, color2):
        r_difference = color2[0] - color1[0]
        g_difference = color2[1] - color1[1]
        b_difference = color2[2] - color1[2]
        distance = math.sqrt(
            math.pow(r_difference, 2) + math.pow(g_difference, 2) + math.pow(b_difference, 2)
        )
        return distance


class CollationFactory:
    COLLATIONS = {
        'deltae': DeltaE,
        'euclidean': EuclideanDistance,
    }

    @classmethod
    def select(cls, name):
        return cls.COLLATIONS[name]
