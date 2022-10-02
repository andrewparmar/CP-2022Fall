# Project 1 - Spring 2022

import numpy as np
import scipy as sp
import cv2
import scipy.signal  # option for a 2D convolution library
from matplotlib import pyplot as plt  # optional
np.set_printoptions(edgeitems=30, linewidth=100000)

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
        self.curr_image = self.image
        self.mask = self._setup_binary_mask(mask)
        self.curr_mask = self.mask
        self.window = window
        self.patch_area = window[0] * window[1]
        self.alpha = 255
        self._setup_maps()
        self.iteration = 0

    def _setup_maps(self):
        self.confidence_map = np.ones_like(self.mask, dtype=np.float32)
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

            # get patch with max priority
            priority_patch = self.priority_patch
            priority_point = self.priority_point

            # find exemplar in source_region that minimizes distance func
            # * use template matching first, then try something more fancy
            self._find_best_matching_exemplar()

            # copy image data from source to target region

            # update confidence scores
            self._update_confidence()

            # update mask
            self._update_curr_mask()

            self.iteration += 1

    def is_pending_target_region(self):
        # TODO: Silence this "pending" calculation
        tmp = self.curr_mask/255
        h, w = self.curr_mask.shape
        pending = (tmp.sum() / (h * w)) * 100
        print(f"% Pending {pending:.2}")
        return self.curr_mask.any()

    def compute_mask_boundary(self, mask):
        """
        Passing in a mask instead of using self.mask, since the mask should be updated in each iteration
        """
        # ret, thresh = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)
        blur = cv2.GaussianBlur(mask, (5, 5), 0)
        ret3, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # self.image_boundary = contours[0]

        # TODO debug output
        # out = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        out = cv2.cvtColor(np.zeros_like(thresh), cv2.COLOR_GRAY2BGR)
        self.contour_img = cv2.drawContours(out, contours, -1, (255, 0, 0), thickness=1)  # the colors are (R,G,B)
        # plt.imshow(self.contour_img); plt.show()

        # use laplacian operator instead. Countours gives a thicker boundary. Laplace is a single layer.
        # fill_front_indices = cv2.Laplacian(thresh, -1, ksize=3)
        # fill_front = np.column_stack(fill_front_indices)
        fill_front = contours[0]
        fill_front.resize((fill_front.shape[0], 2))
        return fill_front

    def _compute_priority(self, fill_front):
        # reusable calculations
        self._compute_point_normals()

        priorities = []
        max_priority = float("-inf")
        self.priority_point = None
        self.priority_patch = None
        self.priority_confidence = None
        for point in fill_front:
            patch_coords = self._get_patch_coordinates(point)
            c_point = self._calculate_confidence(patch_coords)
            d_point = self._calculate_data(point, patch_coords)

            priority = c_point * d_point
            if priority > max_priority:
                max_priority = priority
                self.priority_point = point
                self.priority_patch = patch_coords
                self.priority_confidence = c_point
            priorities.append((priority, point))
        # print(priorities[:10])

    def _get_patch_coordinates(self, point):
        """
        Get boundary coordinates of the patch window centered at "point"
        x1, y1 are the coordinates of the top left
        x2, y2 are the coordinates of the bottom right
        """
        h, w = self.mask.shape
        c, r = point
        k = self.window[0] // 2
        x_1 = max(0, r - k)
        y_1 = max(0, c - k)
        x_2 = min(h, r + k)
        y_2 = min(w, c + k)

        return x_1, y_1, x_2, y_2

    def _calculate_confidence(self, patch_coords):
        x_1, y_1, x_2, y_2 = patch_coords
        confidence = self.confidence_map[x_1:x_2+1, y_1:y_2+1].sum()
        patch_area = (x_2-x_1) * (y_2-y_1)
        # return confidence / self.patch_area # TODO: update patch area to use patch window size
        return confidence / patch_area

    def _calculate_data(self, point, patch_coords):
        max_gradient_orth = self._compute_image_patch_gradient(patch_coords)
        max_normal = self.unit_normal[point[0], point[1]]
        data = np.abs(max_gradient_orth.dot(max_normal))/self.alpha
        return data

    def _compute_point_normals(self):
        _, binary_mask = cv2.threshold(self.curr_mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        grad_x = cv2.Sobel(~binary_mask, cv2.CV_32F, 1, 0, ksize=3, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(~binary_mask, cv2.CV_32F, 0, 1, ksize=3, borderType=cv2.BORDER_DEFAULT)

        grad_x_unit = grad_x / grad_x.max()
        grad_y_unit = grad_y / grad_y.max()

        self.unit_normal = np.dstack((np.abs(grad_x_unit), np.abs(grad_y_unit)))
        # The normal will be magnitude 1 at all points on the frontier. What matters then is the difference of angle
        # between the contour normal and the image gradient normal.

    def _compute_image_patch_gradient(self, patch_coords):
        x_1, y_1, x_2, y_2 = patch_coords
        mask_patch = self.curr_mask[x_1:x_2 + 1, y_1:y_2 + 1]
        image_patch = self.curr_image[x_1:x_2 + 1, y_1:y_2 + 1]

        image_gray = cv2.cvtColor(image_patch, cv2.COLOR_BGR2GRAY)

        grad_x = cv2.Sobel(image_gray, cv2.CV_32F, 1, 0, ksize=3, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(image_gray, cv2.CV_32F, 0, 1, ksize=3, borderType=cv2.BORDER_DEFAULT)
        grad_x_orth = grad_y
        grad_y_orth = -grad_x
        gradient_orth = np.dstack((grad_x_orth, grad_y_orth))

        # maybe calculate the gradient in the patch first. Use regular or orthonormal, it's the same.
        gradient_mag = np.sqrt((grad_x**2 + grad_y**2))

        # Then mask it off and take the max.
        # Dilate the mask to avoid the gradient between the source and the frontier.
        # Just take off 1 pixel along the frontier. TODO: do we need two pixels off?
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilated_mask = cv2.dilate(mask_patch, kernel, iterations=1)
        gradient_mag[dilated_mask == 255] = 0

        loc = np.unravel_index(np.argmax(gradient_mag, axis=None), gradient_mag.shape)

        return gradient_orth[loc]

    def _find_best_matching_exemplar(self):
        x_1, y_1, x_2, y_2 = self.priority_patch
        foo = self.contour_img.copy()
        x, y = self.priority_point
        foo[y, x, :] = (0, 255, 0)
        if not self.iteration % 10:
            plt.imshow(cv2.cvtColor(foo, cv2.COLOR_BGR2RGB)); plt.show()

        template = self.curr_image[x_1:x_2 + 1, y_1:y_2 + 1, :]
        mask = self.curr_mask[x_1:x_2 + 1, y_1:y_2 + 1]
        mask_tmp = mask.reshape(9, 9, 1).repeat(3, axis=2)

        img_tmp = self.curr_image.copy()
        img_tmp[x_1:x_2 + 1, y_1:y_2 + 1, :] = 0
        res = cv2.matchTemplate(img_tmp, template, cv2.TM_SQDIFF, None, ~mask_tmp)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        baz = self.curr_image[min_loc[1]:min_loc[1]+9, min_loc[0]:min_loc[0]+9, :].copy()
        # self.curr_image[x_1:x_2 + 1, y_1:y_2 + 1] = baz  # applying full matched template to patch.
        # self.curr_image[x_1:x_2 + 1, y_1:y_2 + 1,:][mask_tmp==255] = baz  # applying full matched template to patch.
        # baz[mask_tmp == 255] = 0 # black out mask area to see how patch is applied.
        self.curr_image[x_1:x_2 + 1, y_1:y_2 + 1][mask_tmp == 255] = baz[mask_tmp == 255] # applies pixel values ot the masked area.

        # TODO: Debug show rectangle around match location
        top_left = min_loc
        h, w = template.shape[:2]
        bottom_right = (top_left[0] + w, top_left[1] + h)
        img_tmp[x_1:x_2 + 1, y_1:y_2 + 1] = mask_tmp
        img_tmp[y, x, :] = (0, 255, 0)
        cv2.rectangle(img_tmp, top_left, bottom_right, 255, 2)
        if not self.iteration % 10:
            plt.imshow(cv2.cvtColor(img_tmp, cv2.COLOR_BGR2RGB)); plt.show()
            plt.imshow(cv2.cvtColor(self.curr_image, cv2.COLOR_BGR2RGB));plt.show()
        pass

    def _update_confidence(self):
        x_1, y_1, x_2, y_2 = self.priority_patch
        mask = self.curr_mask[x_1:x_2 + 1, y_1:y_2 + 1]
        self.confidence_map[x_1:x_2+1, y_1:y_2+1][mask == 255] = self.priority_confidence

    def _update_curr_mask(self):
        x_1, y_1, x_2, y_2 = self.priority_patch
        self.curr_mask[x_1:x_2 + 1, y_1:y_2 + 1] = 0



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