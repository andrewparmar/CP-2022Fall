# Project 1 - Object Removal

# You can use this file to execute your code. You are NOT required
# to use this file, and ARE ALLOWED to make ANY changes you want in
# THIS file. This file will not be submitted with your project
# or report.

# DO NOT SHARE CODE (INCLUDING TEST CASES) WITH OTHER STUDENTS.

import cv2
import numpy as np
import os
import errno
import time

from object_removal import objectRemoval

"""
IMPORTANT TIPS:

1.  Make sure that you are using CS6475, the class env. We can't promise it
will always pass the AG since its possible that dependencies and versions
changed if you add libraries. To check, run this command in the CS6475 python env:

    pip freeze > requirements.txt

The file requirements.txt will be created. Verify you have matplotlib 3.0.1,
python 3.6.x, numpy 1.15.2, scipy 1.0.0 or reinstall your env following the
Course Setup guidance.

2.  If your laptop/ordinary desktop can produce the result images within the 2 hour
time limit, then your code should be fast enough.
Last term, the mean run time for all 3 images was 20 min, median was 6 minutes.

3.  Keep your images small. The maximum size limit is 1MB (pixel size: H x W).
We recommend staying under 500kB, and even 200kB images can perform well.

4.  Keep your mask target areas small until your code works. Don't go over 10%
of the image pixel size unless your code is fast.

5.  Attend or watch the Office Hour for this Project.
"""


# change these folders as needed
SOURCE_FOLDER = "images/source/"
OUT_FOLDER = "images/result/"


if __name__ == "__main__":
    """ Generate the 3 result images. Place your image/mask pairs in the source folder
    named above, which should be in the same directory as main.py & object_removal.py.
    Image type is assumed to be .png, but you may use .jpg with changes below.
    """
    # make the images/results folder
    output_dir = os.path.join(OUT_FOLDER)

    try:
        os.makedirs(output_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    # TODO change this back to 3.
    for i in range(4, 5):
        # image names should be input_1, input_2, input_3
        start = time.time()
        print("\nProcessing file set", i)
        image_name = SOURCE_FOLDER + 'input_' + str(i) + '.jpg'
        mask_name = SOURCE_FOLDER + 'mask_' + str(i) + '.jpg'

        image = cv2.imread(image_name)
        mask = cv2.imread(mask_name, cv2.IMREAD_GRAYSCALE)  # one channel only

        print(image_name)
        print('image', image.shape, image.size / 3e3, 'kB')
        print('mask', mask.shape)

        output = objectRemoval(image, mask, setnum=i, window=(9,9))
        cv2.imwrite(OUT_FOLDER + 'result_' + str(i) + '.png', output)
        end = time.time()
        print('image completed, elapsed time:', np.round(end-start,3))
