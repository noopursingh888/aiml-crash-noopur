# Executive Summary

## Project Objective
The objective of this project is to analyze the Brazilian E-Commerce Public Dataset and predict whether an order will be delivered late using Machine Learning techniques.

## Dataset Used
- Orders Dataset
- Customers Dataset
- Order Payments Dataset
- Order Items Dataset
- Products Dataset

## Data Preparation
- Loaded and inspected all datasets.
- Cleaned missing values and duplicate records.
- Converted date columns into datetime format.
- Created new features such as delivery_time_days, shipping_time_days, estimated_delay_days, order_month, and order_weekday.
- Merged all datasets into a single dataframe.

## Exploratory Data Analysis
- Analyzed delivery time distribution.
- Compared payment methods.
- Studied monthly order trends.
- Identified delayed and non-delayed orders.
- Performed correlation analysis.
- Analyzed delivery delays across customer states.

## SQL Analysis
- Loaded the cleaned dataset into SQLite.
- Executed SQL queries using SELECT, WHERE, GROUP BY, ORDER BY, JOIN, aggregate functions, and subqueries.
- Verified insights obtained during EDA.

## Machine Learning Models
- Built a Logistic Regression baseline model.
- Developed an XGBoost model using Pipeline and ColumnTransformer.
- Performed Stratified K-Fold Cross Validation.
- Tuned the XGBoost model using GridSearchCV.

## Model Explainability
- Generated SHAP summary plots.
- Identified important features affecting predictions.
- Explained individual predictions using SHAP waterfall plots.

## Business Recommendations
- Monitor orders with high predicted delay risk.
- Improve shipping processes in regions with frequent delays.
- Optimize logistics to reduce delivery time.
- Use predictive models for proactive customer communication.

## Conclusion
This project demonstrates a complete end-to-end data analytics and machine learning workflow, including data preprocessing, SQL analysis, visualization, predictive modeling, model evaluation, and explainability to support business decision-making.