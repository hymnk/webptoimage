import os
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)

IMAGES_DIR = './images'

def load_images(directory_path, extension='webp'):
    if not os.path.isdir(directory_path):
        logging.error(f"Directory '{directory_path}' does not exist.")
        return

    images = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(extension):
            images.append(os.path.join(directory_path, filename))
    return images

def convert_images(images, target_format='png'):
    for infile in images:
        outfile = os.path.splitext(infile)[0] + f'.{target_format}'
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.save(outfile)
            except OSError as e:
                logging.error(f'Failed to converd {infile}: {e}')

def main():
    target_list = load_images(IMAGES_DIR, extension='webp')
    if not target_list:
        logging.error('No webp images found.')
        return

    convert_images(target_list, target_format='png')

if __name__ == '__main__':
    main()
