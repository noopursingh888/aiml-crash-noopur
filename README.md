![Python](https://img.shields.io/badge/Python-3-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
# AIML Crash Course - Noopur Singh

# Python Status

## AIML Crash Course - Noopur Singh

This repository contains my Python practice tasks, data analysis assignments, and mini projects completed during the AI/ML Crash Course. The work covers Python fundamentals, Object-Oriented Programming (OOP), file handling, CSV/JSON processing, Pandas, SQL, data visualization, and exploratory data analysis.

---

## Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* CSV Module
* JSON Module
* Object-Oriented Programming (OOP)
* Git & GitHub
* Jupyter Notebook
* Virtual Environment (venv)

---

## Repository Structure

```text
Data/
├── Sample - Superstore.csv
├── customers.csv
├── orders.csv
├── order_items.csv
├── payments.csv
├── products.csv
├── reviews.csv
└── sellers.csv

notebooks/
├── sales_analysis.ipynb
├── maths_for_ml_eda.ipynb
└── ecommerce_eda.ipynb

sql/
├── queries.sql

visuals/
├── bar_chart.png
├── heatmap.png
├── histogram.png
├── task1_derivative.png
├── task2_loss_curve.png
├── task3_histograms.png

reports/

README.md
```

---

# Day 1 – Day 5 Python Practice Tasks

### Python Fundamentals

* Variables and Data Types
* String Manipulation
* Lists, Tuples, Dictionaries, and Sets
* Loops and Conditional Statements
* Functions and Error Handling

### Object-Oriented Programming

* Classes and Objects
* Inheritance
* Polymorphism
* Dunder Methods
* Class Variables

### File Handling

* Reading and Writing Files
* CSV Processing
* JSON Processing
* Data Storage and Retrieval

### Advanced Python

* Type Hints
* List Comprehensions
* Dictionary Comprehensions
* Fraction Class Implementation
* Inventory Management System

---

# Sales Data Analysis Project

## Overview

This project analyzes sales data using Pandas, SQL, and visualization libraries. The objective is to clean data, perform exploratory data analysis (EDA), generate insights, and understand customer and sales behavior.

### Features

* Data Cleaning
* Missing Value Analysis
* Duplicate Detection
* GroupBy Analysis
* Pivot Tables
* Data Visualization
* SQL Queries
* Business Insights

### Tools Used

* Python
* Pandas
* Matplotlib
* Seaborn
* SQLite

---

# Mathematics for Machine Learning & EDA Assignment

## Tasks Completed

### Task 1: Derivative and Slope Intuition

* Implemented a quadratic function
* Calculated derivatives
* Plotted tangent lines
* Visualized slope behavior

### Task 2: Gradient Descent Mini Experiment

* Simulated gradient descent
* Tracked parameter updates
* Visualized loss convergence

### Task 3: Probability Basics

* Generated Uniform Distribution
* Generated Normal Distribution
* Compared distributions using histograms

### Task 4: Exploratory Data Analysis (EDA)

* Dataset Inspection
* Data Cleaning
* Statistical Summary
* Correlation Analysis
* Feature Relationship Analysis
* Data Visualization

---

# E-Commerce Sales Performance Analysis

## Project Objective

Analyze customer, order, product, payment, review, and seller data to identify business trends and generate actionable insights.

## Analysis Performed

### Data Audit

* Dataset Structure Analysis
* Missing Value Detection
* Duplicate Checking
* Data Type Verification

### Data Cleaning

* Missing Value Handling
* Data Standardization
* Data Quality Improvements

### Exploratory Data Analysis

* Revenue Analysis
* Product Performance Analysis
* Customer Behavior Analysis
* Seller Performance Analysis
* Payment Method Analysis
* Review Score Analysis

### Visualizations

* Histograms
* Bar Charts
* Heatmaps
* Correlation Analysis
* Trend Analysis

## Key Findings

1. Revenue is concentrated among a limited number of top-performing products.
2. Customer purchasing behavior differs across product categories.
3. Certain sellers contribute significantly more revenue than others.
4. Review scores provide useful insights into customer satisfaction.
5. Data visualization helps identify trends and patterns that are difficult to observe from raw data.

---

# Learning Outcomes

Through these assignments and projects, I gained hands-on experience in:

* Python Programming
* Problem Solving
* Data Structures
* Object-Oriented Programming
* File Handling
* CSV and JSON Processing
* Pandas Data Analysis
* SQL Query Writing
* Exploratory Data Analysis (EDA)
* Data Visualization
* Business Insight Generation
* Git & GitHub Workflow
* Project Organization

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/noopursingh888/aiml-crash-noopur.git
```

## Move Into Repository

```bash
cd aiml-crash-noopur
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Run Python Files

```bash
python calculator.py
python inventory.py
python pandas_explore.py
```

---
# Linear Regression Practical Tasks

## Overview
This project was completed as part of the AI/ML Internship Program. The objective was to build and evaluate Linear Regression models using the California Housing Dataset and analyze their performance using different evaluation metrics.

## Dataset
California Housing Prices Dataset

Target Variable:
- median_house_value

## Tasks Completed

### Task 1: Baseline Linear Regression Model
- Loaded and preprocessed the dataset.
- Handled missing values.
- Encoded categorical features.
- Split data into training and testing sets.
- Trained a Linear Regression model.
- Generated predictions.
- Evaluated model using:
  - MSE
  - RMSE
  - MAE
  - R² Score
- Created Actual vs Predicted comparison table.
- Visualized Actual vs Predicted values.

### Task 2: One-Feature vs Multi-Feature Models
- Built Model A using a single feature.
- Built Model B using multiple features.
- Compared both models using:
  - MSE
  - RMSE
  - MAE
  - R² Score
- Identified the better-performing model.

### Task 3: Different Train-Test Splits
- Evaluated Linear Regression using:
  - 80/20 split
  - 70/30 split
  - 60/40 split
- Recorded training and testing metrics.
- Compared model stability across different splits.
- Visualized test performance across splits.

### Task 4: Metric Verification and Exploration
- Manually calculated:
  - MSE
  - RMSE
  - MAE
  - R² Score
- Verified results against Scikit-Learn metrics.
- Calculated an additional metric:
  - Explained Variance Score
- Performed an artificial error experiment.
- Analyzed the effect of large prediction errors on evaluation metrics.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Jupyter Notebook

## Results
The multi-feature Linear Regression model outperformed the single-feature model and achieved better predictive performance. Metric verification confirmed the correctness of manually computed evaluation metrics.

# Brazilian E-Commerce Delivery Delay Prediction

## Project Overview

This project analyzes the Brazilian E-Commerce Public Dataset to identify factors affecting delivery delays and predict whether an order will be delivered late using Machine Learning techniques.

---

## Objectives

- Perform Data Audit and Cleaning
- Conduct Exploratory Data Analysis (EDA)
- Perform SQL Analysis using SQLite
- Build a Logistic Regression model
- Build an XGBoost model using Pipeline
- Perform Cross Validation and Hyperparameter Tuning
- Explain predictions using SHAP

---

## Dataset

The following datasets were used:

- olist_orders_dataset.csv
- olist_order_payments_dataset.csv
- olist_customers_dataset.csv
- olist_order_items_dataset.csv
- olist_products_dataset.csv

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- Scikit-learn
- XGBoost
- SHAP
- Jupyter Notebook

---

## Project Structure

```
DAY-3/
│
├── Data/
├── notebooks/
│   ├── 01_Data_Audit_EDA.ipynb
│   ├── 02_SQL_Analysis.ipynb
│   └── 03_ML_Model.ipynb
│
├── sql/
│   ├── ecommerce.db
│   └── sql_queries.sql
│
├── visuals/
├── report/
│   └── Executive_Summary.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Project Workflow

1. Data Loading
2. Data Cleaning
3. Feature Engineering
4. Data Merging
5. Exploratory Data Analysis
6. SQL Analysis
7. Logistic Regression
8. XGBoost Model
9. Cross Validation
10. Hyperparameter Tuning
11. SHAP Explainability

---

## Results

- Successfully analyzed customer order behavior.
- Built Logistic Regression and XGBoost models.
- Compared model performance using multiple evaluation metrics.
- Improved model performance through GridSearchCV.
- Explained predictions using SHAP.

---

## Business Recommendations

- Monitor orders likely to be delayed.
- Improve shipping efficiency in high-delay regions.
- Enhance logistics planning using predictive analytics.
- Notify customers proactively about potential delays.

---

## Future Improvements

- Include seller and review datasets.
- Deploy the model as a web application.
- Automate prediction using real-time data.

---

## Author

Mini Project – Phase 2

Brazilian E-Commerce Delivery Delay Prediction
# Author

**Noopur Singh**