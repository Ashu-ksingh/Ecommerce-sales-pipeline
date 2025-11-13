# 🛒 E-Commerce Sales Analytics Pipeline

This project demonstrates an end-to-end **batch ETL and analytics pipeline** for e-commerce sales data using **Python, Pandas, and SQL**.  
It processes raw order, customer, and product datasets and produces curated analytical outputs useful for business decisions.

---

## 🏗️ Architecture

Raw CSV/Excel Data
↓
Python ETL (Extract → Transform → Load)
↓
SQLite / SQL Database
↓
Analytics & Reports

yaml
Copy code

---

## 🧰 Tech Stack

- **Python**
- **Pandas**
- **SQLite (or PostgreSQL)**  
- **SQL Queries**
- **Jupyter / Scripts for ETL**

---

## 📂 Project Structure

ecommerce_sales_pipeline/
│
├── data/
│ ├── customers.csv
│ ├── products.csv
│ ├── orders.csv
│
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── main.py
│
├── analytics/
│ ├── sales_by_category.sql
│ ├── top_customers.sql
│ ├── revenue_by_month.sql
│
├── output/
│ ├── final_sales_report.csv
│ ├── enriched_orders.csv
│
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🧰 Setup Instructions

```bash
## 1️⃣ Install dependencies
pip install -r requirements.txt

## 2️⃣ Run complete ETL pipeline
python scripts/main.py

## 3️⃣ View final analytics output
open output/final_sales_report.csv
⚙️ Features & Processing Steps
✔ Extract
Loads CSV datasets: orders, customers, products

✔ Transform
Cleans missing values

Adds calculated fields:

total_amount

profit margins

category-level metrics

Joins customers + orders + products

Performs business-level aggregations:

total revenue

top-selling categories

top customers

monthly revenue growth

✔ Load
Loads curated tables into SQLite database

Stores reports in CSV format inside /output folder

## 📊 Sample Output

customer_id	name	total_spent
101	Neha	5400
103	Ashok	4200
105	Simran	3100

Sales by Category
category	revenue
Electronics	42,000
Fashion	18,500
Home	12,900
