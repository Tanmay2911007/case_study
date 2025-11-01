# Case Study 1: How Does a Bike-Share Navigate Speedy Success

## Overview
This case study examines usage data from a bike-share company to identify behavioral patterns, operational inefficiencies, and opportunities for data-driven optimization.  
The project covers the complete analytical workflow — from data ingestion and cleaning to exploratory data analysis (EDA) and visualization.

---

## Objective
To conduct a structured, end-to-end analysis of the Divvy Bike-Share dataset in order to:

- Clean and prepare raw data for reliable analysis  
- Identify patterns in ridership across days, hours, and user types  
- Derive insights that can inform strategic and operational decisions  

---

## Tools and Technologies
| Tool / Library | Function |
|----------------|-----------|
| Python | Core programming environment |
| Pandas | Data manipulation and preprocessing |
| Matplotlib | Visualization of trends and distributions |
| NumPy | Numerical computation |
| OpenPyXL | Reading Excel files |

---

## Data Cleaning Process
The dataset contained several quality issues, including duplicates, null values, and inconsistent column naming.  
A Python script (`data_cleaning.py`) was developed to automate the cleaning process.

### Steps:
1. Imported and inspected the dataset structure, data types, and missing values.  
2. Removed duplicate rows and irrelevant entries.  
3. Handled missing values through deletion or appropriate imputation.  
4. Standardized column names to lowercase with underscores for consistency.  
5. Filtered out invalid entries such as negative or zero trip durations.  
6. Converted date columns to proper datetime format and extracted new variables (`day_of_week`, `hour`).  
7. Exported the cleaned dataset for analysis.

**Output:** `Divvy_Trips_2019_Q1_cleaned.csv`

---

## Exploratory Data Analysis (EDA)
EDA was conducted to quantify user behavior and operational trends.

### Analyses Performed:
- Distribution of trips by day of week  
- Hourly trip volume to identify peak periods  
- Comparison of usage across user types (casual vs. subscriber)  
- Trip duration statistics and outlier detection  
