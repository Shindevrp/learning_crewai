# Research Writer Crew - CrewAI Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/powered%20by-crewai-orange)](https://crewai.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-production--ready-brightgreen)](README.md)

> An advanced automated research and content creation system using multi-agent AI for comprehensive topic research, analysis, and professional article generation.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output](#output)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Overview

Research Writer Crew is an intelligent multi-agent system designed to automate the research and content creation process. It leverages CrewAI to orchestrate specialized agents that work collaboratively to:

- **Research** topics comprehensively using web search
- **Analyze** information from multiple sources
- **Organize** findings into logical structures
- **Write** professional, well-structured articles
- **Review** content for quality and accuracy

### Use Cases
- Academic research papers
- Blog posts and articles
- Technical documentation
- Market research reports
- News articles and features
- SEO-optimized content
- Competitive analysis

## Features

- **Multi-Agent Architecture**: Research, analyst, writer, and editor agents
- **Web-Based Research**: Real-time information gathering via Serper API
- **Automated Outline Generation**: Structured content planning
- **Professional Writing**: Grammar-correct, engaging content
- **Citation Management**: Source tracking and references
- **SEO Optimization**: Keyword-focused content creation
- **Format Flexibility**: Support for multiple article styles
- **Quality Control**: Multi-stage review and editing
- **YAML Configuration**: Easy customization of agents and workflows

## Architecture

```
┌──────────────────────────────────────────────────────┐
│        Research Writer Crew System                   │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌────────────────────────────────────────────┐    │
│  │      User Input: Topic or Keywords          │    │
│  └────────────────────┬───────────────────────┘    │
│                       │                             │
│     ┌─────────────────┴──────────────────┐         │
│     │                                    │         │
│  ┌──▼──────────────┐          ┌─────────▼──┐     │
│  │ Researcher      │          │ Analyzer   │     │
│  │ Agent           │          │ Agent      │     │
│  │                 │          │            │     │
│  │ Web Research    │          │ Analysis & │     │
│  │ Data Gathering  │          │ Synthesis  │     │
│  └──┬──────────────┘          └────┬───────┘     │
│     │                             │               │
│  ┌──▼──────────────┐    ┌────────▼──┐            │
│  │ Outline Creator│    │ Writer     │            │
│  │ Agent          │    │ Agent      │            │
│  │                │    │            │            │
│  │ Structure &    │    │ Content    │            │
│  │ Plan           │    │ Generation │            │
│  └──┬─────────────┘    └────┬──────┘            │
│     │                        │                   │
│     └────────────┬───────────┘                   │
│                  │                               │
│          ┌───────▼────────┐                     │
│          │ Editor Agent   │                     │
│          │                │                     │
│          │ Review &       │                     │
│          │ Polish         │                     │
│          └───────┬────────┘                     │
│                  │                               │
│          ┌───────▼────────┐                     │
│          │  Output        │                     │
│          │  Article       │                     │
│          │  + Metadata    │                     │
│          └────────────────┘                     │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Prerequisites

### System Requirements
- **OS**: macOS, Linux, or Windows
- **Python**: 3.10, 3.11, 3.12, or 3.13
- **Memory**: Minimum 2GB RAM
- **Disk Space**: 1GB for dependencies

### Required API Keys
- **OpenAI API Key**: For AI research and writing (https://platform.openai.com/api-keys)
- **Serper API Key**: For web research (https://serper.dev)

### Dependencies
- crewai[tools]>=0.86.0
- python-dotenv>=1.0.0
- requests (for API calls)

## Installation

### 1. Navigate to Project Directory

```bash
cd /Users/shinde/Desktop/Talbot/learning_crewai/research_writer_crew
```

### 2. Configure Environment Variables

Ensure `.env` file exists in the workspace root:
```bash
# File: /Users/shinde/Desktop/Talbot/learning_crewai/.env
OPENAI_API_KEY=sk-your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### 3. Verify Environment

```bash
# Check Python version
python3 --version  # Should be 3.10 or higher

# Activate shared virtual environment
source /Users/shinde/Desktop/Talbot/learning_crewai/venv/bin/activate

# Verify CrewAI
python3 -c "import crewai; print(crewai.__version__)"
```

## Configuration

### API Keys Setup

#### OpenAI API Key
1. Visit https://platform.openai.com/api-keys
2. Create a new API key
3. Copy to `.env`: `OPENAI_API_KEY=sk-...`

#### Serper API Key
1. Visit https://serper.dev
2. Sign up for free account
3. Get API key from dashboard
4. Copy to `.env`: `SERPER_API_KEY=...`
5. Free tier: 100 searches/month

### Project Configuration

Edit `src/config/agents.yaml` to customize agent behavior:

```yaml
researcher:
  role: "Senior Research Analyst"
  goal: "Find the most relevant and accurate information"
  backstory: "Expert researcher with access to latest sources..."

writer:
  role: "Professional Content Writer"
  goal: "Create well-structured articles"
  backstory: "Experienced writer with editorial expertise..."
```

## Usage

### Method 1: Command Line (Recommended)

```bash
cd /Users/shinde/Desktop/Talbot/learning_crewai/research_writer_crew/src
python main.py "Artificial Intelligence in Healthcare"
```

### Method 2: With Environment Variables

```bash
# Set topic in .env
export RESEARCH_TOPIC="Quantum Computing Applications"

# Run without arguments
cd src
python main.py
```

### Method 3: Interactive Mode

```bash
cd src
python main.py
# You will be prompted to enter a topic
```

### Example Topics

```bash
# Technology & AI
python main.py "AI in Healthcare"
python main.py "Quantum Computing Applications"
python main.py "Blockchain Technology"

# Business & Economics
python main.py "Digital Transformation Strategies"
python main.py "Sustainable Business Models"

# Science & Nature
python main.py "Climate Change Solutions"
python main.py "Renewable Energy"

# Society & Culture
python main.py "Remote Work Evolution"
python main.py "Mental Health Awareness"
```

## Output

### Generated Files

| File | Description |
|------|-------------|
| `research_output.md` | Generated article in Markdown format |
| `research_report.txt` | Detailed research findings |
| `sources.txt` | List of sources and citations |
| `article.pdf` | Formatted PDF article (if conversion enabled) |

### Output Example

**research_output.md**:
```markdown
# Artificial Intelligence in Healthcare

## Executive Summary
AI is transforming healthcare through diagnostic accuracy, 
personalized treatment, and operational efficiency...

## Introduction
Healthcare professionals are increasingly leveraging AI
to improve patient outcomes and reduce costs...

## Key Applications
### 1. Diagnostic Imaging
- Image recognition for disease detection
- Accuracy rates exceeding 95% in some areas

### 2. Predictive Analytics
- Patient risk stratification
- Early disease detection

## Challenges & Opportunities
...

## Conclusion
...

## Sources
[1] https://example.com/ai-healthcare
[2] https://example.com/medical-ai
...
```

## Project Structure

```
research_writer_crew/
├── src/
│   ├── __init__.py
│   ├── main.py                    # Entry point with CLI handling
│   ├── crew_setup.py              # Crew initialization
│   ├── config/
│   │   ├── agents.yaml            # Agent definitions
│   │   ├── tasks.yaml             # Task configurations
│   │   └── __init__.py
│   └── tools/
│       └── custom_tools.py        # Custom tools & utilities
│
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
├── requirements.txt               # Project dependencies
│
└── Output Files (Generated):
    ├── research_output.md
    ├── research_report.txt
    ├── sources.txt
    └── article.pdf
```

## Agents

### 1. Researcher Agent
**Role**: Senior Research Analyst
- Conducts comprehensive topic research
- Searches for current and historical information
- Verifies source credibility
- Gathers data from multiple sources

### 2. Analyzer Agent
**Role**: Research Analyst & Data Specialist
- Analyzes research findings
- Identifies key themes and insights
- Synthesizes information
- Creates knowledge summaries

### 3. Outline Creator Agent
**Role**: Content Strategist
- Creates article outlines
- Plans content structure
- Organizes information logically
- Prioritizes key points

### 4. Writer Agent
**Role**: Professional Content Writer
- Writes engaging articles
- Maintains consistent tone
- Incorporates SEO best practices
- Creates well-formatted content

### 5. Editor Agent
**Role**: Editorial Manager
- Reviews written content
- Checks for accuracy
- Improves clarity and flow
- Ensures quality standards

## Customization

### Modifying Agent Behavior

Edit `src/config/agents.yaml`:

```yaml
researcher:
  role: "Custom Research Role"
  goal: "Custom research goal"
  backstory: "Custom backstory with specific expertise"
  tools:
    - serper_search_tool
    - web_scraper_tool
```

### Adding Research Sources

Modify `src/tools/custom_tools.py` to integrate additional data sources:

```python
class CustomSourceTool:
    def search(self, query):
        # Implement custom search logic
        pass
```

### Customizing Output Format

Edit task definitions in `src/config/tasks.yaml` to change output format:

```yaml
write_article_task:
  description: "Write custom formatted article"
  expected_output: "Article in your preferred format"
```

## Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'crewai'"
```bash
source /Users/shinde/Desktop/Talbot/learning_crewai/venv/bin/activate
pip install crewai[tools]
```

#### "API Key not found"
```bash
# Verify .env file
cat /Users/shinde/Desktop/Talbot/learning_crewai/.env

# Set manually if needed
export OPENAI_API_KEY=sk-your_key
export SERPER_API_KEY=your_key
```

#### "Serper quota exceeded"
```bash
# Check usage at https://serper.dev/dashboard
# Upgrade plan for more searches
```

#### "No output files generated"
- Check logs for agent execution errors
- Verify all API keys are set
- Ensure topic is specific enough

### Debug Mode

```bash
export LOG_LEVEL=DEBUG
cd src
python main.py "Topic"
```

## Performance Metrics

### Typical Execution Times
- Simple topic: 5-15 minutes
- Complex research: 15-30 minutes
- Full article generation: 20-40 minutes

### API Usage
- Research queries: 10-20 searches per article
- Token usage: Varies by article length (500-2000 words)

## Best Practices

### For Better Results
1. Use specific, well-defined topics
2. Provide context or requirements
3. Allow sufficient time for research
4. Review and edit generated content
5. Verify all citations and sources

### Quality Tips
- Break complex topics into subtopics
- Request specific article formats
- Include keywords for SEO optimization
- Review for accuracy and bias

## Contributing

### Development Setup

```bash
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "feat: description"
git push origin feature/new-feature
```

### Code Standards
- Follow PEP 8
- Add type hints
- Write docstrings
- Include error handling
- Test with various topics

## Support & Resources

- **CrewAI Docs**: https://docs.crewai.com/
- **OpenAI API**: https://platform.openai.com/docs/
- **Serper API**: https://serper.dev/docs
- **Writing Best Practices**: https://www.grammarly.com/

## Security

- Never hardcode API keys
- Use `.env` for sensitive data
- Monitor API usage for abuse
- Keep dependencies updated

## Version History

| Version | Date | Status |
|---------|------|--------|
| 1.0.0 | Dec 6, 2025 | Production Ready |
| 0.9.0 | Dec 5, 2025 | Beta |

---

**Last Updated**: December 6, 2025
**Status**: Production Ready 
**Maintained By**: Learning CrewAI Team

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

