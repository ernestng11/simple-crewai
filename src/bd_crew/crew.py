from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, CodeInterpreterTool
from pydantic import BaseModel, Field

class MarketResearchReport(BaseModel):
	"""Market research report model"""
	competitor_analysis: List[str] = Field(..., description="List of key competitors and their analysis")
	market_size_estimates: str = Field(..., description="Market size estimates and data")
	industry_trends: List[str] = Field(..., description="List of key industry trends")
	strategic_opportunities: List[str] = Field(..., description="List of identified strategic opportunities")

class DataAnalysisReport(BaseModel):
	"""Data analysis report model"""
	tam_calculation: str = Field(..., description="Total Addressable Market calculation and methodology")
	growth_projections: List[str] = Field(..., description="List of growth projection scenarios")
	roi_scenarios: List[str] = Field(..., description="List of ROI scenarios and calculations")
	key_metrics: List[str] = Field(..., description="List of key performance indicators and metrics")

class StrategyValidationReport(BaseModel):
	"""Strategy validation report model"""
	clarity_score: float = Field(..., description="Clarity score on a scale of 0-1")
	assumption_verification: List[str] = Field(..., description="List of verified or challenged assumptions")
	gap_analysis: List[str] = Field(..., description="List of identified gaps or issues")
	recommendations: List[str] = Field(..., description="List of recommendations for improvement")
	final_approval: bool = Field(..., description="Whether the strategy is approved (score >= 0.8)")

@CrewBase
class BdCrew():
	"""BD Crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True,
			memory=False,
		)

	@agent
	def data_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['data_analyst'],
			tools=[CodeInterpreterTool()],
			verbose=True,
			memory=False,
		)

	@agent
	def strategy_validator(self) -> Agent:
		return Agent(
			config=self.agents_config['strategy_validator'],
			tools=[SerperDevTool()],
			verbose=True,
			memory=False,
		)

	@task
	def market_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_research_task'],
			agent=self.market_researcher(),
			output_json=MarketResearchReport
		)

	@task
	def data_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_analysis_task'],
			agent=self.data_analyst(),
			context=[self.market_research_task()],
			output_json=DataAnalysisReport
		)

	@task
	def strategy_validation_task(self) -> Task:
		return Task(
			config=self.tasks_config['strategy_validation_task'],
			agent=self.strategy_validator(),
			context=[self.market_research_task(), self.data_analysis_task()],
			output_json=StrategyValidationReport
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BD crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
