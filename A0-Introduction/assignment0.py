# CS6475 - Fall 2022

# These are the only libraries you may use. No additional imports are allowed.
import cv2
import numpy as np


""" Assignment 0 - Introduction

This file has a number of basic image handling functions that you need
to write python3 code for in order to complete the assignment. We will
be using these image processing skills throughout the course, and this assignment helps
to familiarize yourself with the cv2 and numpy libraries. Please write
the appropriate code, following the instructions in the docstring for each
function. Make sure that you know which commands and libraries you may or may
not use.

GENERAL RULES:
saves, shows, displays, prints, or writes
    over the image
    1. DO NOT INCLUDE CODE THAT PRINTS, SAVES, DISPLAYS IMAGES, OR 
    WRITES OVER THE INPUT IMAGE that you are being passed in. Any code line that 
    you may have in your code to complete these actions must be commented out 
    when you turn in your code. These actions may cause the autograder to crash
    or run slowly, possibly exceeding the time limit of 10 minutes, 
    which will count as one of your limited attempts.

    2. DO NOT IMPORT ANY OTHER LIBRARIES aside from the ones that we
    provide above. If you do, you will error out the Autograder, counting as
    one of your attampts. You can complete the assignment with the given libraries.

    3. DO NOT CHANGE THE FORMAT OF THIS FILE. You may NOT change function
    type signatures (not even named parameters with defaults). You may add
    additional code to this file at your discretion, however it is your
    responsibility to ensure that the autograder accepts your submission. Any changes 
    you make outside the areas annotated for student code must not impact your 
    performance on the autograder, or the operation of the autograder as designed.

    4. THIS FILE HAS ONLY BEEN TESTED IN THE COURSE ENVIRONMENT, (CS6475).
    You are responsible for ensuring that your code executes properly in the
    course environment and in the Gradescope autograder. 
    
    Thank you.
"""


def returnYourName():
    """ When it is called, this function should return your official name as
    shown on your Gradescope Account for full credit.
    
    If you are not sure what name to use, then the first time you submit this
    file to A0_Introduction Resources in Gradescope, the autograder will print an
    error message with your name.

    Parameters
    ----------
    input : none

    Returns
    -------
    output : a string formatted as your official name as shown on your
        Gradescope Account
    """
    return "Andrew Samuel Parmar"


def imageDimensions(image):
    """ This function takes your input image and returns its array shape.
    You may use a numpy command to find the shape.

    Parameters
    ----------
    image : numpy.ndarray
        A 3-channel color (BGR) image, 200kB or less, 
        represented as a numpy array of dimensions (HxWxD) and type np.uint8
    
    Returns
    ----------
    tuple:  tuple of numpy integers of type np.int
        the tuple returns the shape of the image ordered as
        (rows, columns, channels)
    """
    return image.shape
    
def imageSize(image):
    """ This function takes your input image and returns its array size,
    which is the total number of pixels used by all three channels.
    You may use a numpy command to find the size.

    Parameters
    ----------
    image : numpy.ndarray
        A 3-channel color (BGR) image, 200kB or less, 
        represented as a numpy array of dimensions (HxWxD) and type np.uint8
        
    Returns
    ----------
    integer:  integer value of the total number of elements in your image
    """
    return image.size
    
def myFilter():
    """ This function returns the 2D (H, W) filter that you are using in 
    the report. Enter values or calculations to generate your filter,
    as appropriate.
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    filter : numpy.ndarray
        A 2D (H, W) numpy array of variable dimensions, with type np.float64.
        The filter must be square (H = W).
        The dimensions must be odd (H % 2 = 1), where % is the modular operator.
        https://www.w3schools.com/python/trypython.asp?filename=demo_oper_mod
        The filter elements should sum to:
        *  1 for most filters  
        *  0 for edge filters
    """
    n = 7
    return np.ones((n, n), dtype=np.float64) * 1/(n**2)

