import cv2
from pathlib import Path
import piexif

# load the original input image and display it on our screen
files = [
    "images/other/bamboo_forest/input_01.jpg",
    "images/other/bamboo_forest/input_02.jpg",
    "images/other/bamboo_forest/input_03.jpg",
    "images/other/bamboo_forest/input_04.jpg",
    "images/other/bamboo_forest/input_05.jpg",
    "images/other/bamboo_forest/input_06.jpg",
]


def main():
    for f in files:
        img = cv2.imread(f)
        filename = "./images/source/bamboo_forest/" + f.split("/")[-1]
        img_scaled = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, img_scaled)
        piexif.transplant(f, filename)

if __name__ == "__main__":
    main()