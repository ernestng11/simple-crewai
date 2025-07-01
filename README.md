# Simple CrewAI

A simple CrewAI project using Poetry for dependency management.

## Installation

```bash
poetry install
```

## Usage

```bash
poetry env actiavte
poetry run bd_crew
```

## Configuration Files

### agents.yaml
Defines the three role-based agents in the BD crew:

- **Market Researcher**: Conducts comprehensive market research by gathering competitor data, industry news, and market intelligence from various online sources. Specializes in competitor analysis, market trends, and industry dynamics to support strategic decision-making.

- **Data Analyst**: Analyzes market data and creates financial models including TAM (Total Addressable Market), growth projections, and ROI scenarios using advanced analytical tools and code execution capabilities.

- **Strategy Validator**: Cross-checks assumptions, validates strategy coherence, and scores clarity and feasibility on a scale of 0-1. Ensures all recommendations meet quality standards with scores above 0.8 and provides gap analysis with actionable recommendations.

### tasks.yaml
Defines the sequential workflow tasks executed by the agents:

- **market_research_task**: Gathers competitor data, industry news, market trends, and business intelligence using web scraping and search tools. Focuses on identifying market opportunities and competitive landscape analysis.

- **data_analysis_task**: Builds financial models and calculates business metrics including TAM calculations, growth projections, ROI scenarios, and key performance indicators using the market research data as context.

- **strategy_validation_task**: Validates findings from both previous tasks, evaluates strategy coherence, assigns clarity scores, identifies gaps, and provides recommendations. Ensures final approval only when quality scores meet the 0.8 threshold. 