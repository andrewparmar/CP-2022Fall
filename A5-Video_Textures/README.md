# Video Textures

## Synopsis

In this assignment we will be applying our Computational Photography magic to video, with the purpose of creating [video textures](http://www.cc.gatech.edu/cpl/projects/videotexture/) (infinitely looping pieces of video). These are basically gifs with very smooth transitions, as seen in the lectures, and the process is described in the Scholdl, et al. paper *Video Textures*. You are required to take your own input video in order to generate a smooth original video texture.

To help you with this assignment, you should carefully read the required technical paper, and watch the associated lessons:
   - ["Video Textures"](https://dl.acm.org/doi/10.1145/344779.345012) (Schödl, A.,  Szeliski, R., Salesin, D., & Essa, I.)
   - Lesson 06-01: Video Processing
   - Lesson 06-02: Video Textures
   - Lesson 06-03: Video Stabilization

To access the paper on the ACM website, select Get Access > Sign in > Institutional Login (select Georgia Institute of Technology). You will be redirected to GT's central Single Sign-On, where you should enter your GT username (e.g. gburdell3) and password. You should have the option to view the paper in eReader or PDF.  

## Instructions

### 1. Implement the functions in the `textures.py` file.

- `returnYourName`: Return your Gradescope official name.
- `videoVolume`: Take a list containing image numpy arrays, and turn them into a single array which contains the entire video volume.
- `computeSimilarityMetric`: Find the "distance" between every pair of frames in the video.
- `transitionDifference`: Incorporate frame transition dynamics into a difference matrix created by computeSimilarityMetric.
- `findBiggestLoop`: Find an optimal loop for the video texture. (NOTE: part of your task is to determine the best value for the alpha parameter.)
- `synthesizeLoop`: Take our video volume and turn it back into a series of images, keeping only the frames in the loop you found. 

The docstrings of each function contains detailed instructions. You may only have a limited number of submissions for each assignment, so you are *strongly* encouraged to write your own unit tests. **Do *NOT* try to use the autograder as your test suite.** The `test_textures.py` file is provided to get you started. Your code will be evaluated on input and output type (e.g., uint8, float, etc.), array shape, and values. Be careful regarding arithmetic overflow!

When you are ready to submit your code, you can submit it to the Gradescope autograder for scoring, but we will enforce the following penalty for the submissions:

- <= 20 submissions: No penalty 
- <= 30 but >10 submissions: -5 penalty
- <= 40 but >20 submissions: -10 penalty
- more than 40 submissions: -20 penalty

**Notes:**
- Downsampling your images will save processing time during development. Larger images take longer to process.

- The `main.py` script reads files in the sorted order of their file name according to the conventions of python string sorting; it is essential that file names are chosen so that they are in sequential order or your results will be wrong. 

### 2. Use these functions on the sample (candle) images to make a video texture

Use the images in the `videos/source/candle` directory to create a smooth video texture. We provided these images for testing -- _do not include these images in your resources submission_ (although the output should appear in your report). Refer to Section 4 below on finding a good alpha.

### 3. Use these functions on your own input images to make an ORIGINAL video texture - _READ CAREFULLY_

For this section of the assignment, **you are required to take YOUR OWN input video and extract the image frames to generate your own original video texture result. Do NOT use video clips from the web**. Refer to Section 4 below on finding a good alpha.

See the Appendix - “Working with Video” below, for instructions to extract image frames from video clips, and tips on converting the image frames back to a video gif. **Host your video gif & input frames on GT Box. See Section 6 below for instructions**. Provide a working sharing link in your report so that anyone with the link may view the video gif. 

&#x1F534; **IMPORTANT REMINDER:** You are responsible to ensure that links to your GIFs in your report function properly. _We will not accept regrade requests if your images are missing because the links are expired or unviewable._

### 4. Finding a good alpha
The last bit of computation is the alpha parameter, which is a scaling factor. The size of the loop and the transition cost are likely to be in very different units, so we introduce a new parameter to make them comparable. We can manipulate alpha to control the tradeoff between loop size and smoothness. Large alphas prefer large loop sizes, and small alphas bias towards short loop sizes. You are looking for an alpha between these extremes (the goldilocks alpha). Your findBiggestLoop function has to compute this score for every choice of start and end, and return the start and end frame numbers that corresponds to the largest score. 

You must experiment with alpha to generate a loop of reasonable length (and that looks good) - more than one frame, and less than all of the frames. Alpha may vary significantly (by orders of magnitude) for different input videos.  When your coding is complete, the `main.py` program will generate visualization images of the three difference matrices: similarity, transition, and scoring.  These matrices may help you identify good alpha values.

&#x1F534; **IMPORTANT REMINDER:** Discussing the alpha values you experimented with before deciding on the best alpha value for each video texture (candle and your own) is required in your report. Make note of the values while you experiment and how they affect your results. Please read through the provided template for more information before starting on the assignment.

### 5. Complete the LaTeX Report

Use the `A5_Video_Textures_Template.zip` report template provided in the class repository. **The LaTeX template specifies all of the images, data, and questions you must answer.** Follow the instructions in the [Course Setup](https://github.gatech.edu/omscs6475/assignments/tree/master/Course_Setup) to upload it in Overleaf. If you have a different favorite LaTeX program, you may use it; the template should be generally compatible.

&#x1F534; **IMPORTANT REMINDER:** **It is really important that you read the entire LaTeX template.** A couple items that we want to highlight from the report because they usually get missed every semester: A). You will be asked to circle the best score location on your scoring matrix for **BOTH** the sample and original result B). You will be asked to provide images of the transition matrices and images of the start and end frames for **BOTH** the sample and original result. **THE CAPTIONS FOR EVERY IMAGE MATTER**. Pay close attention to the instructions in the template, and ask on Ed if you are unsure. Do not give up these easy points. 
   
  - **The total size of your report+resources must be less than 20MB** for this assignment. If your submission is too large, you can reduce the scale of your images or report. You may resize your images using `cv2.resize`. You can compress your report using [Smallpdf](https://smallpdf.com/compress-pdf).
  - **The total length of your report is 6 pages maximum (including Appendix).** This report is expected to be five pages for most students, unless you decide to submit extra observations and images in the appendix (no extra credit, but the TA staff enjoys interesting work!)
  - **You are required to use the LaTex format for your report.** Different report organization or changing section titles and questions will receive a deduction. You may add additional relevant information or images within the structure of the report, as long as all requirements are met.
  - **You are required to provide References. Everyone is expected to have at least two references**; these should include StackOverflow answers that you relied on for specific commands, valuable tutorials, blogs, helpful Ed posts, and textbook references. Provide URLs and site or page names, typical book information and page numbers, etc. We should be able to easily view your references if needed.

**Save your report as `report.pdf`**

### 6. Upload Results to GT Box

[GT Box](https://oit.gatech.edu/box) provides unlimited space for GT students. Keep in mind that there is a 50GB individual file limit.

Create a directory on GT Box called `A5_Video_Textures` that includes:
1. Your final candle video texture gif
2. Your original video
3. Your final original video texture gif
4. A folder called `original_input_frames` that has all of the frames from your original video. There is no need to include a folder of frames for the sample candle.

Provide a **working** link to your `A5_Video_Textures` directory in your report. Check permissions of the link before pasting it into your report. You will be asked to provide this link on both Page 1 and Page 2 of your report. 

**Do NOT submit the contents of the `A5_Video_Textures`directory in your `resources.zip`. Providing a working link to your GT Box directory in your report is a strict requirement.**

### 7. Complete and Submit the Report on Gradescope AND Canvas

1. **Gradescope:** Submit your Report PDF to **A5-Video Textures Report.** Once it is uploaded, you may look through the pages to make sure you uploaded the right document and all parts are displayed properly. There is no limit to Report submission attempts, only Resources attempts. After you upload your PDF, you will be taken to the "Assign Questions and Pages" section that has a Question Outline on the left hand side. These outline items are determined by the Instructors. **For each question - select the question, and then select ALL pages that go with that question.** This is important because any pages that you do not select for the corresponding question might get missed during grading.

We advise that you download your own PDF submission from Gradescope and test the GT Box link one more time after submitting. We cannot stress enough that your Box link must work. We cannot grade anything that we cannot see. There will be a big additional deduction for broken links and we do not accept links after the assignment closes. 

2. **Canvas:** submit your Report PDF on **Canvas > Assignments > A5-Video Textures Report.** This allows your report to be uploaded to the Peer Feedback system. Forgetting to submit to Canvas by the late deadline will result in a deduction. 

### 8. Submit the Code on Gradescope

Create an archive named `resources.zip` containing your `textures.py` file. Submit your `resources.zip` to **A5-Video Texture Resources** in Gradescope for grading.

You are required to submit only your code in `resources.zip`. All of the other required resources for this assignment must be hosted online and working links must be provided in your report (see Section 6 above). 

Once you’re finished with submitting this assignment, give yourself a pat on the back (or a hug!) because you’re done with the homework assignments for this course!

**Notes:** 

   - **EXIF metadata:** When including or sharing images, make sure there are no data contained in the EXIF metadata that you do not want shared (i.e. GPS). If there is, make sure you strip it out before submitting your work or sharing your photos with others. Normally, we require that your images include aperture, shutter speed, and ISO. You may use `pypi/exif` library in a separate python file to strip GPS data if you wish.  Make sure you do not use an app that strips all exif from the image. 

  - **DO NOT USE 7zip.** We've had problems in the past with 7z archives, so please don't use them unless you don't mind getting a zero on the assignment.
  
  - **Note for All users:** If you zip your files, do it from within the folder by selecting the files.  Do not zip the directory.  The additional file structure will prevent Gradescope from identifying your files.


## Criteria for Evaluation

Your submission will be graded based on:

  - Correctness of required code
  - Creativity & overall quality of results
  - Completeness and quality of report


## Appendix - Working with Video

Working with video is not always user friendly. It is difficult to guarantee that a particular video codec will work across all systems. In order to avoid such issues, the inputs for this assignment are given as a sequence of numbered images.

You may use tools such as Gimp and others to break your own video into separate image frames. Alternatively, there are tools discussed below that you can use to split your own videos into frames, and to reassemble them into videos. These programs may not work for everyone depending on your operating system, software versions, etc. You will need to find something that works for you, so you can produce your results as a gif! Googling for image->gif tools online and asking other students on Ed may help.

**ffmpeg (avconv)**
These are free and very widely used software for dealing with video and audio.

- ffmpeg is available [here](http://www.ffmpeg.org/)
- avconv is available [here](https://libav.org/avconv.html)

Example ffmpeg Usage:

You can use this command to split your video into frames:
```ffmpeg -i video.ext -r 1 -f image2 image_directory/%04d.png```

And this command to put them back together:
```ffmpeg -i image_directory/%04d.png out_video.gif```

**imageio (python library)**
You can also create a gif from a series of images using the imageio library. Here is an [example](https://stackoverflow.com/a/45258744).
