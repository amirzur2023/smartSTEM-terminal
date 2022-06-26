# SmartSTEM Education Software Tool

This tool will help us use teacher-specified learning goals in order to produce relevant analysis that will guide the study habits of students and the curriculum development of teacher!

# Set-Up

In order to get going with the tool, we need to take the following steps:

## Clone Repository

Clone this repository using the `git clone` command:

`git clone https://github.com/amirzur2023/smartstem-terminal.git`

Then go into the `smartstem-tool` repository to get started!

`cd smartstem-tool`

## Install packages

There are two options for package installations: using Anaconda or using pip install.
Go with whichever you feel more comfortable, but for our project you only need one of the two.

### 1. Install with Anaconda

First, we will create a new envrionment called `smartstem`. We will have it start with the default `anaconda` package, which will include all libraries I image we'd need (pandas, numpy, etc.).

`conda create -n smartstem python=3.9 anaconda`

Next, we'll activate this environment with the following code:

`conda activate smartstem`

And we're all set! Whenver you're done, you can deactivate your environment using

`conda deactivate`. 

### 2. Install with Pip

I created a `requirements.txt` file for the packages that the project uses (and we might update this list as we do more analysis). In order to install these requirements, run

`pip install -r requirements.txt`

and you're good to go!

# Running the Code

Our `main.py` file will act as our "app". For a user to run the app on their computer they should run:

`python main.py`

Right now, our code will ask for a path to the learning goal files and a path to the score files, and lastly for the path to the output. It will then create a small smiley face in the output folder specified :)

# Understanding the Code

I wasn't too sure how to break our code down, but I figured we will have three main files:

## `learning_goal_model.py` and `score_model.py`

These files will represent our learning goal data and student score data, respectively. I honestly don't think these will do much more than read the data provided and pass it on, but I believe this is good practice in case we ever want to extract anything more from the data (or keep it safe).

## `analysis_model.py`

This is going to be where most of our code will be. The `AnalysisModel` class will be in charge of using the data stored in `LearningGoalModel` and `ScoreModel` classes in order to generate the analysis graphs for instructors. 

These analysis graphs can include distribution of learning goals, average student performance on an exam, or anything else we've done in our analysis so far!

# Next Steps

I left a few **TODO** statements throughout the code files for things we can start doing. I'll try to summarize them here:

* Code up the `load_data()` function in the `LearningGoalModel` class, which should read in the provided learning goal data. For now, this can be a single file for a single exam, but we should think about how we want these files to be structued for the future (do we want a folder? a single file? should the user specify which exams/years/questions to load?).

* Code up the `load_data()` function in the `ScoreModel` class, which should read in the provided score data. This should hopefully be pretty similar to the previous task, but not exactly the same, since the files are structured differently.

* Add more graphs in the `AnalysisModel`. Right now, our analysis model creates a single graph (a smiley face). Once we have data loaded, either from `LearningGoalModel` or `ScoreModel`, see if we can use it to generate a simple graph. 
