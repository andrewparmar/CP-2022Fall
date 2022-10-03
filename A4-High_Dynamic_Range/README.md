# High Dynamic Range Imaging

## Synopsis

This assignment focuses on the core algorithms behind computing HDR images based on the paper ["Recovering High
 Dynamic Range Radiance Maps from Photographs” by Debevec & Malik](https://www.pauldebevec.com/Research/HDR/). Significant usage of linear algebra is required. The notational conventions & overall structure are explained in the paper. To aid with this assignment review these resources:
  
 - Lesson 05-04 HDR
 - Chapter 10.2: Szeliski, R. (2010). Computer Vision: Algorithms and Applications
 - ["Contrast Enhancement Through Localized Histogram Equalization" by Bob Cromwell](https://cromwell-intl.com/3d/histogram/)

    
  **You are NOT required to take image sets for this assignment**. Instead, you have a choice of taking your own HDR
   image set or using an image set
      from the web. 
      
  If you are interested in taking your own image set, you will need a steady tripod and camera with full manual
   controls. Remote control would be helpful. HDR image sets (minimum of 5 images for this assignment) must be well
    aligned and meet critical settings requirements. At a minimum, the camera
    must have manual exposure time control, where other settings (particularly aperture and ISO) are held constant.
      If you would like to take your own set, examine some of the web sets so that you understand what type of scene
       works well.
     
 
## General Instructions
**TLDR:** Read the Docstrings and the Debevec & Malik paper. You can't get through this assignment without special care
 following the docstrings. 
 
- Images in the `images/source/sample` directory are provided for your own testing. A sample output is also provided for your own comparison use. Due to randomness in the process, your image may be very slightly darker or lighter, but the coloring should be the same. **None** of these sample set images will be included in the report.
- **It is essential to put the images in exposure order and name them in this order. `main.py` expects it, as will our verification software.**  This is done for you in the
 *input/sample/* folder images of the home. For these sample images, the exposure info is given in main.py and repeated here
  (darkest to lightest): `EXPOSURE TIMES = np.float64([1/160.0, 1/125.0, 1/80.0, 1/60.0, 1/40.0, 1/15.0])`  
- Read the `main.py` file before you start, there are tools and plot resources included for you. Main.py is not submitted, and you may make changes to the file. 
- Running `python main.py` will execute your HDR pipeline. The script will look inside each subfolder under `images/source/` and attempt to apply the HDR procedure to the contents, and save the output to `images/output/`. (For example, `images/source/sample` will produce output in `images/output/sample`.)
- **Optional:** Numba library is available for those who are willing to accept its limitations on code format for the trade-off of much greater execution speed. **There is a real learning curve for numba; you cannot blindly apply it to everything.** You would need to `pip install numba`, and look-up material on how to use it. If you vectorize your code well and don't need the speed, you don't need `numba`. It is most important for those who wish to process large images.
- Downsample your input images to 500kB or less for testing. This assignment will be assembling all of your input images into one
 image, and it is memory intensive. Some image sets contain a dozen or more images, and may cause problems with your own computer or the resource-limited autograder.

## 1. Code Guidance
### 1a. Implement Basic HDR image functions in `hdr.py` file
The following functions are require to generate the basic HDR image from an input image set.
- `linearWeight`: Determine the weight of a pixel based on its intensity.
- `sampleIntensities`: Randomly sample pixel intensity exposure populations for each possible pixel intensity value from the exposure stack.
- `computeResponseCurve`: Find the camera response curve for a single color channel by finding the least-squares
 solution to an overdetermined system of equations. This function is difficult. There are two additional resources
  provided in the repo for you: constraintMatrixEqns.pdf and mat_A_example.png. Passing the AG does **NOT** guarantee
   that your mat_A is correct, as randomness in sampleIntensities affects your mat_A and subsequent results. You are
    strongly recommended
    to print or view your mat_A and ensure that its general pattern is similar to these references. Poor results in
     this assignment are often related to mat_A coding errors. 
- `computeRadianceMap`: Use the response curve to calculate the radiance map for each pixel in the current color channel.
At this point, you should be able to use the `main.py` function `computeHDR` to generate your basicHDR result.
 
**Radiance map plots** can be generated as a part of the production of the HDR by `main.py`. This plot is not
 required in the report, but you may compare its output to Figures 5 and 8d in Debevek & Malik to understand the
  magnitudes of the radiance values in your image.

### 1b. Implement Histogram Optimization in the `hdr.py` file
After you complete the (1a) functions and generate the basicHDR image from your input set, complete the
 following functions. These functions take the basic HDR image and apply histogram equalization to it. Review [B. Cromwell’s “Contrast Enhancement through Localized
  Histogram Equalization”](https://cromwell-intl.com/3d/histogram/?s=tb) for background.
 - `computeHistogram`: Generate a histogram of image values given an HDR image, **without using library histogram functions**.
- `computeCumulativeDensity`: Calculate a cumulative density array for the histogram bins.
- `applyHistogramEquilization`: Apply the cumulative density calculated on each pixel in the original image to only the V-channel in the HSV (hue, saturation, value) colorspace. Replace the enhanced V-channel and generate the histogram-equalized (histEQ) HDR image. This image will be used in the Report.
 
**Histogram & Cumulative Density plots** of the basicHDR and histEQ images can be generated in `main.py`. These plots
 are required in the Report. Familiarity with this plot code should help in generating your bestHDR image, as well.
 
### 1c. Implement Best HDR in the `hdr.py` file
See section 3 for direction. This function will be operationally tested by the AG to ensure that it runs and produces a result image of expected type and size only.  TAs will run this code and verify results.  Since this function may be slow, we have increased the autograder time.
 
### 1d. Submitting Code to the Autograder
The docstrings of each function contain detailed instructions. You are *strongly* encouraged to write your own unit
 tests based on the requirements. The hdr_tests.py file is provided to get you started. Your code will be evaluated
  on input and output type (e.g. float64, uint8, etc.), array shape, and values.
  
Be careful regarding arithmetic overflow on function outputs. In this assignment you will often be working in wildly different ranges than 0-255 as we follow the work of Devebec & Malik. The radiance maps will have ranges of many magnitudes. **Do not blindly threshold, clip or convert to uint8 unless it is
     called for, or you may drastically reduce your radiance map and ruin your output results.**
     
**The autograder timeout has been extended to 20 minutes to allow for extra run time for your `bestHDR` function.**
  
When you are ready, submit your code to the Gradescope autograder for scoring. We will enforce the following
 penalties for excessive submissions:
- <= 20 submissions → No penalty 
- <= 30 but >20 submissions → -5 penalty
- <= 40 but >30 submissions → -10 penalty
- more than 40 submissions → -20 penalty
  

## 2. HDR Image Sets
### 2a. Making the four required HDR Images: `basicHDR`, `histEQ`, `bestHDR` and `bestHDRColorEnhanced`
Once you have passed the AG with your code using the sample images, it's time to find/take a good set of HDR images. Use
 these functions on your chosen set of input images to make your `basicHDR`, `histEQ`, `bestHDR` and `bestHDRColorEnhanced` images and associated
  plots. Find an image set on the web, or take your own series of images. 
  
- The entire set of input images along with your resulting HDR images must be submitted in Resources. 
- Obtain an image set with a minimum of 5 images. Your set must have exposure steps while other settings are held constant.
- The size of your complete set of input images must be less than 20MB.  Resize as necessary before you start. 
- The four result images must be produced from the images you submit.
- **Caution:** past students have tried to use image sets that changed the ISO
 values instead of exposure. This is a different method, it will not work here, and you will fail the assignment.
 
### 2b. Image Sources and Settings
Two good sources of HDR image input sets:
- Herrmann, K. (Oct 15 2020), Farbspiel Photography, "HDR pics to play with", 
(https://farbspiel-photo.com/learn/hdr-pics-to-play-with) 
- Toman , W. (Oct 15 2020). "HDR Tutorial Sample HDR photos to play with", 
(http://hdr-photographer.com/hdr-photos-to-play-with/)
- Search the web for other good sets, sources change over time. If you find other good sets, please post the URL on Ed.
- Several students may use the same image set.
- You must cite the source of your images in References. 

### 2c. Requirements for your image set
- **You MUST use at least 5 input images** to create your final HDR image. In most cases, using more input images is
 better. 
- **The size of your entire image set must be less than 20MB.**  Make sure the images retain EXIF.
- **Every input image must have exposure time, aperture, and ISO setting.**  There is a deduction if
 your images do not have all three items.
- **Enter the EXPOSURE_TIMES (NOT exposure values - EV, they are NOT times) into the main.py code.** Images must be
 numbered in order from darkest (input-01) to lightest (input-xx). Times must be in the
 same order as the image files to get a correct HDR result. Order from darkest to lightest. *Your
  results can be amazingly bad if you don't follow this rule.* 
- **There are large sets with big images available.** We recommend 500kB or less per image for testing. When you are happy, go back to a larger image set for your official results.
- **Image alignment is critical for HDR.** Whether you take your own images or use a set from the web, ensure that your
 images are aligned and cropped to the same dimensions. We have provided an alignment tool in main.py in the main
  function that you can enable in the calling line to perform simple alignments. You
  may use a commercial program such as Gimp (open source) or Photoshop ($$) to help with this step, or write your own
   alignment code if our simple tool does not work for you. This is the only permitted usage of outside software packages in this assignment. *Note what you do in your report.*

### 2d. Taking your own images
 You may take your own images (at least 5 input images) if your camera supports manual exposure time control and you
 have a good tripod. A remote control would help in maintaining camera position between shots. There is no extra credit for this, but you will earn our respect! Exposure times are required for your code, and aperture and ISO must be reported. Dark indoor scenes with bright outdoors generally work well for this, or outdoor scenes with overly-bright and dark areas. Take a look at Debevec & Malik 1997 and [Durand & Dorsey "Fast Bilateral Filtering for the Display of High-Dynamic_Range" 2002](https://people.csail.mit.edu/fredo/PUBLI/Siggraph2002/DurandBilateral.pdf) in Canvas for examples of good scenes.


## 3. Histogram Optimization and Tone Mapping: The Best HDR Image

Debevek & Malik's main concern was generating radiance maps that must be produced before images are
 displayed. Mapping the wide range of the HDR radiance map to fit the limited visible range of a display or
 print medium is the final step in computing the basicHDR image. This assignment's base code just normalizes the
  log of the radiance map to 0-255 and saves the result.  You will notice that our basicHDR image demonstrates a nice, but somewhat muted result that needs further processing to generate a pleasing image. The few output images in the Debevek & Malik paper (Figure 8e and 8f, with adaptive histogram compression) were generated using [Greg Ward Larson's 1997 methodology](https://www.semanticscholar.org/paper/A-visibility-matching-tone-reproduction-operator-Larson-Rushmeier/a74444748e2a29f7a31294e6c3a5982819e9b5f7) which used histogram compression to generate the outputs. Ward's method is complex; as an introduction we took a simple path with HEQ.

Now, you will learn a histogram optimization method to clarify your image, followed by channel enhancements as needed for color, saturation, etc.
 
 Your final method should be general enough to work on more than one image set. No one method is the best for all
  sets, but do not overfit your method to only do well on one set. We will be running a test set to see that your method is reasonable.
 
 
### 3a. The first goal is to enhance the details and clarify image using a histogram method.
Implement Q. Wang's paper "Fast Image/Video Contrast Enhancement Based on Weighted Thresholded Histogram Equalization," which provides acceptable results and is easier to implement than Ward's CLAHE and other AHE methods.
<https://ieeexplore.ieee.org/document/4064576>
 
### 3b. The second goal is to enhance your coloring (saturation and value) in a realistic way.
To do this, you may experiment with various image colorspaces (HSV, YUV, HLS, CIE and others) using cv2 functions to translate your image from one space to
   another, as we did in the `applyHistogramEquilization` function. You may change only one channel or more than one. A little research will suggest a variety of colorspace enhancements, which are usually simple to implement (HSV, YUV and others).  You may use any colorspace supported by the version of opencv used in our class env, CS6475. You are working to produce more life-like colors, with less of the muted coloring than the basicHDR image has. The emphasis is on lifelike colors that may be found in some of the input images. Credit your sources.

*Hint:* investigate your histograms and control your outliers to reduce artifacts
 

### 3c. One Best HDR Image Requirements

Generate your `bestHDR` code in `hdr.py` to take as input your basicHDR image and output your bestHDR image. You will also implement the `colorspaceEnhancement` function which will take in your bestHDR image and perform color enhancement on it. All code must be in `hdr.py`. Inputs and outputs are defined in the docstring. The code will be tested for operability in the autograder, and by TAs. Your images and their histogram-CDF plots will go into your report. You will discuss your method and its code. 
    
Write your code *without* using opencv **major algorithm functions**. No cv2.doMyHomeworkForMe(). Specifically, no cv2 versions of CLAHE, or Tonemaps: Debevec, Robertson, Mertens, Drago, Durand, Mantiuk or Reinhard. Nothing in this project can be done using outside software excepting input image alignment for those who take their own pictures. 

**Your bestHDR image should show clear improvement over your basicHDR and histEQ images.** Clear improvement means the
 colors are enhanced realistically to values that may be seen in the individual input images and reasonably existed at the location. Clarity is improved, and fine detail areas enhanced. Halos and other artifacts should not be introduced. If your image takes a pastel church image and turns it into a Gothic Halloween image it may be very cool, but you have missed the mark. 


## 4. Download & Complete the Report

Use the `A4_HDR_report_template_term.zip` report template provided in the class repository. **The LaTeX template specifies all of the images, data, and questions you must answer.** Follow the instructions in the [Course Setup](https://github.gatech.edu/omscs6475/assignments/tree/master/Course_Setup) to upload it in Overleaf. If you have a different favorite LaTeX program, you may use it; the template should be generally compatible.
   
  - **The total size of your report+resources must be less than 35MB** for this project. If your submission is too large, you can reduce the scale of your images or report. You may resize your images using `cv2.resize`. You can compress your report using [Smallpdf](https://smallpdf.com/compress-pdf).
  - **The total length of your report is 7 pages maximum.** This report is expected to be five-six pages for most students, unless you decide to submit extra observations and images in the appendix (no extra credit, but the TA staff enjoys interesting work and unusual fails!)
  - **You are required to use the LaTex format for your report.** Different report organization or changing section titles and questions will receive a deduction. You may add additional relevant information or images within the structure of the report, as long as all requirements are met.
  - **You are required to provide References.** Everyone is expected to have at least four references; the two required papers and two additional references; these should include StackOverflow answers, valuable tutorials, blogs, Ed posts, and other paper or textbook references. Provide URLs and site or page names, typical book information and page numbers, etc. We should be able to easily view your references if needed.
   
**Save your report as `report.pdf`**

## 5. Submit the Report

Submit `report.pdf` to:
 - **Gradescope** as *A4-HDR Report* 
 
    __and__ 
 - **Canvas** > Assignments to *A4: HDR Report*
 
 After you upload your PDF to Gradescope, you will be taken to the "Assign Questions and Pages" section that has a Question Outline on the left hand side. These outline items are determined by the Instructors. For each question - select the question, and then select ALL pages that go with that question. This is important to do correctly because any pages that are not selected for the corresponding question might get missed during grading.


## 


. Submit the Resources

Your `resources.zip` must include your code, the input images you chose, and your three HDR result images
 result for the input set of your choice. Again, do not include the sample set images or results.
 Follow the filename protocol below, the autograder will be expecting these exact filenames.
 
Gather the following files, and zip the files into `resources.zip`.  **DO NOT** place the files inside a folder before you zip them. Submit the zip file to **Gradescope** A4-HDR Resources.  Your entire resources submission should be 30MB or less to allow room for your report in the 35MB limit.

**Filenames for Resources (12 required files):**
*Your images must be one of the following types: png, jpg, or jpeg
- `hdr.py`  submit only one code file that produces all of your images
- `input_01`
- `input_02`
- `input_03`
- `input_04`
- `input_05`
- *also include all remaining images in your set, numbered in order*
- `basicHDR`: basic HDR image 
- `histEQ`:   histogram-equilized image
- `bestHDR`:  bestHDR image
- `bestHDRColorEnhanced`: bestHDR image after color enhancements
- `histCDF_basicHDR`  histogram-CDF plot for basicHDR image 
- `histCDF_histEQ`    histogram-CDF plot for histEQ image 
- `histCDF_bestHDR`   histogram-CDF plot for bestHDR image 
- `histCDF_bestHDRColorEnhanced` histogram-CDF plot for bestHDR image after color enhancements

- any additional images for bestHDR may be included with appropriate filenames
 
      
**Notes:**
   - **Submission Size:** The total size of your project (report.pdf + 
     resources.zip) **MUST** be less than **30MB** for this project. If your submission is too large, you can reduce the scale of your images or report. You can compress your report using [Smallpdf](https://smallpdf.com/compress-pdf).
  - When sharing images, make sure there is no data contained in the EXIF data that you do not want shared (i.e. GPS). If there is, make sure you strip it out before submitting your work or sharing your photos with others. Normally, we only require that your submitted images include aperture, shutter speed, and ISO (these 3 settings are required for A5).

  - **DO NOT USE 7zip.** We've had problems in the past with 7z archives, so please don't use them unless you don't mind getting a zero on the assignment.


#### 7. Criteria for Evaluation

Your submission will be graded based on:

  - Correctness of required code
  - Creativity & overall quality of results
  - Completeness, depth, accuracy and quality of report
