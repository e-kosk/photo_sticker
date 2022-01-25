import argparse
from sticker import ImageSticker

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert photo.')
    parser.add_argument('photos_dir', type=str, help='path of directory containing photos')
    parser.add_argument('main_photo', type=str, help='path of the main photo')
    args = parser.parse_args()

    image = ImageSticker(args.main_photo, args.photos_dir)
    image.convert()
    image.save('sticked.jpg')
