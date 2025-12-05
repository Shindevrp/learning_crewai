# Research Writer Crew - CrewAI Project

A CrewAI project that uses YAML configuration files for agents and tasks. This project creates a research and writing crew that can research any topic and produce well-written articles.

## Setup

1. **Activate the virtual environment:**
   ```bash
   # From the learning_crewai root directory
   source venv/bin/activate
   ```

2. **Set up environment variables:**
   Create a `.env` file in the `learning_crewai` root directory (one level up from this project folder) with your API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   Note: The `.env` file is shared across all projects in the `learning_crewai` directory.

3. **Run the project:**
   ```bash
   cd research_writer_crew/src
   python main.py
   ```

## Changing the Research Topic

You can change the research topic in **3 different ways**:

### Method 1: Command Line Argument (Recommended)
Pass the topic as an argument when running:
```bash
cd research_writer_crew/src
python main.py "Artificial Intelligence in Healthcare"
python main.py "Climate Change Solutions"
python main.py "Space Exploration"
```

### Method 2: Environment Variable
Set the topic in your `.env` file (at the root `learning_crewai` directory):
```bash
RESEARCH_TOPIC=Quantum Computing Applications
```

Then run normally:
```bash
cd research_writer_crew/src
python main.py
```

### Method 3: Edit tasks.yaml Directly
Edit `research_writer_crew/src/config/tasks.yaml` and replace `{topic}` with your desired topic:
```yaml
description: |
    Research and gather comprehensive information about: Artificial Intelligence
```

## Project Structure

```
learning_crewai/                          # Root directory (shared resources)
├── .env                                  # Shared environment variables
├── venv/                                 # Shared virtual environment
├── .gitignore                            # Shared gitignore
└── research_writer_crew/                 # This project
    ├── README.md
    └── src/
        ├── config/
        │   ├── agents.yaml               # Agent configurations
        │   └── tasks.yaml                # Task configurations
        ├── crew_setup.py                 # CrewAI setup and configuration loader
        └── main.py                       # Main entry point
```

## Configuration

- Edit `src/config/agents.yaml` to customize agents
- Edit `src/config/tasks.yaml` to customize tasks

