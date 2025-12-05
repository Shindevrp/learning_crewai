"""
Main entry point for the CrewAI application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from crewai import Crew
from crew_setup import create_crew

# Load environment variables from .env file (located at root, 3 levels up)
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


def main(topic: str = None):
    """Main function to run the CrewAI crew.
    
    Args:
        topic: Optional topic to research and write about. 
               If not provided, you can set it via environment variable RESEARCH_TOPIC
               or it will use a default generic topic.
    """
    # Get topic from environment variable or parameter
    if topic is None:
        topic = os.getenv('RESEARCH_TOPIC', None)
    
    print("Initializing CrewAI...")
    if topic:
        print(f"Research Topic: {topic}")
    
    # Create the crew from configuration files
    crew = create_crew(topic=topic)
    
    print("Crew created successfully!")
    print("\nStarting crew execution...")
    
    # Run the crew
    result = crew.kickoff()
    
    print("\n" + "="*50)
    print("Crew Execution Completed!")
    print("="*50)
    print("\nResults:")
    print(result)
    
    return result


if __name__ == "__main__":
    import sys
    
    # Allow topic to be passed as command line argument
    topic = sys.argv[1] if len(sys.argv) > 1 else None
    main(topic=topic)

