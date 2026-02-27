# 📊 PRODUCT SALES TREND VIEWER

---

## 📌 Project Overview
An interactive **Sales Analytics Dashboard** built using **Streamlit** to analyze product sales, visualize trends, and forecast future performance using machine learning.

This application transforms raw sales data into **actionable business insights** for better decision-making.

---

## 🎯 Objectives
- Analyze product-wise sales performance  
- Identify monthly and seasonal sales trends  
- Forecast future sales using predictive models  
- Support business decisions using data insights  

---

## 📂 Dataset Description

### 🔹 Default Dataset
- File: `sales_data.csv`
- Contains:
  - Date  
  - Product  
  - Sales  
  - Region  
  - Customer Type  
  - Quantity Sold  

### 🔹 Retail Dataset
- File: `retail_sales_dataset.csv`
- Contains:
  - Product Category  
  - Quantity  
  - Unit Price  
  - Total Amount  

---

## ⚙️ Features

- 📊 KPI Dashboard (Total Sales, Avg Monthly Sales, Best Month)  
- 📈 Monthly Sales Trend Visualization  
- 🔮 6-Month Forecast using Prophet  
- 🏆 Top 5 Products Analysis  
- 🌍 Region-wise Sales Distribution  
- 📥 Download Filtered Data as CSV  

---
## 📸 Project Output

### 🖥️ Dashboard Overview
<p align="center">
  <img src="1.png" width="900"/>
</p>

---

### 📈 Sales Trend & Forecast
<p align="center">
  <img src="2.png" width="900"/>
</p>

---

### 🏆 Top Products
<p align="center">
  <img src="3.png" width="900"/>
</p>

---

### 🌍 Region-wise Sales
<p align="center">
  <img src="4.png" width="900"/>
</p>

---

### 📋 Filtered Data Table
<p align="center">
  <img src="5.png" width="900"/>
</p>

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit  
- Pandas  
- Plotly  
- Prophet  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run sales_app.py
