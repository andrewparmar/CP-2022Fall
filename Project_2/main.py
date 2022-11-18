"""
Project_2
CS 6475 Fall 2022

You can use this file to execute your code. You are NOT required
to use this file, and ARE ALLOWED to make ANY changes you want in
THIS file. This file will not be submitted with your assignment
or report.

If your travel-level laptop can run this file and produce
all of the outputs without errors within the 2 hour time limit,
then your code should be fast enough. For those wishing a speedier
run, this can be completed in under 5 minutes on that same laptop.

DO NOT SHARE CODE (INCLUDING TEST CASES) WITH OTHER STUDENTS.
"""
import cv2

import os
import errno
import time     # you may add section timing


from seam_carving import (beach_back_removal,
                          dolphin_back_insert,
                          dolphin_back_double_insert,
                          bench_back_removal,
                          bench_for_removal,
                          car_back_insert,
                          car_for_insert,
                          difference_image,
                          numerical_comparison)

SOURCE_FOLDER = "images"
OUT_FOLDER = "images/results"


def generate_base_arrays():
    prefix = SOURCE_FOLDER + "/base/"
    post = ".png"
    try:
        beach = cv2.imread(prefix + "beach" + post)
        dolphin = cv2.imread(prefix + "dolphin" + post)
        bench = cv2.imread(prefix + "bench" + post)
        car = cv2.imread(prefix + "car" + post)
        print("base image arrays generated")
        return beach, dolphin, bench, car
    except:
        print("Error generating base image arrays")


def generate_result_images(beach, dolphin, bench, car):
    """ Calls seam_carving to generate each of the ten result images
    """
    try:
        result = beach_back_removal(beach, seams=300)
        cv2.imwrite("images/results/res_beach_back_rem.png", result)
    except: print('Error generating res_beach_back_rem ')

    try:
        result = dolphin_back_insert(dolphin, seams=100, redSeams=False)
        cv2.imwrite("images/results/res_dolphin_back_ins.png", result)
    except: print('Error generating res_dolphin_back_ins')

    try:
        result = dolphin_back_insert(dolphin, seams=100, redSeams=True)
        cv2.imwrite("images/results/res_dolphin_back_ins_red.png", result)
    except: print('Error generating res_dolphin_back_ins_red')

    try:
        result = dolphin_back_double_insert(dolphin, seams=100, redSeams=False)
        cv2.imwrite("images/results/res_dolphin_back_double.png", result)
    except: print('Error generating res_dolphin_back_double')

    try:
        result =  bench_back_removal(bench, seams=225, redSeams=False)
        cv2.imwrite("images/results/res_bench_back_rem.png", result)
    except: print('Error generating res_bench_back_rem')

    try:
        result = bench_back_removal(bench, seams=225, redSeams=True)
        cv2.imwrite("images/results/res_bench_back_rem_red.png", result)
    except: print('Error generating res_bench_back_rem_red')

    try:
        result = bench_for_removal(bench, seams=225, redSeams=False)
        cv2.imwrite("images/results/res_bench_for_rem.png", result)
    except: print('Error generating res_bench_for_rem')

    try:
        result = bench_for_removal(bench, seams=225, redSeams=True)
        cv2.imwrite("images/results/res_bench_for_rem_red.png", result)
    except: print('Error generating res_bench_for_rem_red')

    try:
        result = car_back_insert(car, seams=170)
        cv2.imwrite("images/results/res_car_back_ins.png", result)
    except: print('Error generating res_car_back_ins')

    try:
        result = car_for_insert(car, seams=170)
        cv2.imwrite("images/results/res_car_for_ins.png", result)
    except: print('Error generating res_car_for_ins')

    print('result images generated')
    return

def generate_differences():
    results = [
        "res_beach_back_rem.png",
        "res_dolphin_back_ins.png",
        "res_dolphin_back_double.png",
        "res_bench_back_rem.png",
        "res_bench_for_rem.png",
        "res_car_back_ins.png",
        "res_car_for_ins.png"
    ]

    comps = [
        "comp_beach_back_rem.png",
        "comp_dolphin_back_ins.png",
        "comp_dolphin_back_double.png",
        "comp_bench_back_rem.png",
        "comp_bench_for_rem.png",
        "comp_car_back_ins.png",
        "comp_car_for_ins.png"
    ]

    diffs = [
        "diff_beach_back_rem.png",
        "diff_dolphin_back_ins.png",
        "diff_dolphin_back_double.png",
        "diff_bench_back_rem.png",
        "diff_bench_for_rem.png",
        "diff_car_back_ins.png",
        "diff_car_for_ins.png"
    ]


    for i in range(len(results)):
        # create & save difference images
        try:
            result = cv2.imread("images/results/" + results[i])
            comp = cv2.imread("images/comparison/" + comps[i])
            diff = difference_image(result, comp)
            cv2.imwrite("images/results/" + diffs[i], diff)
        except:
            print("Error in ", diffs[i])

        # compute & print numerical comparison values
        try:
            num_comp = numerical_comparison(result, comp)
            print("numerical comp value(s): " + results[i] + "\n", num_comp)
        except:
            print("Error num_comp: ", results[i])

    print('differences completed')
    return


if __name__ == "__main__":
    """ Generate the 10 result images, 7 diff images, and 7 numerical comparisons
    """
    # make the images/results folder
    output_dir = os.path.join(OUT_FOLDER)

    try:
        os.makedirs(output_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    print("Processing files...")

    beach, dolphin, bench, car = generate_base_arrays()

    generate_result_images(beach, dolphin, bench, car)

    generate_differences()


