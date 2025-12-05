# Cricket Performance Analysis - CrewAI Project

A CrewAI project that analyzes cricket player performance using YAML configuration files for agents and tasks. This project creates a crew of specialized agents that research, analyze, and generate detailed performance reports and visualizations for cricketers.

## Setup

1. **Activate the virtual environment:**
   ```bash
   # From the learning_crewai root directory
   source venv/bin/activate
   ```

2. **Set up environment variables:**
   Create a `.env` file in the `learning_crewai` root directory with your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

### About SERPER_API_KEY

**What is SERPER_API_KEY?**
- Serper is a search engine API that provides real-time internet search results
- It allows the Stats Fetcher agent to search the web for cricket statistics and player data
- The API returns structured data about cricket matches, player statistics, and performance metrics

**What does it do in this project?**
- **Stats Fetcher Agent**: Uses SERPER_API_KEY to search the internet for {cricketer_name}'s cricket statistics
- **Data Retrieval**: Fetches real-time match records, scores, averages, and performance data
- **Multiple Sources**: Searches and verifies data from multiple reliable cricket databases
- **Accuracy**: Ensures accurate and up-to-date cricket performance information

**How to Get SERPER_API_KEY?**

1. **Visit Serper Website:**
   - Go to https://serper.dev/
   - Click "Sign Up" or "Get Started"

2. **Create Account:**
   - Sign up with your email address
   - Verify your email
   - Create a free account

3. **Get Your API Key:**
   - Log in to your Serper dashboard
   - Navigate to "API Key" section
   - Copy your free API key (includes 100 free searches/month)

4. **Add to .env File:**
   ```bash
   SERPER_API_KEY=your_copied_serper_api_key
   ```

5. **Pricing:**
   - Free tier: 100 searches/month
   - Paid plans: Starting at $5/month for 10,000 searches
   - Perfect for this cricket analysis project

3. **Run the project:**
   ```bash
   cd cricketer_performance_analysis/src
   python main.py
   ```

## Changing the Cricketer and Year

You can analyze different cricketers in 3 different ways:

### Method 1: Command Line Arguments (Recommended)
Pass the cricketer name and year as arguments:
```bash
cd cricketer_performance_analysis/src
python main.py "Virat Kohli" "2023"
python main.py "Babar Azam" "2022"
python main.py "Steve Smith" "2021"
```

### Method 2: Environment Variables
Set the cricketer name and year in your `.env` file:
```bash
CRICKETER_NAME=Sachin Tendulkar
YEAR=2012
```

Then run normally:
```bash
cd cricketer_performance_analysis/src
python main.py
```

### Method 3: Default Values
If no values are specified, the project defaults to analyzing Virat Kohli for the year 2023.

## Project Structure

```
cricketer_performance_analysis/
├── src/
│   ├── __init__.py
│   ├── main.py           # Main entry point
│   ├── crew.py           # Crew configuration and agents
│   └── config/
│       ├── agents.yaml   # Agent definitions
│       └── tasks.yaml    # Task definitions
└── README.md
```

## Agents

- **Stats Fetcher**: Gathers comprehensive cricket statistics from various sources using the Serper API
- **Stats Calculator**: Analyzes and calculates performance metrics like averages, strike rates, and consistency
- **Graph Creator**: Creates visual representations (graphs and charts) of performance data using Python

## How It Works

1. The crew reads agent and task configurations from YAML files in `src/config/`
2. The Stats Fetcher collects cricketer statistics for the specified year
3. The Stats Calculator computes performance metrics and analyzes trends
4. The Graph Creator generates visual graphs and performance summaries
5. Output files are generated with statistics and performance visualizations

## Output Files

- `stats_for_cricketer.txt` - Detailed statistical analysis and averages
- `performance_graph.png` - Visual representation of performance metrics

