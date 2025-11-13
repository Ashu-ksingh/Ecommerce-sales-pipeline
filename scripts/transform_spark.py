import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Initialize Spark
spark = SparkSession.builder \
    .appName("Ecom Transform Pipeline") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

print("✅ Spark session started:", spark.version)

# Paths
raw_path = "../data/raw"
processed_path = "../data/processed"

# ---- Load Latest Orders CSV ----
order_files = [f for f in os.listdir(raw_path) if f.startswith("orders_") and f.endswith(".csv")]
if not order_files:
    raise FileNotFoundError("❌ No orders CSV found in data/raw/")
latest_orders = sorted(order_files)[-1]
orders_path = os.path.join(raw_path, latest_orders)
print(f"📂 Loading latest orders file: {orders_path}")

# ---- Load Raw Data ----
customers_df = spark.read.json(f"{raw_path}/customers.json")
products_df = spark.read.json(f"{raw_path}/products.json")
orders_df = spark.read.option("header", True).csv(orders_path)

# Convert numeric columns
orders_df = orders_df.withColumn("quantity", col("quantity").cast("int"))

# ---- Join Data ----
joined_df = (
    orders_df
    .join(customers_df, "customer_id", "left")
    .join(products_df, "product_id", "left")
    .withColumnRenamed("name", "customer_name")   # rename from customers
    .withColumnRenamed("name", "product_name")    # rename from products (will fix below)
)

# ⚠️ The above rename overwrites the second name, so do it stepwise:
joined_df = (
    orders_df
    .join(customers_df.withColumnRenamed("name", "customer_name"), "customer_id", "left")
    .join(products_df.withColumnRenamed("name", "product_name"), "product_id", "left")
)

print("🧩 Joined Data:")
joined_df.show(truncate=False)

# ---- Compute Metrics ----
revenue_df = joined_df.withColumn("revenue", col("quantity") * col("price"))

# Revenue per category
agg_category = revenue_df.groupBy("category").agg(_sum("revenue").alias("total_revenue"))

# Revenue per customer
agg_customer = revenue_df.groupBy("customer_id", "customer_name").agg(_sum("revenue").alias("customer_revenue"))

# Top products
agg_products = revenue_df.groupBy("product_id", "product_name").agg(_sum("revenue").alias("revenue")) \
    .orderBy(col("revenue").desc())

# ---- Save Outputs ----
os.makedirs(processed_path, exist_ok=True)

agg_category.write.mode("overwrite").csv(f"{processed_path}/agg_category", header=True)
agg_customer.write.mode("overwrite").csv(f"{processed_path}/agg_customer", header=True)
agg_products.write.mode("overwrite").csv(f"{processed_path}/agg_top_products", header=True)

print("✅ Transformations complete. Processed data saved under /data/processed")

spark.stop()
