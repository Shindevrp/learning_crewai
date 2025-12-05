# CrewAI Learning Projects

This directory contains multiple CrewAI projects sharing common resources.

## Shared Resources

The following resources are shared across all projects in this directory:

- **`.env`** - Environment variables (API keys, etc.) shared by all projects
- **`venv/`** - Python virtual environment with common dependencies
- **`.gitignore`** - Common gitignore rules

## Projects

### research_writer_crew

A research and writing crew that uses YAML configuration files for agents and tasks. This project can research any topic and produce well-written articles.

**Location:** `research_writer_crew/`

See the project's README for setup and usage instructions.

## Setup

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Set up environment variables:**
   Create a `.env` file in this root directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Adding New Projects

To add a new CrewAI project:

1. Create a new folder in this directory (e.g., `my_new_project/`)
2. The new project can use the shared `.env` and `venv` resources
3. Update this README to list your new project

