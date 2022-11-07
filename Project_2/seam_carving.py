# CS6475 - Fall 2022

import numpy as np
import scipy as sp
import cv2
import scipy.signal                     # option for a 2D convolution library
from matplotlib import pyplot as plt    # for optional plots

import copy
import time

""" Project 2: Seam Carving

This file has a number of functions that you need to fill out in order to
complete the assignment. Please write the appropriate code, following the
instructions on which functions you may or may not use.

References
----------
See the following papers, available in Canvas under Files:

(1) "Seam Carving for Content-Aware Image Resizing"
    Avidan and Shamir, 2007

(2) "Improved Seam Carving for Video Retargeting"
    Rubinstein, Shamir and Avidan, 2008

FORBIDDEN:
    1. OpenCV functions SeamFinder, GraphCut, and CostFunction are
    forbidden, along with any similar functions that may be in the class environment.
    2. Numeric Metrics functions of error or similarity; e.g. SSIM, RMSE.
    These must be coded from their mathematical equations. Write your own versions.

GENERAL RULES:
    1. ALL CODE USED IN THIS ASSIGNMENT to generate images, red-seam images,
    differential images, and comparison metrics must be included in this file.
    2. YOU MAY NOT USE any library function that essentially completes
    seam carving or metric calculations for you. If you have questions on this,
    ask on Ed. **Usage may lead to zero scores for the project and review
    for an honor code violation.**
    3. DO NOT CHANGE the format of this file. You may NOT change existing function
    signatures, including the given named parameters with defaults.
    4. YOU MAY ADD FUNCTIONS to this file, however it is your responsibility
    to ensure that the autograder accepts your submission.
    5. DO NOT IMPORT any additional libraries other than the ones imported above.
    You should be able to complete the assignment with the given libraries.
    6. DO NOT INCLUDE code that prints, saves, shows, displays, or writes the
    images, or your results. If you have code in the functions that
    does any of these operations, comment it out before autograder runs.
    7. YOU ARE RESPONSIBLE for ensuring that your code executes properly.
    This file has only been tested in the course environment. Any changes you make
    outside the areas annotated for student code must not impact the autograder
    system or your performance.

FUNCTIONS:
    returnYourName
    IMAGE GENERATION:
        beach_back_removal
        dolphin_back_insert with redSeams=True and False
        dolphin_back_double_insert
        bench_back_removal with redSeams=True and False
        bench_for_removal with redSeams=True and False
        car_back_insert
        car_for_insert
    COMPARISON METRICS:
        difference_image
        numerical_comparison
"""


def returnYourName():
    """ This function returns your name as shown on your Gradescope Account.
    """
    return "Andrew Samuel Parmar"


# -------------------------------------------------------------------
""" IMAGE GENERATION
    *** ALL IMAGES SUPPLIED OR RETURNED ARE EXPECTED TO BE UINT8 ***
    Parameters and Returns are as follows for all of the removal/insert
    functions:

    Parameters
    ----------
    image : numpy.ndarray (dtype=uint8)
        Three-channel image of shape (r,c,ch).
    seams : int
        Integer value of number of vertical seams to be inserted or removed.
        NEVER HARDCODE THE NUMBER OF SEAMS, we check other values in the autograder.
    redSeams : boolean
        Boolean variable; True = produce a red seams image, False = no red seams

    Returns
    -------
    numpy.ndarray (dtype=uint8)
        An image of shape (r, c_new, ch) where c_new = new number of columns.
        Make sure you deal with any needed normalization or clipping, so that
        your image array is complete on return.
"""


class BaseSeamCarver:
    pass


