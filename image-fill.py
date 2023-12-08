# This script automatically inserts img elements into
# the html file for the pictures page.

import glob
from pathlib import Path
import re
import argparse
from fileinput import FileInput
from sys import exit


def get_html_path(args) -> Path:
    # Find the path to the HTML file
    html_path = glob.glob(args.html_file)
    if len(html_path) == 0:
        print("HTML file provided cannot be found")
        exit(1)
    return Path(html_path[0])  # Shadow original html_path, now a Path


def get_image_path(args) -> Path:
    # Find the image directory
    image_dir = glob.glob(args.img_dir)
    if len(image_dir) == 0:
        print("Image directory cannot be found")
        exit(1)
    return Path(image_dir[0])


def find_images(image_dir: Path) -> [(str, [Path])]:
    out = []
    root_images = [p for p in image_dir.glob('*.*')
                   if re.match(r'.+(jpg|jpeg|png)', str(p))]
    out.append(('root', root_images))

    for dir in image_dir.glob('*/'):
        d_images = [p for p in dir.glob('*.*')
                    if re.match(r'.+(jpg|jpeg|png)', str(p))]
        out.append((dir.name, d_images))

    return out


def create_img_tag(image_path: Path, depth: int) -> str:
    src = image_path.relative_to(
        image_path.parents[depth]).as_posix().replace(" ", "\\ ")
    return f'<img src="{src}" />'


def create_section(name: str, image_paths: [Path]) -> [str]:
    if len(image_paths) == 0:
        return []

    out = []
    # Generate opening <details> tag
    out.append('<details>')
    # and the summary tag with the name:
    out.append(f'<summary>{name}</summary>')
    out.append('<div class="gallery">')

    # Add the image tags
    for img in image_paths:
        out.append(create_img_tag(img, 1 if name == "root" else 2))

    # close the details tag
    out.append('</div>')
    out.append("</details>")

    return out


def main():
    parser = argparse.ArgumentParser(
        prog="ImgInserter",
        description="Fills img elements into the html file for the pictures page"
    )

    parser.add_argument("html_file",
                        help="HTML file to be modified")
    parser.add_argument("img_dir",
                        help="""Directory where images are stored;
                        must be in the same directory as the HTML file""")

    args = parser.parse_args()

    html_path = get_html_path(args)

    image_dir = get_image_path(args)

    images = find_images(image_dir)

    with FileInput(html_path, inplace=True) as html:
        for line in html:
            if "Images go below" in line:  # Insert imgs here
                print(line, end='')
                for (section_name, paths) in images:
                    for line in create_section(section_name, paths):
                        print(line)
            else:
                print(line, end='')


if __name__ == "__main__":
    main()
