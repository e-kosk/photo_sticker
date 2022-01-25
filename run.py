import argparse
from sticker import ImageSticker

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert photo.')
    parser.add_argument('photos_dir', type=str, help='path of directory containing photos')
    parser.add_argument('main_photo', type=str, help='path of the main photo')
    parser.add_argument('output', type=str, help='output path of processed image')
    args = parser.parse_args()

    output = args.output or 'processed.jpg'

    image = ImageSticker(args.main_photo, args.photos_dir)
    image.convert()
    image.save(output)
