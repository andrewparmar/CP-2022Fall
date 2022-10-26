import errno
import os
import sys
from glob import glob

import cv2
import numpy as np
import textures


def vizDifference(diff):
    """This function normalizes the difference matrices so that they can be
    shown as images.
    """
    return (((diff - diff.min()) / (diff.max() - diff.min())) * 255).astype(np.uint8)


def runTexture(img_list, alpha):
    """This function administrates the extraction of a video texture from the
    given frames, and generates the three viewable difference matrices.
    """
    video_volume = textures.videoVolume(img_list)
    ssd_diff = textures.computeSimilarityMetric(video_volume)
    transition_diff = textures.transitionDifference(ssd_diff)
    idxs = textures.findBiggestLoop(transition_diff, alpha)
    print("Loop bounds: {}".format(idxs))
    print(alpha, idxs)

    diff3 = np.zeros(transition_diff.shape, float)

    for i in range(transition_diff.shape[0]):
        for j in range(transition_diff.shape[1]):
            diff3[i, j] = alpha * (j - i) - transition_diff[j, i]

    return (
        vizDifference(ssd_diff),
        vizDifference(transition_diff),
        vizDifference(diff3),
        textures.synthesizeLoop(video_volume, idxs[0], idxs[1]),
        idxs,
    )


def readImages(image_dir):
    """This function reads in input images from a image directory

    Note: This is implemented for you since its not really relevant to
    computational photography (+ time constraints).

    Args:
    ----------
        image_dir : str
            The image directory to get images from.

    Returns:
    ----------
        images : list
            List of images in image_dir. Each image in the list is of type
            numpy.ndarray.

    """
    extensions = [
        "bmp",
        "pbm",
        "pgm",
        "ppm",
        "sr",
        "ras",
        "jpeg",
        "jpg",
        "jpe",
        "jp2",
        "tiff",
        "tif",
        "png",
    ]

    search_paths = [os.path.join(image_dir, "*." + ext) for ext in extensions]
    image_files = sorted(sum(map(glob, search_paths), []))
    images = [
        cv2.imread(f, cv2.IMREAD_UNCHANGED | cv2.IMREAD_COLOR) for f in image_files
    ]

    bad_read = any([img is None for img in images])
    if bad_read:
        raise RuntimeError(
            "Reading one or more files in {} failed - aborting.".format(image_dir)
        )

    return images


def draw_circle(image, idxs):
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    # Window name in which image is displayed
    window_name = 'Image'
    # Center coordinates
    center_coordinates = (idxs[1], idxs[0])

    # Radius of circle
    radius = 8

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.circle() method
    # Draw a circle with blue line borders of thickness of 2 px
    image = cv2.circle(image, center_coordinates, radius, color, thickness)
    return image

# The following section will run this file, save the three difference matrices
# as images, and complete the video frame extraction into the output folder.
# You will need to modify the alpha value in order to achieve good results.
if __name__ == "__main__":

    # Change alpha here or from the command line for testing
    try:
        # alpha = float(sys.argv[1])
        alpha = 0.5
    except (IndexError, ValueError):
        print(
            "The required positional argument alpha was missing or "
            + "incompatible. You must specify a floating point value for "
            + "alpha.  Example usage:\n\n    python main.py 0.5\n"
        )
        exit(1)

    # After testing on the candle images, change video_dir
    # to point to directory containing your original images.
    video_dir = "incense_2"
    image_dir = os.path.join("videos", "source", video_dir)
    out_dir = os.path.join("videos", "out", video_dir, str(alpha))

    try:
        _out_dir = os.path.join(out_dir, video_dir)
        not_empty = not all(
            [os.path.isdir(x) for x in glob(os.path.join(_out_dir, "*.*"))]
        )
        if not_empty:
            raise RuntimeError("Output directory is not empty - aborting.")
        os.makedirs(_out_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    print("Reading images.")
    images = readImages(image_dir)

    print("Computing video texture with alpha = {}".format(alpha))
    diff1_ssd, diff2_transition, diff3, out_list, idxs = runTexture(images, alpha)

    cv2.imwrite(os.path.join(out_dir, "{}_diff1.png".format(video_dir)), diff1_ssd)
    cv2.imwrite(os.path.join(out_dir, "{}_diff2.png".format(video_dir)), diff2_transition)
    cv2.imwrite(os.path.join(out_dir, "{}_diff3.png".format(video_dir)), diff3)
    diff3 = draw_circle(diff3, idxs)
    cv2.imwrite(os.path.join(out_dir, "{}_diff3_circled.png".format(video_dir)), diff3)

    for idx, image in enumerate(out_list):
        cv2.imwrite(
            os.path.join(out_dir, video_dir, "frame{0:04d}.png".format(idx)), image
        )

    cv2.imwrite(os.path.join(out_dir, f"{video_dir}_start_frame.png"), out_list[0])
    cv2.imwrite(os.path.join(out_dir, f"{video_dir}_end_frame.png"), out_list[-1])

