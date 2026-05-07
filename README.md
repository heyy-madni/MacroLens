🌐
Global Economic Health Analyzer
Multi-country economic data pipeline with interactive Streamlit dashboard — powered by World Bank datasets

 Python 3.x
pandas
streamlit
World Bank Data
130+ Countries
About
A data pipeline and analytics tool that ingests annual World Bank datasets across 130+ countries, transforms them from wide to long format, merges them into a unified dataset, and surfaces insights through a terminal interface and an interactive Streamlit dashboard.

Built as an internship-level project to demonstrate end-to-end data engineering — from raw CSV ingestion to cleaned, analysis-ready data and visual output.

Features
Data pipeline
Merges 4 World Bank CSVs, wide → long reshape, missing value handling
130+ countries
Annual data coverage across all major and emerging economies
Streamlit dashboard
Interactive charts, filters, and country comparisons in the browser
Terminal menu
Navigate reports and outputs entirely from the command line
Project architecture
4× CSV files
World Bank
raw datasets
→
data_pipeline.py
Clean, reshape
& merge
→
functions.py
Shared analysis
functions
→
report_generator.py
Chart & output
generation
→
web_presentation.py
Streamlit
dashboard
Terminal users navigate via menu_manager.py instead of the web interface.

File structure
File	Purpose
main.py	Entry point — launches either the Streamlit dashboard or the terminal menu
data_pipeline.py	Loads all 4 CSVs, reshapes wide → long, cleans nulls, merges into a single dataframe
functions.py	Reusable analysis functions shared across modules (filtering, aggregation, metrics)
menu_manager.py	Interactive terminal menu for navigating reports without the web interface
report_generator.py	Generates charts and formatted outputs from processed data
web_presentation.py	Full Streamlit dashboard — run directly via main.py
data/	Raw World Bank CSV files (4 datasets, annual, 130+ countries)
Datasets
All datasets sourced from the World Bank Open Data portal. Downloaded in wide format (countries as rows, years as columns) and reshaped to long format during the pipeline.

DATASET 01
Economic Indicator
Annual data · 130+ countries
DATASET 02
Economic Indicator
Annual data · 130+ countries
DATASET 03
Economic Indicator
Annual data · 130+ countries
DATASET 04
Economic Indicator
Annual data · 130+ countries
 Replace the dataset names above with your actual indicator names (e.g. GDP per capita, Inflation rate, etc.)

Requirements
Python 3.8+
pandas
streamlit
pathlib (standard library)
os (standard library)
# Install dependencies
pip install pandas streamlit
Getting started
Clone the repository and place your World Bank CSV files in the data/ folder.

# 1. Clone the repo
git clone https://github.com/heyy-madni/Global-Economic-Health-Analyzer.git
cd Global-Economic-Health-Analyzer

# 2. Install dependencies
pip install pandas streamlit

# 3. Run the project
python main.py
Running python main.py automatically launches the Streamlit dashboard in your browser. No separate terminal command needed.
Terminal mode
Prefer working in the terminal? The menu manager lets you navigate all reports and outputs without opening the browser.

# Launch terminal interface instead
python menu_manager.py
