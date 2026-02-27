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
