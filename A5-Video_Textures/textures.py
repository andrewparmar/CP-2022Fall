""" Video Textures

This file has a number of functions that you need to fill out in order to
complete the assignment. Please write the appropriate code, following the
instructions on which functions you may or may not use.

GENERAL RULES:
    1. DO NOT INCLUDE code that saves, shows, displays, writes the image that
    you are being passed in. Do that on your own if you need to save the images
    but the functions should NOT save the image to file.

    2. DO NOT import any other libraries aside from those that we provide.
    You may not import anything else, and you should be able to complete
    the assignment with the given libraries (and in many cases without them).

    3. DO NOT change the format of this file. You may NOT change function
    type signatures (not even named parameters with defaults). You may add
    additional code to this file at your discretion, however it is your
    responsibility to ensure that the autograder accepts your submission.

    4. This file has only been tested in the provided class environment.
    You are responsible for ensuring that your code executes properly in the
    class environment, and that any changes you make outside the
    areas annotated for student code do not impact your performance on the
    autograder system.
"""
import cv2
import numpy as np
import scipy as sp
import scipy.signal


def returnYourName():
    """When it is called, this function should return your official name as
    shown on your Gradescope Account. If you are not sure what name to use,
    when you submit this file to Gradescope, the autograder will print an
    error message with your name.
    Returns
    -------
    output : string formatted as follows: your official name in Gradescope
    """
    return "Andrew Samuel Parmar"


def videoVolume(images):
    """Create a video volume (4-d numpy array) from the image list.

    Parameters
    ----------
    images : list
        A list of frames. Each element of the list contains a numpy array
        representing a color image. You may assume that each frame has the same
        shape: (rows, cols, 3).

    Returns
    -------
    numpy.ndarray(dtype: np.uint8)
        A 4D numpy array. This array should have dimensions
        (num_frames, rows, cols, 3).
    """
    raise NotImplementedError


def computeSimilarityMetric(video_volume):
    """Compute the differences between each pair of frames in the video volume.

    The goal, of course, is to be able to tell how good a jump between any two
    frames might be so that the code you write later on can find the optimal
    loop. The closer the similarity metric is to zero, the more alike the two
    frames are.

    Loop through each pair (i, j) of start and end frames in the video volume.
    Calculate the root sum square deviation (rssd) score for each pair and
    store the value in cell (i, j) of the output:

        rssd = sum( (start_frame - end_frame) ** 2 ) ** 0.5

    Finally, divide the entire output matrix by the average value of the matrix
    in order to control for resolution differences and distribute the values
    over a consistent range.

    Hint: Remember the matrix is symmetrical, so when you are computing the
    similarity at i, j, its the same as computing the similarity at j, i so
    you don't have to do the math twice.  Also, the similarity at all i,i is
    always zero, no need to calculate it.

    Parameters
    ----------
    video_volume : numpy.ndarray
        A 4D numpy array with dimensions (num_frames, rows, cols, 3).

        This can be produced by the videoVolume function.

    Returns
    -------
    numpy.ndarray(dtype: np.float64)
        A square 2d numpy array where output[i,j] contains the similarity
        score between the start frame at i and the end frame at j of the
        video_volume.  This matrix is symmetrical with a diagonal of zeros.
    """
    raise NotImplementedError


def transitionDifference(similarity):
    """Compute the transition costs between frames accounting for dynamics.

    Iterate through each cell (i, j) of the similarity matrix (skipping the
    first two and last two rows and columns).  For each cell, calculate the
    weighted sum:

        diff = sum ( binomial * similarity[i + k, j + k]) for k = -2...2

    Hint: There is an efficient way to do this with 2d convolution. Think about
          the coordinates you are using as you consider the preceding and
          following frame pairings.

    Parameters
    ----------
    similarity : numpy.ndarray
        A similarity matrix as produced by your similarity metric function.

    Returns
    -------
    numpy.ndarray
        A difference matrix that takes preceding and following frames into
        account. The output difference matrix should have the same dtype as
        the input, but be 4 rows and columns smaller, corresponding to only
        the frames that have valid dynamics.
    """
    raise NotImplementedError


def findBiggestLoop(transition_diff, alpha):
    """Find the longest and smoothest loop for the given difference matrix.

    For each cell (i, j) in the transition differences matrix, find the
    maximum score according to the following metric:

        score = alpha * (j - i) - transition_diff[j, i]

    The pair i, j correspond to the start and end indices of the longest loop.

    **************************************************************************
      NOTE: Remember to correct the indices from the transition difference
        matrix to account for the rows and columns dropped from the edges
                    when the binomial filter was applied.
    **************************************************************************

    Parameters
    ----------
    transition_diff : np.ndarray
        A square 2d numpy array where each cell contains the cost of
        transitioning from frame i to frame j in the input video as returned
        by the transitionDifference function.

    alpha : float
        A parameter for how heavily you should weigh the size of the loop
        relative to the transition cost of the loop. Larger alphas favor
        longer loops, but may have rough transitions. Smaller alphas give
        shorter loops, down to no loop at all in the limit.

    Returns
    -------
    int, int
        The pair of (start, end) indices of the longest loop after correcting
        for the rows and columns lost due to the binomial filter.
    """
    raise NotImplementedError


def synthesizeLoop(video_volume, start, end):
    """Pull out the given loop from the input video volume.

    Parameters
    ----------
    video_volume : np.ndarray
        A (time, height, width, 3) array, as created by your videoVolume
        function.

    start : int
        The index of the starting frame.

    end : int
        The index of the ending frame.

    Returns
    -------
    list
        A list of arrays of size (height, width, 3) and dtype np.uint8,
        similar to the original input to the videoVolume function.
    """
    raise NotImplementedError


def binomialFilter5():
    """Return a binomial filter of length 5.

    NOTE: DO NOT MODIFY THIS FUNCTION.

    Returns
    -------
    numpy.ndarray(dtype: np.float)
        A 5x1 numpy array representing a binomial filter.
    """
    return np.array([1 / 16.0, 1 / 4.0, 3 / 8.0, 1 / 4.0, 1 / 16.0], dtype=float)
