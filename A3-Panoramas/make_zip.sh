rm resources.zip
mkdir resources

cp images/source/boardwalk_small/*.jpeg resources/
cp images/output/boardwalk_small/output.jpg resources/result.jpg

zip resources.zip -j \
    panorama.py \
    main.py \
    resources/*.jpeg \
    resources/result.jpg
