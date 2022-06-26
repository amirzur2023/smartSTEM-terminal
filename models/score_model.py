"""
score_model.py
------------------------
This contains our ScoreModel class, which will be in charge of
storing the score data downloaded from GradeScope by a user.
"""

class ScoreModel:
    """
    class ScoreModel
    ------------------------
    This is a class to represent our student score data.
    """
    
    def __init__(self, path_to_data):
        """
        Initializes our model with the path to the student scores
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
        Returns the data stored by ScoreModel
        """
        return self.data