"""
CrewAI configuration and setup module.
"""

from crewai import Agent, Crew, Task
from typing import List, Dict
import yaml
from pathlib import Path


def load_config(config_path: str) -> Dict:
    """Load YAML configuration file."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def create_agents_from_config(config_path: str = None) -> List[Agent]:
    """Create CrewAI agents from YAML configuration."""
    if config_path is None:
        # Get the directory where this file is located
        base_dir = Path(__file__).parent.parent
        config_path = base_dir / 'src' / 'config' / 'agents.yaml'
    
    config = load_config(str(config_path))
    agents = []
    
    for agent_config in config.get('agents', []):
        agent = Agent(
            role=agent_config.get('role'),
            goal=agent_config.get('goal'),
            backstory=agent_config.get('backstory'),
            verbose=agent_config.get('verbose', True),
            allow_delegation=agent_config.get('allow_delegation', False)
        )
        agents.append(agent)
    
    return agents


def create_tasks_from_config(agents: List[Agent], config_path: str = None, topic: str = None) -> List[Task]:
    """Create CrewAI tasks from YAML configuration.
    
    Args:
        agents: List of agents to assign tasks to
        config_path: Path to tasks configuration file
        topic: Optional topic to replace {topic} placeholder in task descriptions
    """
    if config_path is None:
        # Get the directory where this file is located
        base_dir = Path(__file__).parent.parent
        config_path = base_dir / 'src' / 'config' / 'tasks.yaml'
    
    config = load_config(str(config_path))
    tasks = []
    
    # Create a dictionary to map agent roles to agent objects
    agent_dict = {agent.role: agent for agent in agents}
    
    # Default topic if not provided
    if topic is None:
        topic = "the given topic"
    
    for task_config in config.get('tasks', []):
        agent_role = task_config.get('agent')
        agent = agent_dict.get(agent_role)
        
        if agent:
            # Replace {topic} placeholder in description and expected_output
            description = task_config.get('description', '').format(topic=topic)
            expected_output = task_config.get('expected_output', '').format(topic=topic) if '{topic}' in task_config.get('expected_output', '') else task_config.get('expected_output', '')
            
            task = Task(
                description=description,
                agent=agent,
                expected_output=expected_output
            )
            tasks.append(task)
    
    return tasks


def create_crew(agents: List[Agent] = None, tasks: List[Task] = None,
                agents_config: str = None,
                tasks_config: str = None,
                topic: str = None) -> Crew:
    """Create a CrewAI crew with agents and tasks.
    
    Args:
        agents: Optional list of agents (will be loaded from config if not provided)
        tasks: Optional list of tasks (will be loaded from config if not provided)
        agents_config: Path to agents configuration file
        tasks_config: Path to tasks configuration file
        topic: Optional topic to replace {topic} placeholder in task descriptions
    """
    if agents is None:
        agents = create_agents_from_config(agents_config)
    
    if tasks is None:
        tasks = create_tasks_from_config(agents, tasks_config, topic=topic)
    
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )
    
    return crew

