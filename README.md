# 🛒 E-Commerce Sales Analytics Pipeline (PySpark + PostgreSQL)

This project builds an end-to-end **batch ETL pipeline** for e-commerce sales data using **PySpark** and **PostgreSQL**.  
It processes raw orders, customers, and product datasets and generates analytical aggregations, which are then loaded into PostgreSQL.

---

## 🧠 Overview

The pipeline processes three raw datasets:

- `orders.csv` (order details)
- `customers.json` (customer master)
- `products.json` (product catalog)

It then produces insights such as:

- Total revenue per category  
- Total revenue per customer  
- Top products by revenue  

The results are loaded into PostgreSQL tables created via `schemas.sql`.

---

## 🏗️ Architecture

Raw Data (CSV + JSON)
↓
PySpark Transformations
↓
Aggregations (Category, Customer, Products)
↓
PostgreSQL (agg_category, agg_customer, agg_top_products)


---

## 🧰 Tech Stack

- **PySpark** (Spark SQL + DataFrame API)
- **Python**
- **PostgreSQL**
- **psycopg2 + SQLAlchemy**
- **JSON + CSV data sources**

---

## 📂 Project Structure

ecommerce_sales_pipeline/
│
├── data/
│ └── raw/
│ ├── orders.csv
│ ├── customers.json
│ └── products.json
│
├── scripts/
│ ├── transform_spark.py # PySpark transformations & aggregations
│ ├── load_postgres.py # Loads aggregated results into PostgreSQL
│ └── main.py # Orchestrator: runs transform → load
│
├── config/
│ └── db_config.py # PostgreSQL credentials
│
├── schemas.sql # SQL schema for output tables
│
├── requirements.txt
└── README.md


---

## 🧰 Setup Instructions

```bash
# 1️⃣ Install Dependencies
pip install -r requirements.txt

# 2️⃣ Start PostgreSQL and create required tables
psql -U postgres -d ecommerce_db -f schemas.sql

# 3️⃣ Run PySpark Transformation
python scripts/transform_spark.py

# 4️⃣ Load Aggregations into PostgreSQL
python scripts/load_postgres.py

# 5️⃣ (Optional) Run Full Pipeline (Transform + Load)
python scripts/main.py



🗃️ PostgreSQL Output Tables

1. agg_category
Column	Description
category	Product category name
total_revenue	Total revenue for the category

2. agg_customer
Column	Description
customer_id	Unique customer ID
customer_name	Customer full name
customer_revenue	Total spend by that customer

3. agg_top_products
Column	Description
product_id	Product identifier
product_name	Product name
revenue	Total revenue generated

⚙️ PySpark Transformations Performed

Read CSV + JSON inputs

Clean missing values

Join orders → customers → products

Compute:
total_amount = quantity × price
category-level revenue
customer-level revenue
product-level revenue

Generate 3 aggregated DataFrames:
category insights
customer insights
top product insights

💾 Example Query Results

Top Categories
Electronics | 42000
Fashion     | 18500
Home        | 12900

Top Customers
Neha   | 5400
Ashok  | 4200
Simran | 3100
