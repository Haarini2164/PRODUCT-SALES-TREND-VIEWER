# 📊 PRODUCT SALES TREND VIEWER

## 📌 Project Overview
This project is an interactive **Sales Analytics Dashboard** built using **Streamlit**.  
It allows users to upload sales datasets, analyze trends, and forecast future sales using machine learning.

The goal is to transform raw sales data into **actionable business insights** for better decision-making.

---

## 🎯 Objectives
- Analyze product-wise sales performance
- Identify seasonal trends in sales
- Forecast future sales using predictive models
- Provide insights for inventory and marketing strategies

---

## 📂 Dataset Description

### 🔹 Default Dataset
- File: `sales_data.csv`
- Fields:
  - Date
  - Product
  - Sales
  - Region (optional)
  - Customer Type
  - Quantity Sold

### 🔹 Uploaded Dataset
- File: `retail_sales_dataset.csv`
- Fields:
  - Product Category
  - Quantity
  - Unit Price
  - Total Amount
  - Customer Demographics

---

## ⚙️ Features

### 📊 KPI Dashboard
- Total Sales
- Average Monthly Sales
- Best Sales Month

### 📈 Trend Analysis
- Monthly sales trend visualization
- Detect seasonal patterns

### 🔮 Forecasting
- 6-month sales prediction using Prophet

### 🏆 Top Products
- Top 5 products based on total sales

### 🌍 Region Analysis
- Sales distribution by region (pie chart)

### 📥 Data Export
- Download filtered dataset as CSV

---

## 🧹 Data Processing
- Automatic column mapping
- Handles different column names
- Converts date to datetime format
- Removes invalid or missing values

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- Prophet (Machine Learning)

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run sales_app.py
