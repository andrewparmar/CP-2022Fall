rm resources.zip
rm -r resources
mkdir resources

cp images/output/bamboo_forest/*.png resources/
cp images/source/bamboo_forest/*.jpg resources/

zip resources.zip -j \
    hdr.py \
    resources/*