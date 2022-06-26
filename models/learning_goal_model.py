"""
learning_goal_model.py
------------------------
This contains our LearningGoalModel class, which will be in charge of
storing the tagged learning goal data that is provided by a user.
"""

class LearningGoalModel:
    """
    class LearningGoalModel
    ------------------------
    This is a class to represent our tagged learning goals.
    """
    
    def __init__(self, path_to_data):
        """
        Initializes our model with the path to the tagged learning goals
        (TODO: we need to choose whether this will be a folder or a single file)
        """
        self.path_to_data = path_to_data
        self.data = self.load_data()

    def load_data(self):
        """
        TODO: implement this to load the data from `self.path_to_data`
        """
        pass
    
    def get_data(self):
        """
        Returns the data stored by LearningGoalModel
        (in the future, we might want our model to do more things, but who know? 
        i vaguely think that this is standard practice)
        """
        return self.data