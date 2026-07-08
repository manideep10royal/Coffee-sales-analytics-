# Coffee Sales Data Science Analysis

## Project Overview
This project performs comprehensive data science analysis on coffee shop sales data, including exploratory data analysis (EDA), statistical insights, and visualization dashboards.

## Dataset
- **File:** `index (2).csv`
- **Records:** 1,133 transactions
- **Date Range:** March 2024
- **Columns:** date, datetime, cash_type, card, money, coffee_name

## Key Features

### 1. Data Loading & Cleaning
- Automatic CSV loading with proper path handling
- DateTime conversion and feature engineering
- Missing value detection and reporting
- Data type validation

### 2. Exploratory Data Analysis (EDA)
- Dataset overview (shape, types, missing values)
- Descriptive statistics
- Basic data profiling

### 3. Statistical Insights
- **Total Revenue:** $37,508.88
- **Average Transaction:** $33.11
- **Top Products:** Americano with Milk, Latte, Cappuccino
- **Peak Hour:** 10:00 AM
- **Busiest Day:** Tuesday

### 4. Time-Based Analysis
- Hourly sales distribution
- Daily sales trends
- Day-of-week analysis
- Week-of-year breakdown

### 5. Product Analysis
- Coffee type popularity ranking
- Price distribution by product
- Sales volume by beverage

### 6. Visualizations
The script generates a 4-panel dashboard (`coffee_sales_analysis.png`) with:
- **Panel 1:** Top 10 coffee types (horizontal bar chart)
- **Panel 2:** Hourly sales revenue distribution (bar chart)
- **Panel 3:** Daily sales trend (line chart)
- **Panel 4:** Price distribution by coffee type (box plot)

## Output Files
- `coffee_sales_analysis.png` - Dashboard visualization (300 DPI)
- Console output with detailed analysis report

## Requirements
```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

## Installation & Usage

### Setup Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
```

### Install Dependencies
```bash
pip install pandas scikit-learn matplotlib seaborn
```

### Run Analysis
```bash
python coffee_sales.py
```

## Script Output
The script provides:
1. **Console Report** with:
   - Dataset overview and statistics
   - Missing value analysis
   - Top products and peak hours
   - Day-of-week sales breakdown

2. **Visualization Dashboard** saved as PNG file with:
   - Product popularity charts
   - Temporal sales patterns
   - Price analysis

## Data Features Engineered
From the datetime column, the following features are extracted:
- `hour` - Hour of transaction (0-23)
- `day` - Day of month
- `month` - Month number
- `day_of_week` - Day name (Monday-Sunday)
- `week_of_year` - ISO week number

## Project Structure
```
coffee sales/
├── coffee_sales.py              # Main analysis script
├── index (2).csv                # Source dataset
├── coffee_sales_analysis.png    # Generated dashboard
└── README.md                    # This file
```

## Analysis Highlights
- **Most Popular Drink:** Americano with Milk (268 transactions)
- **Most Expensive Range:** Up to $40.00
- **Most Affordable Range:** Starting at $18.12
- **Missing Data:** 89 missing card entries
- **Revenue Distribution:** Fairly consistent across days ($4,969-$6,092)

## Notes
- The script handles relative file paths automatically, so it can be run from any directory
- All monetary values are in the dataset's native currency
- Visualizations are saved at high resolution (300 DPI) for quality output
- The analysis includes robust error handling for file operations

## Author
Unified Mentor Projects - Data Science Pathway

## License
Open source - Educational purposes