class BackwardSeamCarver(BaseSeamCarver):
    def __init__(self, image, seam_count, red_seams=False, scale=False):
        self.image = self._setup_image(image, scale)
        self.seam_count = seam_count
        self.working_image = self.image.copy()
        self.viz_delay = 10
        self.seam_image = None
        self.pos_map = self._setup_pos_map()
        self.mask = np.zeros_like(self.pos_map, dtype=bool)
        self.red_seams = red_seams
        self.cum_offset = None

    def _setup_image(self, image, scale):
        scale_factor = 0.75
        if scale:
            image = cv2.resize(
                image, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA
            )
        return image

    def _setup_pos_map(self):
        h, w, _ = self.image.shape
        map = np.zeros((h, w), dtype=tuple)
        for i in range(h):
            for j in range(w):
                map[i, j] = (i, j)
        return map

    def get_energy_map_sobel(self, image):
        b, g, r = cv2.split(image)
        b_energy = np.absolute(cv2.Sobel(b, -1, 1, 0)) + np.absolute(cv2.Sobel(b, -1, 0, 1))
        g_energy = np.absolute(cv2.Sobel(g, -1, 1, 0)) + np.absolute(cv2.Sobel(g, -1, 0, 1))
        r_energy = np.absolute(cv2.Sobel(r, -1, 1, 0)) + np.absolute(cv2.Sobel(r, -1, 0, 1))
        return b_energy + g_energy + r_energy

    def get_lowest_cumulative_energy(self, energy_map):
        h, w = energy_map.shape
        M = np.zeros((h, w))
        # Set top row to energy map top row
        M[0, :] = energy_map[0, :]

        for i in range(1, h):
            for j in range(w):
                M[i, j] = energy_map[i, j] + \
                          min(M[i - 1, max(0, j - 1)], M[i - 1, j], M[i - 1, min(w-1, j + 1)])

        return M

    def get_lowest_energy_seam(self, M):
        h, w = M.shape
        seam = np.zeros(h, dtype=np.int64)
        seam[-1] = np.argmin(M[-1, :])
        prev_j = seam[-1]

        for i in range(h - 2, -1, -1):
            min_val = np.inf
            min_col = None
            for nc in [(prev_j - 1), prev_j, (prev_j + 1)]:
                if 0 <= nc < w and M[i, nc] < min_val:
                    min_val = M[i, nc]
                    min_col = nc
            seam[i] = min_col
            prev_j = seam[i]
        return seam

    def plot_seam(self, image, seam_cells):
        self.seam_image = image.copy()
        for i, j in enumerate(seam_cells):
            self.seam_image[i, j, :] = (0, 0, 255)

        # img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # plt.imshow(img_rgb); plt.show()
        # cv2.imshow("window1", self.seam_image)
        # cv2.waitKey(1000)

    def remove_seam(self, image, seam_cells):
        # img_cp = image.copy()
        for i, j in enumerate(seam_cells):
            image[i, j:-1, :] = image[i, j + 1:, :]

        image = image[:, :-1, :]

        # img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # plt.imshow(img_rgb); plt.show()
        foo = np.hstack((self.seam_image, image))
        cv2.imshow("Removal", foo)
        cv2.waitKey(self.viz_delay)

        return image

    def remove_seam_from_map(self, seam_cells):
        for i, j in enumerate(seam_cells):
            self.pos_map[i, j:-1] = self.pos_map[i, j + 1:]

        self.pos_map = self.pos_map[:, :-1]

    def add_seam(self, image, seam_cells):
        h, w, d = image.shape
        extra_col = np.zeros((h, 1, d), dtype=image.dtype)
        new_img = np.concatenate((image, extra_col), axis=1)
        for i, j in enumerate(seam_cells):
            # shift pixels in new_img to make room for new seam
            # seam pixels are shifted to the right
            new_img[i, j + 2:, :] = image[i, j+1:, :]

            # calculate avg of seam's neighboring pixels.
            l = j
            r = j + 2 #TODO: consider using min(j+2, w)
            if l >= 0:
                l_val = image[i, l, :]
            else:
                l_val = 0
            if r < image.shape[1]:
                r_val = image[i, r, :]
            else:
                r_val = 0
            avg_vals = np.mean([l_val, r_val], axis=0)

            new_img[i, j, :] = avg_vals

        image = new_img

        # img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # plt.imshow(img_rgb); plt.show()
        foo = np.hstack((self.seam_image, image))
        cv2.imshow("Insertion", foo)
        cv2.waitKey(self.viz_delay)

        return image

    def mark_mask(self, seam):
        for r, c in enumerate(seam):
            i, j = self.pos_map[r, c]
            self.mask[i, j] = 1

    def apply_red_seams(self, image):
        image[:, :, 0][self.mask] = 0
        image[:, :, 1][self.mask] = 0
        image[:, :, 2][self.mask] = 255
        return image
        # foo = np.repeat(np.atleast_3d(self.mask), 3, axis=2)
        # image[foo] = (0, 0, 255)
        # return image

    def _reduce(self):
        seam_list = []

        for count in range(self.seam_count):
            loop_start = time.time()
            print(f"Removing seam #{count}")
            img_f64 = self.working_image.astype(np.float64)
            start = time.time()
            energy_map = self.get_energy_map_sobel(img_f64)
            print("energy_map", time.time() - start)

            start = time.time()
            M = self.get_lowest_cumulative_energy(energy_map)
            print("cumulative map", time.time() - start)

            start = time.time()
            seam_cells = self.get_lowest_energy_seam(M)
            print("get seam", time.time() - start)
            seam_list.append(seam_cells)

            self.plot_seam(self.working_image, seam_cells)

            self.working_image = self.remove_seam(self.working_image, seam_cells)
            self.mark_mask(seam_cells)
            self.remove_seam_from_map(seam_cells)

            print("Loop time", time.time() - loop_start)

        return seam_list

    def run_removal(self):
        seam_list = self._reduce()

        if self.red_seams:
            red_seam_image = self.apply_red_seams(self.image.copy())
            return red_seam_image

        return self.working_image

    def _mask_insert(self, seam_cells):
        h, w = self.mask.shape
        extra_col = np.zeros((h, 1), dtype=self.mask.dtype)
        new_mask = np.concatenate((self.mask, extra_col), axis=1)
        for i, j in enumerate(seam_cells):
            # shift pixels in new_img to make room for new seam
            # pixels to the right of the seam are shifted 1 pixel over to the right
            new_mask[i, j + 2:] = self.mask[i, j+1:]
            new_mask[i, j+1] = 0
            new_mask[i, j] = 1

        self.mask = new_mask.copy()
        # TODO: visualize mask with cv2.imshow.

    def update_seams(self, seam_list, curr_seam):
        new_seam_list = []
        for seam in seam_list:
            new_seam = seam.copy()
            new_seam[np.where(seam > curr_seam)] = new_seam[np.where(seam > curr_seam)] + 2
            new_seam_list.append(new_seam)
        return new_seam_list

    def run_insert(self):
        # Revers the list because we are using pop in the while loop below.
        seam_list = self._reduce()[::-1]

        self.cum_offset = np.cumsum(self.mask, axis=1) - 1
        self.mask = np.zeros_like(self.image[:,:,0], dtype=bool)

        self.working_image = self.image.copy()
        while seam_list:
            seam = seam_list.pop()
            # seam = self.get_offset_seam(seam)
            self.working_image = self.add_seam(self.working_image, seam)
            self._mask_insert(seam)
            seam_list = self.update_seams(seam_list, seam)

        return self.working_image

