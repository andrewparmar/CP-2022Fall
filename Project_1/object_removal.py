# Project 1 - Spring 2022

import numpy as np
import scipy as sp
import cv2
import scipy.signal                     # option for a 2D convolution library
from matplotlib import pyplot as plt    # optional 

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
    """ This function returns your name as shown on your Gradescope Account.
    """
    # WRITE YOUR CODE HERE.
    
    raise NotImplementedError


def objectRemoval(image, mask, setnum=0, window=(9,9)):
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

    # WRITE YOUR CODE HERE.

    raise NotImplementedError
 
