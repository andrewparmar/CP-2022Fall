import cv2
from pathlib import Path
import piexif

# load the original input image and display it on our screen
files = [
    "./images/stash/boardwalk_1/input_2.jpeg",
    "./images/stash/boardwalk_1/input_3.jpeg",
    "./images/stash/boardwalk_1/input_1.jpeg",
    # "images/stash/marina_2/IMG_1286.png",
    # "images/stash/marina_2/IMG_1284.png",
    # "images/stash/marina_2/IMG_1285.png",
    # "images/stash/yachts_1/input_1.png",
    # "images/stash/yachts_1/input_2.png",
    # "images/stash/yachts_1/input_3.png",
    # "images/stash/marina_1/input_1.png",
    # "images/stash/marina_1/input_2.png",
    # "images/stash/marina_1/input_3.png"
]


def main():
    for f in files:
        img = cv2.imread(f)
        filename = "./images/source/boardwalk_small/" + f.split("/")[-1]
        img_scaled = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, img_scaled)
        piexif.transplant(f, filename)

if __name__ == "__main__":
    main()