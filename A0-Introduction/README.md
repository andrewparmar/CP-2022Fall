# A0 - Introduction

## Synopsis

In this introductory assignment, you will do some Python programming **using an
 image that you took with your camera or smartphone**. You will use NumPy and
OpenCV libraries to work with the image array and write your own convolution
   function. 
  
To accomplish this, you will use the Python3 environment CS6475, your
   LaTeX program (Overleaf Professional or others), Gradescope to autograde
    your code and turn in your Report and Resources, and Canvas to practice submitting your report for Peer Feedback. Although there is no Peer Feedback for A0, we want you to submit your report to Canvas to build the habits that you will use for each assignment. 

References for this assignment *(Lessons are in Canvas > Ed Discussion > Lessons Icon*):
- [*Course Setup*](https://github.gatech.edu/omscs6475/assignments) must be completed before this assignment.
- [*Notebook 1: Image Processing*](https://github.gatech.edu/omscs6475/lab_exercises) is extremely helpful with writing code for this assignment
- Lesson 02-01 parts 6-14: Pixels, grayscale vs. color images
- Lesson 02-04 parts 1-10: Introduction to smoothing (filtering)
- Lesson 02-05: Convolution and filtering

### 1. Download the Assignment0 files from GitHub
See the *Course Setup README* for information on how to pull Assignment0-Introduction from
 the class repo. The files include:
 - ***README.md*** which may be viewed in various IDEs, Notepad++ with MarkdownViewer++ installed, and other text readers. The README provides general assignment requirements, and specific information on submission requirements.
 - ***A0-latex_report_template_term.zip***, a LaTeX template which you must use for your report. The report template contains the questions you must answer, and has placeholders for the required images and data you will need to produce from your code.
See the *Course Setup* to setup your free Professional account. If you have your account, login at [Overleaf](https://www.overleaf.com/) and import the template.zip file. You should see the normal dashboard with a button to create a **New Project**. Select **Create First/New Project → Upload Project** and choose your template zip file. Make a working copy so you can always refer back to the original (click on the Copy icon under the Actions column). Read through the template, so you know what you will be asked.  You can print out a PDF to make notes on during your work (download the file at the top of the Recompile window, then print).
 - ***assignment0.py***, a python3 file containing a skeleton with function signatures and detailed docstrings with specific
    requirements for the functions you must write. Read the docstrings carefully for guidance and restrictions on what cv2 and numpy functions you can use.
 - ***main.py***, a helper file that you may use to run your chosen image through your chosen filter and produce the required result images. You may alter this file as desired, and it is **NOT** turned in. Most assignments will provide a `main.py` file to help produce final results.
 - ***images/source***, folder contains a small sample `image.png` you may use while you are writing your code. Replace this image with your image to generate results for your report. DO NOT TURN IN THE PUPPY IMAGE OR ITS RESULT IMAGES.
 - ***toy_image.png***, a sample toy image is provided as example of arrays that can help test your code. The command to produce *image.png* is in the *main* function in *assignment0.py*. This is an extra-small 3D array of pixels with
    random uint8 values in the range (0-255). A toy image would be used to make sure your code is working as you figure out padding and convolution. It has
      no other use, and is not turned in. It can be visualized as an image or printed out as an array using most IDEs. You should produce your own toy images as needed. 

### 2. Take a picture
Many of the class assignments require you to use ORIGINAL images that you have taken yourself, either now or in the past. Your subject matter for this image should be clear and static. You will be filtering, so clear and sharp images of nearby objects work well. Its not hard to get intriguing images of everyday objects.

#### Image Requirements 
Deductions are taken if you don't meet these requirements.
 -  One image you took yourself. No downloads, no pictures your friends took.
 -  **maximum image size of 300kB is required.** Maximum image size (total number of pixels) will be determined during our code run, by using `np.size(image_array)`. The reason we require small images is so you can use small-sized filters, which will work much faster on small images. 
 -  To reach the maximum size, you may resize/crop your image. You must retain the EXIF, see info below for this. This resized or cropped image with EXIF becomes your "original image" for the report.
 -  **Your report images must clearly show the effects produced by your filter;** using larger images can make this difficult.
 -  image is in color (three-channel RGB) 
 -  in format of .png or .jpg (the report pdf LaTeX compiler has issues with other image types, use cv2 to convert image formats)
 -  with EXIF information retained for exposure time, aperture, and ISO, for
  the report
  
  **Important Note:** Other students in the class, as well as the teaching staff, will see your image, so do not choose subjects that could embarrass you or others. Make sure your image is appropriate to share publicly with the class.
 
 #### Regarding Image Size and Type (png or jpg)
 We recommend working with PNG images throughout the class. The PNG images will seem to be larger for any particular image, but that's a red herring. The same image of the same dimensions may be listed as only half the size in the compressed JPG image, as compared to the PNG image. The PNG image will list a size in pixels = height x width x 3 (channels). But when your "smaller" JPG file is opened in your code, it reverts to its uncompressed size, the same as the PNG.  And it will run just as slow. The PNG images will retain more detail. The assignment limits are always sufficient for the reports and resources.  Your 4MB or 12MB image isn't going to look much better in the report when it is only a couple inches in dimension.  And it will take a whole lot longer to process through your code.  You want an image that can process in seconds, or at least only a couple minutes.  
 
 Finally, the input and result images you submit in Resources must be the same-size versions you used to make your report. The Autograder will grade your code functionality. We will also run your code using your own input images, and we expect to get output images that match yours. If your result images don't match our result images, we will contact you, and ask why?
  
#### Retaining Image EXIF Information
You will probably be resizing your image to meet the 300kB total image size. There are several ways to keep the EXIF info with your image.
- Use the python library [piexif](https://pypi.org/project/piexif/). Piexif can use a single command to transplant exif from one pic to another, such as after a resize. See [StackOverflow](https://stackoverflow.com/a/51759580) for more on this.
- If you use the open source program [Gimp](https://www.gimp.org), you can resize (image > scale image) and will not lose your EXIF. Then export (not save) the new image in the desired type of png or jpg. 
- [ExifTool](https://exiftool.org/#JPEG) is an older library that can write EXIF.
- Share other methods you find on Ed!


### 3. Choose a Filter
We are not trying to trick you or require particularly difficult filters for this assignment. You only need to produce results for the report using one filter, which you will document in the code function `myFilter`. You may use any of the common filters mentioned in the lessons for this purpose, including box, gaussian, edge-finding, median, and more. You may find filters in the lessons or in the textbook, if you are interested in looking further. 

#### Filter Requirements
- Use one of the filters mentioned in any of the course lessons or the Szeliski textbook, as long as the filter is square and odd. See the listed lessons for examples of filters you could use. Although many filters are symetrical across both x and y, at least one of the autograder test cases will be a non-symmetrical (but square and odd) filter.  Edge-finding filters such as Sobel, Prewitt and Scharr are non-symmetrical in this respect.
- Your filter must be **square and odd** and 2D.  Example dimensions (H,W): (3,3), (11,11), (21,21).  
- The filter effect must be **clearly visible in the report** images.  
- The filter effect must be **what is expected** from that type of filter.  i.e. if you use a box filter, we don't expect to see a psychedelic spaghetti image. (yes, it happens). Make sure you know what to expect.
- Most filters need to be **normalized** (the elements should sum to one). What happens to the image if the filter elements sum to a larger number? Try it.
- Edge filters usually sum to 0, they are an exception. 

### 4. Implement the Functions in `assignment0.py` file

First, write the code as specfied in `assignment0.py` using toy image arrays to help with testing. Do NOT hard-code the filters or images in your python file, except for the function: myFilter. Your convolution code functions should be able to accept any 3-channel RGB image and any square odd-dimensioned filter and produce results. 

When you are satisfied with your code or a significant function is complete, submit it to the Gradescope autograder. You have a limited number of submittals which is covered below. When your code scores are as good as you can get, save a copy of your good `assignment0.py` for the final Resources submittal. Then, use your **original unprocessed (may be resized) image, renamed as *image.png* or *image.jpg*** to generate results for the report using your chosen filter in myFilter.

**Note: All of the filters you may write for the functions, or that we will test with, should be square and odd; e.g. 3x3, 5x5, 15x15, etc.** 

- `returnYourName` A function that returns *Your Name* when called. Your name
 should match your Gradescope account *Course-Specific Information* Name exactly. When you test your code in Gradescope, if your name does not match, Gradescope will return the exact name it expects, making it easy to correct your code.
- `imageDimensions` A function that returns the dimensions of the image array.
- `imageSize` A function that returns the true size of your image array. This function will be used when we run your code outside of the autograder.
- `myFilter` A function that returns the filter you chose to use with your image for the report. This function will be used when we run your code outside of the autograder.
- `convolveManual` A function that
 takes in an image and filter (kernel) and convolves the image with the
  filter. Padding will be needed. The convolved image of the same dimensions as the input image is returned. You must use loops in your code
   for this function to pass over every image pixel. **You
   are NOT allowed to use out-of-the-box convolution algorithms from OpenCV, NumPy, or anywhere else.** Yes, it will be slow.
- `convolveCV2` A function that convolves the same image with the same filter
 using powerful OpenCV commands. You may discuss appropriate openCV commands on ED for this assignment. Provide references in your report for your final choice.

**IMPORTANT NOTE:** We are expecting your code to complete a true convolution in both of the convolve functions. Make sure you know the difference between correlation and convolution, and what the openCV commands actually do. We will have some autograder cases that will deliberately test for convolution.

The docstrings for each function contain detailed instructions. You have a limited number of free submissions to the autograder for each project, so begin coding with a small
  toy image array so that you can immediately print results from your code and verify them by hand. Then, you are encouraged to write your own unit tests. You can write your own testing script in the main function at the end of the python skeleton. 
  
  After the late due date for the assignment, the TAs will run your code through your `convolveManual` and `convolveCV2` functions. The code run will use your input image from Resources, and your filter from `myFilter`.  The results we get should match your Resources results, and the images in your report. At this time, we will also verify your image  array size using your `imageSize` function is no more than 300kB.
  
  #### The Gradescope Autograder
   
   When you have as much code written and working as possible, test it using the Gradescope autograder.  
   Make sure that you leave a couple autograder submissions for your final Resources submission with your images. We will enforce the limits and point value penalties shown below through the Gradescope autograder.
   
**IMPORTANT NOTE: If the autograder crashes and says contact instructors, DO NOT keep trying,** each attempt counts. Often the problem is a fatal error in your code, such as bad indentation or a misspelled or broken variable or command. Make sure your code compiles and runs on your own computer running the class environment (CS6475) first! If you can't find anything wrong, contact the Instructor staff via Ed.

- The autograder times out in 10 minutes.  Make sure your code can run on small images (e.g.: 100x150x3 pixels before padding) with small filters (9x9 or much less) in this time, as we will test your code with small images. It should not be difficult to meet this time, your code should take only a few seconds to run.

- <= 20 submissions → No penalty 
- <= 30 but >20 submissions → -5 penalty
- <= 40 but >30 submissions → -10 penalty
- more than 40 submissions → -20 penalty


### 5. Complete the LaTex Report

Use the `report_template.zip` file provided in the class  repo. **The template specifies all of the images, data, and questions you must answer.** This is a LaTeX template, follow the instructions in the Course Setup to upload it in Overleaf. If you have a different favorite LaTeX
   program, you may use it; the template should be generally compatible.
   
  - **The total size of your report+resources must be less than 10MB** for this project. If your submission is too large, you can reduce the scale of
    your report. You can compress your report using [Smallpdf](https://smallpdf.com/compress-pdf).
   - **This report is expected to be about one page for the great majority of students.** The maximum length of your Report is 2 pages. A report that is
    even one line over 2 pages will receive a deduction. You can use the second page for additional or "interesting" results. Please describe what is in any extra images, and how it came to be. There is no extra credit, but we are always interested in what you can produce. 
   - **You are required to use the LaTex format for your report.** Different report organization or changing section titles and questions will receive a deduction. You may add additional relevant information or images within the structure of the report, as long as all requirements are met.
   - **You are required to provide References.** Everyone is expected to have at least two references; these should include tutorial or reference answers that you relied on for specific commands, blogs, helpful Ed posts, and textbook references. Provide URLs and website or page names, typical book information and page numbers, etc. We should be able to easily view your references if needed.
   
**Save your report as `report.pdf`**


### 6. Submit the Report on Gradescope and Canvas

1. **Gradescope:** Submit your Report PDF to **A0-Introduction Report.** Once it is uploaded, you may look through the pages to make sure you uploaded the right document and all parts are displayed properly. There is no limit to Report submission attempts, only Resources attempts. After you upload your PDF, you will be taken to the "Assign Questions and Pages" section that has a Question Outline on the left hand side. These outline items are determined by the Instructors. **For each question - select the question, and then select ALL pages that go with that question.** This is important because any pages that you do not select for the corresponding question might get missed during grading.

2. **Canvas:** submit your Report PDF on **Canvas > Assignments > A0-Introduction Report.** This allows your report to be uploaded to the Peer Feedback system. Starting with A1, forgetting to submit to Canvas by the late deadline will result in a deduction. We require you to submit your A0 PDF to Canvas as practice so you become familiar with the subission process. 


### 7. Submit the Resources to Gradescope

Your Resources, consisting of required code and images, are submitted to Gradescope only. They are NOT submitted to Canvas.
 
Gather the following files together. Your Resources files must be named as follows.  Note that both 'png' and 'jpg' images are allowed, but no
  other image types, as Overleaf's PDFcompiler will not accept them.
  
- `assignment0.py` - Python file
- `image.png` - your correctly sized image with EXIF
- `convolveManual.png` - convolved image from the convolveManual function
- `convolveCV2.png` - convolved image from the convolveCV2 function
- *Optional:* any additional images that you submitted in your report should be submitted. Name them in a similar way as the required images (e.g. `image_2.png`)
, and use these names in the Report. (no extra credit, though)

Zip the files together. Rename the zipped file `resources.zip`. When you are zipping up your files, make sure that you zip the files, **not the folder containing the files**. Gradescope only looks at the root of the zip archive for the submitted files, so keep this in mind to avoid submission issues.
   
Submit your zipped file to **A0-Introduction Resources** on Gradescope. The autograder will test `assignment0.py` immediately, and it will also check that you
     submitted three image files with the correct names and acceptable file extensions (e.g. `image.jpg`, `convolveManual.png`).  The autograder
       will give you a score for the Resources portion of the assignment immediately. 
   
- Keep in mind that the autograder only checks that you submitted image files with the correct name and an acceptable extension. The Instructors will still manually check Resources for correctness/quality during grading and will deduct points if necessary. We will run your code to ensure that it produced the images you submitted. Therefore, the grade you receive from the Gradescope autograder may not be your final grade.  

**Important Notes:**

- **EXIF metadata:** When including or sharing images, make sure there are no data contained in the EXIF metadata that you do not want shared (i.e. GPS). If there is, make sure you strip it out before submitting your work or sharing your photos with others. Normally, we require that your images include aperture, shutter speed, and ISO. 

- **DO NOT USE 7zip.** We've had problems in the past with 7z archives, so please don't use them unless you don't mind getting a zero on the assignment.


### 8. Criteria for Evaluation
Your submission will be graded based on:

  - Correctness of required code
  - Creativity & overall quality of results, images, and data.
  - Completeness, depth, accuracy and quality of report


