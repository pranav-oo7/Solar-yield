cd path/to/solar_yield_project
git init
git add .
git commit -m "Initial commit: solar yield project — notebook, CSVs, report, plots"
git branch -M main
git remote add origin https://github.com/<yourusername>/solar-yield.git
git push -u origin main



# Solar Yield – Energy Audit Project

This project estimates the solar energy yield, cost savings, and CO₂ avoided for a rooftop solar PV system (3 kW example).  
It demonstrates basic data analysis and a short energy-audit style report using Python.

## Project Summary
- **Location:** Mumbai (example)  
- **System size:** 3.0 kW rooftop PV  
- **Annual production:** 4,206 kWh  
- **Estimated CO₂ avoided:** ~3.323 tonnes/year (using 0.79 kgCO₂/kWh)

## What’s included
- `solar_yield_notebook_visuals.ipynb` — Jupyter/Colab notebook (run to regenerate plots & PDF).  
- `solar_yield_script.py` — runnable Python script.  
- `monthly_production.csv`, `hourly_production.csv` — sample output files.  
- `monthly_production.png`, `hourly_production.png`, `savings_by_tariff.png`, `co2_comparison.png` — visuals.  
- `solar_yield_complete_report.pdf` — downloadable short energy-audit report.

## How to run
1. Open the notebook in Google Colab (recommended) or Jupyter.  
2. Update `annual_kwh` (or upload your own CSVs) and run all cells.  
3. Download generated plots and the PDF report.

## Tools & libs
Python, pandas, numpy, matplotlib, fpdf (for report generation).

## Extensions (ideas)
- Add payback/ROI calculation (system cost vs savings)  
- Compare multiple locations or tilt/azimuth sensitivity  
- Package as a Streamlit app for interactive audits

---
