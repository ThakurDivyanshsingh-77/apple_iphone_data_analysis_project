# Apple iPhone Data Analysis Project

## Overview
This is a complete Python data analysis project on Apple iPhone models from **iPhone 1 (2007)** to **iPhone 17**.

The project is structured for final-year academic submission and includes:
- Structured dataset creation using pandas
- Sales, revenue, and profit analysis
- Visualization and interpretation
- Feature impact insights (Face ID, 5G, Dynamic Island, USB-C)
- Strategic recommendations for iPhone 18

## Project Structure

- `apple_iphone_data_analysis.py`: Main analysis script
- `iphone_models_1_to_17.csv`: Generated iPhone dataset
- `outputs/iphone_financial_summary.csv`: Computed financial summary
- `outputs/plots/`: Saved plots

## Dataset Columns
- Model Name
- Launch Year
- Display Size
- Processor
- Camera Specifications
- Battery Capacity
- Special Features
- Launch Price
- Estimated Production Cost
- Units Sold (in millions)

## Financial Formulas
- `Revenue = Units Sold x Launch Price`
- `Profit = (Launch Price - Production Cost) x Units Sold`

> Note: Units are in millions; therefore revenue and profit in the script are reported in USD millions/billions.

## Required Libraries
- pandas
- numpy
- matplotlib
- seaborn

## How To Run

```bash
python apple_iphone_data_analysis.py
```

## Generated Visuals
The script saves the following charts in `outputs/plots/`:
1. Sales trend over years (line chart)
2. Top-selling models (bar chart)
3. Profit comparison by model (bar chart)
4. Correlation heatmap

## Academic Notes
- The script prints clear section-wise insights and interpretations.
- iPhone 16 and iPhone 17 entries are modeled as realistic analytical estimates for continuity.
- Production cost values are estimated for academic analysis.
