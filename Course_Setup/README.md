# CS 6475 Computational Photography: Course Setup

## Instructions

This course setup document is designed to help you get started in the course during the first couple of days. This is not a graded assignment (i.e. you do not have to submit a report and resources to Gradescope), but it is important that you complete it immediately so you can have a working environment before starting on Notebook 1 and Assignment 0. Do not wait to start setting up your environment, otherwise you might waste time trying to resolve any technical issues. 

For this course setup, you will perform the following:
#### 1. Review the Syllabus and Schedule on the Course Website
#### 2. Confirm you have access to the course Canvas and Ed
#### 3. Clone the course repository
#### 4. Set up the course python3 environment using Anaconda
#### 5. Log in to Gradescope 
#### 6. Log in to Peerfeedback
#### 7. Log in to Overleaf - LaTeX report tool
#### 8. Review Course Policies and GT's Honor Code and take the graded Plagiarism Quiz
#### 9. Take the Exemplary Report Permission Quiz
#### 10. Cameras, Tripods and EXIF data
#### 11. Complete Notebook 1 and Quiz 1
#### 12. Complete Assignment 0 


## 1. Review the Syllabus and Schedule on the Course Website

It is very important that you review the [CS 6475: Computational Photography Course Website](https://omscs6475.cc.gatech.edu). This site has all of the course information, including the course syllabus, complete course schedule, and required reading materials. If you have any questions regarding any of the information on the website, please ask on Ed.


## 2. Confirm Canvas and Ed Access 

Review the [Course Policies, Section 3F: Official Course Communication](https://omscs6475.cc.gatech.edu/course-syllabus/) for important information regarding Ed.  

**Canvas** - If you have not already, please check that you have access to CS-6475-001 on Canvas. If you just enrolled in the course, it might take some time for you to see the course in Canvas, so give it a couple days. If you still do not see the course after waiting, message the Instructors on Ed.

**Ed** - If this is your first time using Ed as a GT student, go to [https://edstem.org/us/login](https://edstem.org/us/login) and enter your **GT email address**. You will be redirected to GT's central Single Sign-On, where you should enter your GT username (e.g. gburdell3) and password. Once you are logged in, you will see a Dashboard with your courses that you have access to. Once you are officially added to our Canvas roster, you will be added to the course Ed roster as well. We will do a daily Ed roster check during Week 1 to make sure the Ed and Canvas rosters are synced. Once you have access to the course Canvas, you can also access Ed by selecting 'Ed Discussion' in our Canvas sidebar. 

Once you have access to Ed, go ahead and introduce yourself!


## 3. Clone the Course Repository

Throughout the course, assignments and projects will be released via the course GitHub repository. To clone the course repository to your local machine, make sure you have [Git](https://git-scm.com/downloads) installed and the executable is on your system PATH. You can verify that you have Git installed and on your system PATH by executing the command `git --version` from a terminal. Clone the repository by issuing the command `git clone https://github.gatech.edu/omscs6475/assignments.git`.

Note: If you want to use the Git repository locally to track your changes, you should checkout a new branch immediately after cloning: `git checkout -b <branch>`. See [here](https://git-scm.com/docs/git-checkout) for more information on git-checkout. 

#### Receiving Updates

Updates can be retrieved by running `git pull` in the root directory of the repository from your terminal. It is important to pull the latest changes when an assignment/project is released, or when the Instructors make an announcement that there have been updates. See [here](https://git-scm.com/docs/git-pull) for more information on git-pull.


## 4. Set up the Virtual Environment Using Anaconda

**We require all students use the same python3 (3.8.xx) class environment.** This course uses large third-party libraries (NumPy, SciPy, OpenCV, etc.) for assignments and projects. Severe errors may result if your environment uses different versions of python or the required libraries than the versions we specified in the `cs6475.yml` file, up to causing your code to crash and earn a zero.
 
The standardized class environment, CS6475, allows for proper execution of your code across your local environment, the remote autograder, Instructors' machines that must run your code,  and makes sure that the assignment code we provide works as expected. Follow the directions to setup an Anaconda virtual environment that includes the correct version of all required software and libraries.

**NOTE: ALTHOUGH THE CONDA ENVIRONMENT HAS BEEN TESTED FOR CROSS-PLATFORM COMPATIBILITY WITH THE AUTOGRADER ENVIRONMENT, THE CONDA ENVIRONMENT IS NOT THE EXACT ENVIRONMENT YOUR CODE IS RUN IN BY THE AUTOGRADER. YOU ARE RESPONSIBLE TO ENSURE YOUR CODE WORKS ON THE AUTOGRADER SYSTEM. IT IS NOT ENOUGH THAT IT WORKS ON YOUR SYSTEM IN THE CONDA ENVIRONMENT.**

- **Use Anaconda to download and install (run) the latest supported 64-bit Python3 version, (which will be higher than 3.8) for your OS** [here](https://www.anaconda.com/download). Scroll to the bottom to see the list of installers. Do NOT download a Python2 version. Downloading the latest 64-bit Python3 version of Anaconda will permit conda to create the CS6475 environment with the correct 3.8.xx version, below. This procedure will work for Linux, MACOSX, and Windows. 

- **Resources:** Anaconda Documentation for installation on 
[Windows](https://docs.anaconda.com/anaconda/install/windows/), 
[macOS](https://docs.anaconda.com/anaconda/install/mac-os/), 
and [Linux](https://docs.anaconda.com/anaconda/install/linux/)

- **Open a terminal window (you can use Anaconda Prompt) and go to the local course repository directory you cloned in the previous section.** The `cs6475.yml` file should be there. This step will take a few minutes, as conda will gather all of the required supporting packages for the named versions, including python 3.8.xx.  Create the CS6475 virtual environment by running 

```
conda env create -f cs6475.yml

(base) C://your current path
```

- **Activate the CS6475 virtual environment from the terminal by executing the following command:**

```
conda activate CS6475

(CS6475) C://your current path
```

**NOTE 1: Do NOT let your IDE update file/library versions in the CS6475 class environment.**  This will undo all the work you just did to setup the environment, and your will need to follow the next note before you recreate the env. 

**NOTE 2: If your initial CS6475 environment gets messed up and you need to recreate it,** make sure that you remove the environment first by running `conda env remove --name CS6475`. 

**NOTE 3: for Linux & MACOS users only,** `conda activate` and `conda deactivate` only work on conda 4.6 and later. For conda versions prior to 4.6, Linux and macOS users should use `conda source activate` and `conda source deactivate` if necessary.

**Resource:** Anaconda Documentation - [Creating an environment from an environment yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

Once the virtual environment has been activated, you can execute code from the same terminal. It's worth mentioning that popular Python IDEs, such as PyCharm, VSCode or Atom, facilitate using an Anaconda environment as the interpreter for your project or repository. This course setup will not go over those steps, as they will vary from tool to tool.


### Validate Environment Setup

You can test that your environment is setup correctly by opening a terminal, activating the virtual environment, and running the `test.py` file in the root folder of this repository. The test file performs basic checks to confirm that the required versions of all packages are correctly installed. 

```
~$ conda activate CS6475
(CS6475) ~$python test.py
     
--------------------------------------------------
Ran 5 tests in 0.xxx s

OK
```

**NOTE 4:** A small number of students may need to run `python3 test.py` if the above command crashes. 

**NOTE 5:** If you prefer to manage your own environment, we cannot provide support for students who choose to do so. In any event, the file `cs6475.yml` which is provided in the class repo will always have the current list of major libraries and their respective version numbers. These libraries are packaged automatically by conda as it follows the `yml` file, so only students who choose to develop their own environments will need to individually adhere to this list. You will need the specific library versions **and their numerous dependencies.**


## 5. Log in to Gradescope 

Log in to [Gradescope](https://www.gradescope.com/) using your GT username and password and you should be able to see the course listed in your dashboard. This might take a 3-4 days to take effect if you just enrolled into the course, so be patient. Once you have access to the course Canvas, you can also access Gradescope by selecting 'Gradescope' in our Canvas sidebar. 


We will be using Gradescope to process assignment/project submissions in this course. Each assignment/project will normally require submission of a report (pdf) and resources (code files and images). The report will be submitted separately from the resources, each under its corresponding assignment on Gradescope. When you submit code to the Gradescope autograder, you should be able to see the output of the autograder within a few minutes. Each assignment/project will have submission instructions, so make sure you pay really close attention to them.


## 6. Log in to Peer Feedback

Log in to [Peer Feedback](https://peerfeedback.gatech.edu/app/home) with your GT username and password and make sure that you are able to see this course. You will be assigned Peer Feedback tasks starting with Assignment 1. The Instructors normally assign Peer Feedback after an assignment closes (usually after the 2-late day submission deadline passes). An announcement on Ed will be made when Peer Feedback is released for each assignment/project. 

Instructions on Peer Feedback tasks for this course are given on the course website [here](https://omscs6475.cc.gatech.edu/peer-feedback/). 


## 7. Log in to Overleaf Professional for LaTeX reports

Your assignment and project reports will be formatted in LaTeX, in the same style as technical papers. The TeX format provides a small font with plenty of writing space and compact image handling.  No other format will be accepted. We will provide a detailed template for each assignment via the GitHub repository to make this easier for you and the TA graders. If you already use a TeX program that you like, you may continue to use it with our templates. 

If you have never used LaTeX, Georgia Tech has a contract with Overleaf, and a free Overleaf Professional account is available for each student. Overleaf is an online program with excellent help available that can be sync'd with Dropbox, provides storage, and retains your version history. [Access Overleaf here.](https://www.overleaf.com/edu/gatech) 

### Registering for a Professional Overleaf Account through Georgia Tech
1. Register using your GaTech email address: [Access GaTech overleaf from the Register or Sign Up buttons](https://www.overleaf.com/edu/gatech) 
2. Respond to the confirmation email that is sent to your GaTech email after registering.
3. Done! 

#### Importing a Report Template into Overleaf 
Upon creating your account, you will have a welcome page (left) with a button to **Create First Project** or if you already have an account, you may have the normal dashboard with a button to create a **New Project**. Select **Create First/New Project → Upload Project** and choose your template zip file.

All of your assignments will include a report template zip file for import into overleaf. The template will contain a skeleton consisting of the section headings, questions, and frameworks for your images, along with further guidance to help you use it.

For more information on how to use specific LaTeX commands, please refer to Overleaf's help [here.](https://www.overleaf.com/learn)


## 8. Take the Plagiarism Quiz on the Course Policies and Georgia Tech's Honor Code

We take Academic Integrity very seriously and it is very important that our students understand the [Course Policies](https://omscs6475.cc.gatech.edu/course-syllabus/) (see Section III of the Course Syllabus) and [Georgia Tech's Academic Honor Code](https://policylibrary.gatech.edu/student-life/academic-honor-code). Once you review the information, take the Plagiarism Quiz on Canvas. This graded quiz has 15-20 multiple choice questions aimed to help students understand our CS 6475 policies in depth. The scenarios have all occurred in this class over time. You are allowed unlimited attempts, open sources, and only your final score will count towards your participation grade. See the Course Schedule for the quiz's due date.

**You can access this quiz by going to Canvas → Quizzes → Assignment Quizzes.**

## 9. Take the Permission Quiz on sharing exemplary work

After we finish grading the assignments, we will pick a few reports and share them as Exemplary Reports on Canvas. In the past, before work was shared, we had to email every student in order to get permission, which delayed the sharing of the reports immediately after grades were released. 

To make things easier and faster, we need you to complete a “Yes/No” quiz that will give our entire CS6475 staff permission beforehand to share any of your assignments and projects with the class, if chosen. If you are not comfortable sharing your reports with your peers, do not hesitate to select “No”. You will not be penalized. If, for whatever reason, you select “Yes” in the quiz, but then you change your mind for a certain assignment or project and want your work removed from Canvas, if chosen, please message the Instructors on Ed and your report will be removed immediately. If you select "No" or do not take the quiz at all (we assume the answer is "No" if you don't), but change your mind later on and wouldn't mind having your work shared, if chosen, feel free to take the quiz again.

**This quiz is ungraded and already available on Canvas. You can access this quiz by going to Canvas → Quizzes → Surveys**.

After the semester is over, we will not share your work in future semesters.  
 
## 10. Cameras, Tripods, and EXIF Data

You are allowed to use any kind of camera  -- anything from smartphones to high-end DSLR cameras -- for this class. Most students have successfully completed assignments using only a smartphone, so do not feel that you need to go and buy a fancy camera (although many students have used this class as an excuse to buy the camera of their dreams).

### Required Manual Controls
Many assignments have specific setting requirements for **exposure time, aperture, and ISO.** Information is available online on camera settings, and we expect you to find it for your device. You will need to be able to manually control exposure time and ISO for several assignments. Note that aperture is fixed on almost all smartphones, therefore it is already "manually controlled" for those devices. There are apps that can help smartphones, but since apps constantly change, we cannot make recommendations for them. Feel free to share names of apps with your classmates on Ed. 

  - Exposure time in seconds (ex: 1/2000 s, 1/30 s)
  - Aperture (ex: f 2.8, f16) 
  - ISO (ex: ISO 100, ISO 1600)

### EXIF Metadata
To help you get used to your camera and its settings, you will be asked to provide some technical information about your photograph on Assignment 0. You should immediately find out how to get the EXIF data for the camera you plan to use in this course. Google it!

EXIF data is recorded as a part of digital images, and can be found on your phone, in your digital camera, or on your computer. **Image editing can erase the data, so record the settings before playing with your image.** Make a copy of your original image before completing actions such as resizing and filtering, so that you do not lose this info. Search online for information on finding EXIF data for your device if you are not sure how to find it or do not know what it is. You can also discuss EXIF data, and how to keep it, on Ed.

**Location privacy:** When including or sharing images, make sure there are no data contained in the EXIF metadata that you do not want shared (i.e. GPS locations). If there is, make sure you strip it out before submitting your work or sharing your photos with others. You may use the python [pypi-exif](https://pypi.org/project/exif/) library to write a python file to strip GPS data if you wish.  Make sure you do not use an app that strips all EXIF from the image. 

### Required Stable Camera Position: Tripods or Supports
Several assignments require long exposures or keeping the camera motionless between successive shots, which is challenging. Learning to use your time delay feature will help prevent camera motion during individual shots. You can either use a tripod or an improvised support. Students have successfully created homemade tripods to stabilize their smartphones if they did not have a tripod. Google homemade or improvised camera tripods for ideas, or check shopping site prices for bargains. Discuss your ideas and sources on Ed. 

It is harder to improvise for larger cameras and DSLRs. There are bargain tripods that work reasonably well, or try to borrow one.  You may be able to improvise something with ingenuity. 


## 11. Complete Notebook 1 and Quiz 1

This notebook introduces some key aspects of the NumPy and OpenCV APIs as they relate to image manipulation. These techniques are building blocks that can be used extensively throughout the course. Although there are no deliverables for these notebook exercises, there is a **graded Canvas quiz** (see course schedule for due date). You are free to discuss the notebooks on the forums, but make sure that you refrain from giving away quiz questions and answers. **We cannot recommend enough that you start on this first notebook immediately because it can be a great reference for the assignments/projects in this course. If you are unfamiliar with python, reviewing Notebook 1 alongside Assignment 0 may be very helpful.**

**The Instructors will make an announcement on Ed once Notebook 1 and its corresponding quiz is released on Day 1 of class. The quiz will be due a week later (see course schedule for exact due date).**


## 12. Complete Assignment 0

This is a short introductory assignment to help you become familiar with the course submission process. You will be required to write some python code, create a report using a LaTeX template, and submit both your report and resources to Gradescope. It is very important to get Assignment 0 completed immediately before starting on Assignment 1.

**The Instructors will make an announcement on Ed once Assignment 0 is released on Day 1 of class. It will be due about a week later (see course schedule for exact due date).**
