# Project 1 - Spring 2022

import numpy as np
import scipy as sp
import cv2
import scipy.signal  # option for a 2D convolution library
from matplotlib import pyplot as plt  # optional

''' Project 1 - Object Removal

This file has a number of functions that you need to write to complete the project.
Please follow the instructions on which functions you may or may not use.

Reference:
----------
Criminisi, A., Perez, P., & Toyama, K. (2004). Region Filling and Object Removal by
Exemplar-Based Image Inpainting. IEEE Transactions on Image Processing, 13(9).

FORBIDDEN:
    1. YOU MAY NOT USE any library function that essentially completes object removal
    or region inpainting for you. This includes:
        - OpenCV function cv2.inpaint
        - Any similar functions that may be in the class environment/other libraries.
    2. The use of other algorithms than the one presented in the paper.

    If you have questions on this, ask on Ed.


GENERAL RULES:
    1. ALL CODE USED IN THIS PROJECT to generate images must be included in this file.
    2. DO NOT CHANGE the format of this file. You may NOT change existing
        function signatures, including the given named parameters with defaults.
    3. YOU MAY ADD FUNCTIONS to this file, however it is your responsibility to ensure
        that the autograder running the class environment accepts your submission.
    4. DO NOT IMPORT any additional libraries other than the ones imported above.
        You should be able to complete the project with the given libraries.
    5. DO NOT INCLUDE code that prints, saves, displays, or writes the images
        or your results. Imshow and waitkey are particular problems. If you have code
        that does any of these operations, comment it out before autograder runs.
    6. YOU ARE RESPONSIBLE for ensuring that your code executes properly.
        This file has only been tested in the course environment.
        Any changes you make outside the areas annotated for student code must not impact
        the autograder system or your performance.

FUNCTIONS:
    returnYourName
    objectRemoval
'''


def returnYourName():
    """ This function returns your name as shown on your Gradescope Account."""
    raise "Andrew Samuel Parmar"


class ObjectRemover:
    def __init__(self, image, mask, window):
        self.image = image
        self.mask = self._setup_binary_mask(mask)
        self.curr_mask = self.mask
        self.window = window
        self.patch_area = window[0] * window[1]
        self.alpha = 255
        self._setup_maps()

    def _setup_maps(self):
        self.confidence_map = np.ones_like(self.mask)
        self.confidence_map[self.mask == 255] = 0

    @staticmethod
    def _setup_binary_mask(mask):
        k = 5
        blur = cv2.GaussianBlur(mask, (k, k), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh

    def run(self):
        # TODO should we be looking at the mask for this condition?
        while self.is_pending_target_region():
            # identify fill region
            fill_front = self.compute_mask_boundary(self.curr_mask)

            # compute priorities
            self._compute_priority(fill_front)
            break

            # get patch with max priority

            # find exemplar in source_region that minimizes distance func

            # copy image data from source to target region

            # update confidence scores

            # update mask
            # self.update_curr_mask(point)
            pass

    def _compute_priority(self, fill_front):
        priorities = []
        for point in fill_front:
            patch_coords = self._get_patch_coordinates()
            c_point = self._calculate_confidence(patch_coords)
            d_point = self._calculate_data(patch_coords)

            priority = c_point * d_point

            priorities.append((priority, point))
        print(priorities[:10])
        pass

    def _get_patch_coordinates(self, point):
        """
        Get boundary coordinates of the patch window centered at "point"
        x1, y1 are the coordinates of the top left
        x2, y2 are the coordinates of the bottom right
        """
        h, w = self.mask.shape
        r, c = point
        k = self.window[0] // 2
        x_1 = max(0, r - k)
        y_1 = max(0, c - k)
        x_2 = min(h, r + k)
        y_2 = min(w, c + k)

        return x_1, y_1, x_2, y_2

    def _calculate_confidence(self, patch_coords):
        x_1, y_1, x_2, y_2 = patch_coords
        confidence = self.confidence_map[x_1:x_2+1, y_1:y_2+1].sum()
        return confidence / self.patch_area

    def _calculate_data(self, patch_coords):
        ...


    def is_pending_target_region(self):
        # TODO: Silence this "pending" calculation
        tmp = self.curr_mask/255
        h, w = self.curr_mask.shape
        pending = (tmp.sum() / (h * w)) * 100
        print(f"% Pending {pending:.2}")
        return self.curr_mask.any()

    def update_curr_mask(self, point):
        # self.curr_mask[point]
        pass

    @staticmethod
    def compute_mask_boundary(mask):
        """
        Passing in a mask instead of using self.mask as the mask should be updated in each iteration
        """
        # ret, thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)
        blur = cv2.GaussianBlur(mask, (5, 5), 0)
        ret3, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # self.image_boundary = contours[0]

        # TODO debug output
        # out = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        # out = cv2.cvtColor(np.zeros_like(thresh), cv2.COLOR_GRAY2BGR)
        # contour_img = cv2.drawContours(out, contours, -1, (255, 0, 0), 2)
        # plt.imshow(contour_img)
        # plt.show()

        # use laplacian operator instead. Countours gives a thicker boundary. Laplace is a single layer.
        # fill_front_indices = cv2.Laplacian(thresh, -1, ksize=3)
        # fill_front = np.column_stack(fill_front_indices)
        fill_front = contours[0]
        fill_front.resize((fill_front.shape[0], 2))
        return fill_front

    def calculate_priority(self, point_tuple):
        pass


def objectRemoval(image, mask, setnum=0, window=(9, 9)):
    """ ALL IMAGES SUPPLIED OR RETURNED ARE UINT8.
    This function will be called three times; once for each of your
    image/mask pairs to produce your result images.

    Parameters and Returns are as follows for all images you process

    Parameters
    ----------
    image : numpy.ndarray (dtype=uint8)
        Three-channel color image of shape (r,c,3)

    mask: numpy.array (dtype=uint8)
        Single channel B&W image of shape (r,c) which defines the
        target region to be removed.

    setnum: (integer)
        setnum=0 is for use with the autograder
        setnum=1,2,3 are your three required image sets

    window: default = (9, 9), tuple of two integers
        The dimensions of the target window described at the beginning of
        Section III of the paper.
        You can optimize the window for each image. If you do this,
        then include the final value in your code, where it can be activated
        by setnum. Then when we run your code, we should get the same results.

    Returns
    -------
    numpy.ndarray (dtype=uint8)
        Three-channel color image of same shape as input image (r, c, 3)
        Make sure you deal with any needed normalization or clipping, so that
        your image array is complete on return.
    """
    obj_remover = ObjectRemover(image, mask, window)
    obj_remover.run()

    return np.zeros_like(image, dtype=np.uint8)