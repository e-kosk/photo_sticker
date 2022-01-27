import argparse
from sticker import ImageSticker

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert photo.')
    parser.add_argument('photos_dir', type=str, help='path of directory containing photos')
    parser.add_argument('main_photo', type=str, help='path of the main photo')
    parser.add_argument('--output', type=str, help='output path of processed image', default='processed.jpg')
    parser.add_argument('--color-picker', type=str, help='color picker class', default='resize')
    parser.add_argument('--color-collation', type=str, help='color comparing class', default='euclidean')
    args = parser.parse_args()

    image = ImageSticker(args.main_photo, args.photos_dir, args.color_picker, args.color_collation)
    image.convert()
    image.save(args.output)
