# This script automatically inserts img elements into
# the html file for the pictures page.

import glob
from pathlib import Path
import argparse
from fileinput import FileInput
from sys import exit

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

# Find the path to the HTML file
html_path = glob.glob(args.html_file)
if len(html_path) == 0:
    print("HTML file provided cannot be found")
    exit(1)
html_path = Path(html_path[0])  # Shadow original html_path, now a Path

# Find the image directory
image_dir = glob.glob(args.img_dir)
if len(image_dir) == 0:
    print("Image directory cannot be found")
    exit(1)
image_dir = Path(image_dir[0])  # Shadow original image_dir, now a Path

# Find all images in the image directory
images = list(image_dir.rglob("*.png")) + \
    list(image_dir.rglob("*.jpg")) + \
    list(image_dir.rglob("*.jpeg"))

# Generate the img tag for each file
imgs = []
for i in images:
    src = str(i.relative_to(i.parents[1]))
    imgs.append(f'<img src="{src}" />')

with FileInput(html_path, inplace=True) as html:
    for line in html:
        if "Images go below" in line:  # Insert imgs here
            print(line, end='')
            for img in sorted(imgs):
                print(img)
        else:
            print(line, end='')