class ForwardSeamCarver(BaseSeamCarver):
    pass


def beach_back_removal(image, seams=300, redSeams=False):
    """ Use the backward method of seam carving from the 2007 paper to remove
    the required number of vertical seams in the provided image. Do NOT hard-code the
    number of seams to be removed.
    """
    # TODO: adjust the input args and kwargs that are hardcoded.
    handler = BackwardSeamCarver(image, seam_count=seams, red_seams=True, scale=True)
    res = handler.run_removal()

    return res


def dolphin_back_insert(image, seams=100, redSeams=False):
    """ Similar to Fig 8c and 8d from 2007 paper. Use the backward method of seam carving to
    insert vertical seams in the image. Do NOT hard-code the number of seams to be inserted.

    This function is called twice:  dolphin_back_insert with redSeams = True
                                    dolphin_back_insert without redSeams = False
    """
    handler = BackwardSeamCarver(image, seam_count=seams, red_seams=False)
    res = handler.run_insert()

    return res


def dolphin_back_double_insert(image, seams=100, redSeams=False):
    """ Similar to Fig 8f from 2007 paper. Use the backward method of seam carving to
    insert vertical seams by performing two insertions, each of size seams, in the image.
    i.e. insert seams, then insert seams again.
    Do NOT hard-code the number of seams to be inserted.
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


def bench_back_removal(image, seams=225, redSeams=False):
    """ Similar to Fig 8 from 2008 paper. Use the backward method of seam carving to
    remove vertical seams in the image. Do NOT hard-code the number of seams to be removed.

    This function is called twice:  bench_back_removal, redSeams = True
                                    bench_back_removal, redSeams = False
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


