# 📊 PRODUCT SALES TREND VIEWER

## 📌 Project Overview
This project is an interactive **Sales Analytics Dashboard** built using **Streamlit**.  
It enables users to upload sales datasets, analyze trends, and forecast future sales using machine learning.

The application helps convert raw sales data into **meaningful business insights** for better decision-making.

---

## 🎯 Objectives
- Analyze product-wise sales performance  
- Identify monthly and seasonal sales trends  
- Forecast future sales using predictive models  
- Support business decisions with data insights  

---

## 📂 Dataset Description

### 🔹 Default Dataset
- File: `sales_data.csv`
- Contains:
  - Date  
  - Product  
  - Sales  
  - Region (optional)  
  - Customer Type  
  - Quantity Sold  

### 🔹 Uploaded Dataset
- File: `retail_sales_dataset.csv`
- Contains:
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
- 6-month sales prediction using **Prophet**  

### 🏆 Top Products
- Top 5 products based on total sales  

### 🌍 Region Analysis
- Region-wise sales distribution (Pie Chart)  

### 📥 Data Export
- Download filtered dataset as CSV  

---

## 🧹 Data Processing
- Automatic column mapping  
- Handles different column naming formats  
- Converts date columns to datetime  
- Removes invalid and missing values  

---

## 🛠️ Tech Stack
- Python 🐍  
- Streamlit  
- Pandas  
- Plotly  
- Prophet (Machine Learning)  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run sales_app.py
