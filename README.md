# 🌐 MacroLens

> Multi-country economic data pipeline with an interactive Streamlit dashboard — powered by World Bank datasets.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.0+-150458?style=flat-square&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![World Bank](https://img.shields.io/badge/Data-World%20Bank-009FDA?style=flat-square)
![Countries](https://img.shields.io/badge/Coverage-130%2B%20Countries-2E8B57?style=flat-square)

---

## About

**MacroLens** is a data pipeline and analytics tool that ingests annual World Bank datasets across 130+ countries, transforms them from wide to long format, merges them into a unified dataset, and surfaces insights through a terminal interface and an interactive Streamlit dashboard.

Built as an internship-level project to demonstrate end-to-end data engineering — from raw CSV ingestion to cleaned, analysis-ready data and visual output.

---

## Features

- **Data pipeline** — Merges 4 World Bank CSVs, reshapes wide → long, handles missing values
- **130+ countries** — Annual coverage across all major and emerging economies
- **Streamlit dashboard** — Interactive charts, filters, and country comparisons in the browser
- **Terminal menu** — Navigate reports and outputs entirely from the command line

---

## Project Architecture

```
4× CSV files (World Bank)
        │
        ▼
data_pipeline.py     ← Clean, reshape & merge
        │
        ▼
functions.py         ← Shared analysis functions
        │
        ▼
report_generator.py  ← Chart & output generation
        │
       / \
      ▼   ▼
web_presentation.py  menu_manager.py
(Streamlit dashboard) (Terminal interface)
```

---

## File Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — launches the Streamlit dashboard automatically |
| `data_pipeline.py` | Loads all 4 CSVs, reshapes wide → long, cleans nulls, merges into a single dataframe |
| `functions.py` | Reusable analysis functions shared across modules (filtering, aggregation, metrics) |
| `menu_manager.py` | Interactive terminal menu for navigating reports without the browser |
| `report_generator.py` | Generates charts and formatted outputs from processed data |
| `web_presentation.py` | Full Streamlit dashboard UI |
| `data/` | Raw World Bank CSV files (4 datasets, annual, 130+ countries) |

---

## Datasets

All datasets are sourced from the [World Bank Open Data](https://data.worldbank.org) portal. Downloaded in wide format (years as columns) and reshaped to long format during the pipeline.

| # | Indicator | Source |
|---|---|---|
| 1 | *GDP growth* | World Bank |
| 2 | *inflation* | World Bank |
| 3 | *Unemployment* | World Bank |
| 4 | *income per capita* | World Bank |

---

## Requirements

- Python 3.8+
- pandas
- streamlit
- pathlib *(standard library)*
- os *(standard library)*

Install dependencies:

```bash
pip install pandas streamlit
```

---

## Getting Started

Clone the repository and place your World Bank CSV files in the `data/` folder.

```bash
# 1. Clone the repo
git clone https://github.com/heyy-madni/MacroLens.git
cd MacroLens

# 2. Install dependencies
pip install pandas streamlit

# 3. Run the project
python main.py
```

Running `python main.py` will automatically launch the Streamlit dashboard in your browser — no separate terminal command needed.

---

## Terminal Mode

Prefer the command line? The menu manager lets you navigate all reports and outputs without opening the browser.

```bash
python menu_manager.py
```

---

## main.py — Streamlit Auto-Launch

```python
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    file = Path(__file__).parent / "web_presentation.py"
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(file)])
```

---

*Data sourced from the [World Bank Open Data](https://data.worldbank.org) portal · Built with Python & Streamlit · Internship project by [heyy-madni](https://github.com/heyy-madni)*
