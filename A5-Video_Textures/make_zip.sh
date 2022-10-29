rm resources.zip
rm -r resources
mkdir resources

cp videos/out/candle_diff1.png resources/candle_matrix_1.png
cp videos/out/candle_diff2.png resources/candle_matrix_2.png
cp videos/out/candle_diff3.png resources/candle_matrix_3.png
cp videos/out/candle_start_frame.png resources/candle_start_frame.png
cp videos/out/candle_end_frame.png resources/candle_end_frame.png

#cp videos/out/original_diff1.png resources/original_matrix_1.png
#cp videos/out/original_diff2.png resources/original_matrix_2.png
#cp videos/out/original_diff3.png resources/original_matrix_3.png
#cp videos/out/original_start_frame.png resources/original_start_frame.png
#cp videos/out/original_end_frame.png resources/original_end_frame.png

zip resources.zip -j \
    resources/*
