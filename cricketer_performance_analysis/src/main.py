#!/usr/bin/env python
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import warnings

# Load environment variables from .env file (located at root, 3 levels up)
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from crew import CricketAgent

def run():
    """
    Run the crew.
    """
    cricketer_name = None
    year = None
    
    # Get from command line arguments
    if len(sys.argv) > 1:
        cricketer_name = sys.argv[1]
    if len(sys.argv) > 2:
        year = sys.argv[2]
    
    # Get from environment variables if not provided
    if cricketer_name is None:
        cricketer_name = os.getenv('CRICKETER_NAME', 'Virat Kohli')
    if year is None:
        year = os.getenv('YEAR', '2023')
    
    print(f"Analyzing Cricketer: {cricketer_name} (Year: {year})")
    
    inputs = {
        'cricketer_name': cricketer_name,
        'year': year
    }
    CricketAgent().crew().kickoff(inputs=inputs)


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         CrewAiAgents().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         CrewAiAgents().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         CrewAiAgents().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")