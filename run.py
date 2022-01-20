import argparse
from photo_sticker import PhotoSticker


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert photo.')
    parser.add_argument('photos_dir', type=str, help='path of directory containing photos')
    parser.add_argument('main_photo', type=str, help='path of the main photo')
    args = parser.parse_args()

    sticker = PhotoSticker(photos_dir_path=args.photos_dir, main_photo_path=args.main_photo, scale=20)
    sticker.prepare()
    sticker.run()

