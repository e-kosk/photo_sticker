import math

import colour


class DeltaE:
    @classmethod
    def compare(cls, color1, color2):
        lab1 = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(color1))
        lab2 = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(color2))
        delta_e = colour.delta_E(lab1, lab2)
        return delta_e


class EuclideanDistance:
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
