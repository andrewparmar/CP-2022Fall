# CS6475 - Fall 2022

import numpy as np
import scipy as sp
import cv2
import scipy.signal                     # option for a 2D convolution library
from matplotlib import pyplot as plt    # for optional plots

import copy


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
    # WRITE YOUR CODE HERE.
    
    raise NotImplementedError


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

def beach_back_removal(image, seams=300, redSeams=False):
    """ Use the backward method of seam carving from the 2007 paper to remove
   the required number of vertical seams in the provided image. Do NOT hard-code the
    number of seams to be removed.
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


def dolphin_back_insert(image, seams=100, redSeams=False):
    """ Similar to Fig 8c and 8d from 2007 paper. Use the backward method of seam carving to 
    insert vertical seams in the image. Do NOT hard-code the number of seams to be inserted.
    
    This function is called twice:  dolphin_back_insert with redSeams = True
                                    dolphin_back_insert without redSeams = False
    """
    # WRITE YOUR CODE HERE.

    raise NotImplementedError


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