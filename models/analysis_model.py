"""
analysis_model.py
------------------

This contains our AnalysisModel, which will use the data
from the LearningGoalModel and ScoreModel in order to generate 
graphs at a specified output location
(we might want to break this down in the future, since this is likely
going to be our biggest file, but i'm not quite sure about how -- please
suggest ideas!!)
"""

import os

import numpy as np
from matplotlib import pyplot as plt

from models.learning_goal_model import LearningGoalModel
from models.score_model import ScoreModel

class AnalysisModel:
    """
    class AnalysisModel
    --------------------
    A model that generates our analysis graphs, from the provided
    learning goal data and score data. 

    Its key function is `generate_graphs()`, which will generate all 
    of the graphs we want 
    (in the future, we can think about only generating specific graphs)
    """

    def __init__(self, path_to_learning_goal_data, path_to_score_data, path_to_output):
        # load data
        self.learning_goal_model = LearningGoalModel(path_to_learning_goal_data)
        self.score_model = ScoreModel(path_to_score_data)

        # create the output path
        self.path_to_output = path_to_output
        if not os.path.exists(self.path_to_output):
            os.mkdir(path_to_output)

    def generate_example_graph(self):
        """
        Generates one example graph (a smiley face!)
        """
        # you can ignore this chunk of code (I don't understand it either),
        # i copied this from stackoverflow to create a smiley face
        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(1,1,1, aspect=1)

        ax.scatter([.5],[.5], c='#FFCC00', s=120000, label="face")
        ax.scatter([.35, .65], [.63, .63], c='k', s=1000, label="eyes")

        X = np.linspace(.3, .7, 100)
        Y = 2* (X-.5)**2 + 0.30

        ax.plot(X, Y, c='k', linewidth=8, label="smile")

        ax.set_xlim(0,1)
        ax.set_ylim(0,1)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

        # this is the important part: we want to save our figure under the name
        # `example_graph.png` in the user-specified output folder
        save_path = os.path.join(self.path_to_output, 'example_graph.png')
        plt.savefig(save_path)
    
    def generate_graphs(self):
        self.generate_example_graph()
        # BIG TODO: generate more graphs!!
        # (maybe generate_learning_goal_distribution_graph,
        # or generate_average_student_performance_graph)