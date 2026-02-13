import argparse
import os
from PIL import Image


def v_concatenate_imgs(img_paths, output_path):
    imgs = [Image.open(img_url) for img_url in img_paths]

    output_width = max([img.width for img in imgs])
    output_height = sum([img.height for img in imgs])

    new_image = Image.new("RGB", (output_width, output_height))

    y_offset = 0
    for img in imgs:
        new_image.paste(img, (0, y_offset))
        y_offset += img.height

    new_image.save(output_path)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_img_paths", nargs='+')
    parser.add_argument("-o", type=str)
    parser.add_argument("-v", action="store_true")

    args = parser.parse_args()

    img_paths = [os.path.join(os.getcwd(), img_path) for img_path in args.input_img_paths]
    
    if args.v:
        v_concatenate_imgs(img_paths, os.path.join(os.getcwd(), args.o))


if __name__ == "__main__":
    main()