def convolutionManual(image, filter):
    """ This function takes your input color (BGR) image and any square, symmetrical
    filter with odd dimensions and convolves them. MAKE SURE YOUR CODE PERFORMS 
    CONVOLUTION, NOT CORRELATION. The difference is small but important.
    
    The returned image must be the same size and type as the input image. We will 
    input different filters in the autograder tests, do not hard-code the filter.

    YOUR CODE MUST USE LOOPS (it will be slower) and move the filter past each pixel
    of your image to determine the new pixel values. We assign this exercise to help
    you understand what filtering does and exactly how it is applied to an image.
    Almost every assignment will involve filtering, this is essential understanding.

    **************** FORBIDDEN COMMANDS ******************
    NO CV2 COMMANDS AT ALL MAY BE USED IN THIS FUNCTION
    NO NUMPY CONVOLVE OR STRIDES COMMANDS
    In general, no use of commands that do your homework for you.
    The use of forbidden commands may result in a zero score
    and an honor code violation review.
    
    We will review the code from this function during grading.
    If we find that you are using any commands that are 
    forbidden here, you may receive a zero for the assignment 
    and it will be reviewed for an honor code violation.    
    ******************************************************

    Follow these steps:
    (1) Copy the image into a new array, so that you do not write over the image.
        Change the type to float64 for calculations.
    (2) From the shape of the filter, determine how many rows of padding you need.
    (3) Pad the copied image with "mirrored" padding. You must use the correct
        amount of padding of the correct type. For example: if a 7x7 filter is
        used you will require three rows/columns of padding around the image.
        A mirrored padding row will look like:

            image row [abcdefgh] ====> padded image row [cba|abcdefgh|hgf]

        Note1: If you use np.pad for this, each channel must be filtered separately.

    (4) Convolve, passing the filter (kernel) through all of the padded image.
        Save new pixel values in the result array. Don't overwrite the padded image!
    (5) Use numpy.rint to round your values after convolution is completed.
    (6) Convert to the required output type.

    Parameters
    ----------
    image : numpy.ndarray
        A 3-channel color (BGR) image, 300kB or less, represented as a numpy array of 
        dimensions (H, W, channels) and type np.uint8
    filter_rot : numpy.ndarray
        A 2D numpy array of variable dimensions, with type np.float.
        The filter (also called kernel) will be square and symmetrical,
        with odd values. Your code should be able to handle
        any filter that fits this description.
    Returns
    ----------
    image:  numpy.ndarray
        a convolved numpy array with the same dimensions (H, W, ch) as the input image
        with type np.uint8.
    """
    # copy and cast image
    img = image.copy()
    img_64 = image.astype(np.float64)

    # cast filter and transform
    filter_rot = np.rot90(filter.astype(np.float64), 2)
    filter_h = filter_rot.shape[0]
    # using: 2k + 1 = filter_height, and solving for k
    padding = int((filter_h - 1) / 2)

    # Pad image
    npad = ((padding, padding), (padding, padding), (0, 0))
    img_mirror = np.pad(img_64, npad, mode='symmetric')

    result = np.zeros_like(img, dtype=np.float64)
    h, w, channels = img.shape
    for row in range(padding, padding+h):
        for col in range(padding, padding+w):
            for ch in range(channels):
                row_start = row-padding
                row_end = row+padding+1
                col_start = col-padding
                col_end = col+padding+1

                tmp = img_mirror[row_start:row_end, col_start:col_end, ch] * filter_rot
                result[row-padding][col-padding][ch] = tmp.sum()

    result = np.rint(result.astype(np.float64))
    return result.astype(np.uint8)


def convolutionCV2(image, filter):
    """ This function performs convolution on your image using a square,
    symmetrical odd-dimension 2D filter. Use cv2 commands to complete this
    function. See the opencv docs for the version of cv2 used in the class env.
    Opencv has good tutorials for image processing.

    *** Hint: You may use cv2.filter2D for this function, but you must closely
        read the docs. You are performing convlution, not cross correlation. 

    Follow these steps:
    (1) same as convolutionManual.
    (2) Ensure your padding is in the same mirrored style as the manual version,
        which must match this format:
            
            image row [abcdefgh] ====> padded image row [cba|abcdefgh|hgf]
            
        Warning: With opencv commands you may not need to code the padding, which
        is determined by the Border Type value. Numpy and cv2 use different names 
        for this style of padding. 
    (3) Complete the convolution. 
    (4) Process your image array to meet the return requirements

    Parameters
    ----------
    image : numpy.ndarray
        A 3-channel color (BGR) image, 300kB or less, 
        represented as a numpy array of dimensions (HxWxD) and type np.uint8
    filter : numpy.ndarray
        A 2D numpy array of variable dimension values and type np.float.
        The filter will be square and symmetrical, with odd values. 
        Your code should be able to handle any filter that
        fits this description.
    Returns
    ----------
    image:  numpy.ndarray
        a convolved numpy array with the same dimensions as the input image and
        type np.uint8.
    """
    img = image.copy()
    img_64 = img.astype(np.float64)

    # using: 2k + 1 = filter_height, and solving for k
    filter_flipped = cv2.flip(filter.astype(np.float64), flipCode=-1)
    # filter_h = filter.shape[0]
    # padding = int((filter_h - 1) / 2)

    result = cv2.filter2D(img_64, ddepth=-1, kernel=filter_flipped, borderType=cv2.BORDER_REFLECT)
    result = np.rint(result.astype(np.float64))
    return result.astype(np.uint8)


# ----------------------------------------------------------
if __name__ == "__main__":
    """ YOU MAY USE THIS AREA FOR CODE THAT ALLOWS YOU TO TEST YOUR FUNCTIONS.
    This section will not be graded, you can change or delete the code below.
    You may test your code from separate files. We do not collect those files.

    When you are ready to test your code on the autograder, it is safest to
    comment out any code below, along with any print statements you may have in 
    your functions. Code here, such as extra import statements OR 
    prints (like a line for each pixel), may cause the autograder to crash, 
    which will cost you a try!
    """
    print(returnYourName())

    # read in your image, change image format to match. Uncomment useful lines.
    image = cv2.imread("images/source/image.png")
    # image = cv2.imread("toy_image.png")
    print(imageDimensions(image))
    print(imageSize(image))

    # Create a small random toy image for testing, and save it.
    # image = np.random.randint(0, 255, (5, 4, 3), dtype=(np.uint8))
    # cv2.imwrite("image.png", image)
    my_filter = myFilter()
    print('sum of filter elements =', np.sum(my_filter))

    img_manual = convolutionManual(image, my_filter)
    cv2.imwrite('images/output/convolveManual.png', img_manual)

    img_cv2 = convolutionCV2(image, my_filter)
    cv2.imwrite('images/output/convolveCV2.png', img_cv2)

    assert np.all(img_manual[:,:,:] == img_cv2[:,:,:])

    pass