rm resources.zip
rm -r resources
mkdir resources

cp images/results/*.png resources/
cp seam_carving.py resources/

zip resources.zip -j resources/*