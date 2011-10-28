# coding: utf8

import os
import Image
import glob

images_files = glob.glob("*.jpg")
output_dir = "output"

for img_file in images_files:
    file_name = os.path.splitext(img_file)[0]
    file_ext = os.path.splitext(img_file)[1]

    img = Image.open(open(img_file))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    width = img.size[0]
    half_width = img.size[0]/2
    height = img.size[1]
    left_img = img.crop((0, 0, half_width, height))
    left_img.save("%s/%s-1%s" % (output_dir, file_name, file_ext))

    right = img.crop((half_width, 0, width, height))
    right.save("%s/%s-2%s" % (output_dir, file_name, file_ext))
