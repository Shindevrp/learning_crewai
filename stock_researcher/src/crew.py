from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
import os


# Initialize SerperDevTool for search capabilities
search_tool = SerperDevTool()

# Note: To add matplotlib support, run: pip install matplotlib seaborn
# Matplotlib is used for data visualization and graph generation


@CrewBase
class StockResearchCrew():
	"""Stock Research and S&P 500 Benchmark Analysis Crew
	
	This crew coordinates multiple agents for comprehensive stock analysis:
	- Research stock fundamentals and S&P 500 benchmarks
	- Compare and visualize performance metrics
	- Generate investment suggestions with appropriate disclaimers
	"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	
	# Track execution progress
	step_counter = 0
	task_counter = 0

	def step_callback(self):
		"""Called after each step (action/tool call) in agent execution.
		Useful for progress tracking and logging intermediate actions."""
		self.step_counter += 1
		print(f"\n[STEP {self.step_counter}] Agent action completed")

	def task_callback(self, task_output):
		"""Called after each task completes.
		Useful for tracking task completion and logging final outputs."""
		self.task_counter += 1
		print(f"[TASK {self.task_counter}] Task completed successfully")

	@agent
	def project_coordinator(self) -> Agent:
		"""Coordinates overall workflow and task dependencies"""
		return Agent(
			config=self.agents_config['project_coordinator'],
			verbose=True
		)

	@agent
	def stock_researcher(self) -> Agent:
		"""Researches detailed stock data using search capabilities"""
		return Agent(
			config=self.agents_config['stock_researcher'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def sp_benchmark_analyst(self) -> Agent:
		"""Analyzes S&P 500 benchmark data"""
		return Agent(
			config=self.agents_config['sp_benchmark_analyst'],
			verbose=True,
			tools=[search_tool]
		)

	@agent
	def data_processor(self) -> Agent:
		"""Structures and organizes raw data for analysis"""
		return Agent(
			config=self.agents_config['data_processor'],
			verbose=True
		)

	@agent
	def financial_data_analyst(self) -> Agent:
		"""Generates visualizations and comparative analysis"""
		return Agent(
			config=self.agents_config['financial_data_analyst'],
			verbose=True
		)

	@agent
	def investment_advisor(self) -> Agent:
		"""Provides AI-generated investment suggestions with disclaimers"""
		return Agent(
			config=self.agents_config['investment_advisor'],
			verbose=True
		)

	@task
	def stock_research_task(self) -> Task:
		"""Research task for gathering stock data"""
		return Task(
			config=self.tasks_config['stock_research_task'],
			tools=[search_tool]
		)

	@task
	def sp_benchmark_task(self) -> Task:
		"""Research task for S&P 500 benchmark data"""
		return Task(
			config=self.tasks_config['sp_benchmark_task'],
			tools=[search_tool]
		)

	@task
	def data_preparation_task(self) -> Task:
		"""Data preparation task with dependencies on research tasks"""
		return Task(
			config=self.tasks_config['data_preparation_task'],
			context=[self.stock_research_task(), self.sp_benchmark_task()],
			output_file='stock_sp500_data.txt'
		)

	@task
	def comparison_and_visualization_task(self) -> Task:
		"""Visualization task with dependency on data preparation"""
		return Task(
			config=self.tasks_config['comparison_and_visualization_task'],
			context=[self.data_preparation_task()],
			output_file='stock_analysis_summary.txt'
		)

	@task
	def investment_suggestion_task(self) -> Task:
		"""Investment suggestion task with full analysis context"""
		return Task(
			config=self.tasks_config['investment_suggestion_task'],
			context=[self.comparison_and_visualization_task()],
			output_file='investment_suggestion_report.txt'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates and configures the Stock Research Crew
		
		Configuration includes:
		- Sequential task processing for logical workflow
		- Step and task callbacks for progress tracking
		- Project coordinator for workflow management
		- Comprehensive logging for debugging and monitoring
		"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			full_output=True,
			manager_agent=self.project_coordinator(),
			output_log_file='stock_analysis_logs.txt'
		)
