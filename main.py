"""
main.py
--------
This is our main file for the command-line version of the SmartSTEM tool.

We'll need to think about this further, but for now a user will run our application
by running this specific python file.
"""

from models.analysis_model import AnalysisModel

def main():
    # introduction statement
    print('Hello! Welcome to the SmartSTEM educational software tool :)')

    # ask for data files
    path_to_learning_goal = input('Please enter the path to your tagged learning goals file: ')
    path_to_score = input('Please enter the path to your downloaded student scores: ')

    # ask for path to final output
    path_to_output = input('Please enter the path where you would like to store your output: ')

    # create our analysis model
    analysis_model = AnalysisModel(
        path_to_learning_goal_data=path_to_learning_goal,
        path_to_score_data=path_to_score,
        path_to_output=path_to_output
    )

    # generate outputs and done!
    print('Thank you! Generating graphs...')
    analysis_model.generate_graphs()
    print(f'Done generating graphs! Please see {path_to_output} for your generated information.')

if __name__ == '__main__':
    main()