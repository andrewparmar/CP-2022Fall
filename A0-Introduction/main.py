"""
You can use this file to execute your code. You are NOT required
to use this file, and ARE ALLOWED to make ANY changes you want in
THIS file. This file will not be submitted with your assignment
or report.

DO NOT SHARE CODE (INCLUDING TEST CASES) WITH OTHER STUDENTS.
"""

import cv2
import numpy as np
import os
import errno
from assignment0 import imageDimensions, imageSize, myFilter, convolutionManual, convolutionCV2

SRC_FOLDER = "images/source"
OUT_FOLDER = "images/output"


def main(image, out_path):
    """ Apply convolution(s) to a given image"""

    print("image shape =",imageDimensions(image))
    
    # check image size
    image_size = imageSize(image) / 1000
    print('image_size =', image_size, 'kB')
        
    my_filter = myFilter()
    print('sum of filter elements =', np.sum(my_filter))

    conv_manual = convolutionManual(image, my_filter)
    conv_cv2 = convolutionCV2(image, my_filter)

    out_manual = os.path.join(out_path, 'convolveManual.png')
    out_cv2 = os.path.join(out_path, 'convolveCV2.png')

    cv2.imwrite(out_manual, conv_manual)
    cv2.imwrite(out_cv2, conv_cv2)
    print('images created in', out_path,' folder')


if __name__ == '__main__':
    """ Apply convolution to single image in all folders below SRC_FOLDER
    """

    subfolders = os.walk(SRC_FOLDER)
    
    for dirpath, dirnames, fnames in subfolders:

        image_dir = os.path.split(dirpath)[-1]
        output_dir = os.path.join(OUT_FOLDER)

        print("Processing files in '" + image_dir + "' folder...")

        try:
            os.makedirs(output_dir)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        # the source folder should contain a single image of type .png or .jpg
        image_name = os.path.join(dirpath, fnames[0])
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)

        main(image, output_dir)