def bench_for_removal(image, seams=225, redSeams=False):
    """ Similar to Fig 8 from 2008 paper. Use the forward method of seam carving to
    remove vertical seams in the image. Do NOT hard-code the number of seams to be removed.

    This function is called twice:  bench_for_removal, redSeams = True
                                    bench_for_removal, redSeams = False
  """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


def car_back_insert(image, seams=170, redSeams=False):
    """ Fig 9 from 2008 paper. Use the backward method of seam carving to insert
    vertical seams in the image. Do NOT hard-code the number of seams to be inserted.
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


def car_for_insert(image, seams=170, redSeams=False):
    """ Similar to Fig 9 from 2008 paper. Use the forward method of seam carving to
    insert vertical seams in the image. Do NOT hard-code the number of seams to be inserted.
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


# __________________________________________________________________
""" COMPARISON METRICS
    There are two functions here, one for visual comparison support and one
    for a quantitative metric.
"""


def difference_image(result_image, comparison_image):
    """ Take two images and produce a difference image that best visually
    indicates how and where the two images differ in pixel values.

    Parameters
    ----------
    result_image, comparison_image : numpy.ndarray (dtype=uint8)
        two BGR images of the same shape (r,c,ch)

    Returns
    -------
    numpy.ndarray (dtype=uint8)
        A BGR image of shape (r, c, ch) representing the differences between two
        images.

    NOTES: MANY ERRORS IN PRODUCING DIFFERENCE IMAGES RELATE TO THESE ISSUES
        1) Do your calculations in floats, so that data is not lost.
        2) Before converting back to uint8, complete any necessary scaling,
           rounding, or clipping.
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


def numerical_comparison(result_image, comparison_image):
    """ Take two images and produce one or two single-value metrics that
    numerically best indicate(s) how different or similar two images are.
    Only one metric is required, you may submit two, but no more.

    If your metric produces a result indicating a total number of pixels, or values,
    formulate it as a ratio of the total pixels in the image. This supports use
    of your results to evaluate code performance on different images.

    ******************************************************************
    NOTE: You may not use functions that perform the whole function for you.
    Research methods, find an algorithm (equation) and implement it. You may
    use numpy array MATHEMATICAL functions such as abs, sqrt, min, max, dot, .T
    and others that perform a single operation for you.

    FORBIDDEN: Library functions of error or similarity; e.g. SSIM, RMSE, etc.
    Use of these functions may result in zero for the assignment and review
    for an honor code violation.
    ******************************************************************

    Parameters
    ----------
    result_image, comparison_image : numpy.ndarray (dtype=uint8)
        two BGR images of the same shape (r,c,ch)

    Returns
    -------
    value(s) : float
        One or two single_value metric comparisons
        Return a tuple of values if you are using two metrics.

    NOTE: you may return only one or two values; choose the best one(s) you tried.
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


if __name__ == "__main__":
    """ You may use this area for code that allows you to test your functions.
    This section will not be graded, and is optional.

    Comment out this section when you submit to the autograder to avoid the chance
    of wasting time and attempts.
    """
    # WRITE YOUR CODE HERE

    pass
