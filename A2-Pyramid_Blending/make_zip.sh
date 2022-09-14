rm resources.zip
mkdir resources

cp images/source/original/black.png resources/black_0.png
cp images/source/original/white.png resources/white_0.png
cp images/source/original/mask.png resources/mask_0.png
cp images/output/original/result.png resources/result_0.png

zip resources.zip -j \
    blending.py \
    resources/black_0.png \
    resources/white_0.png \
    resources/mask_0.png \
    resources/result_0.png
