import subprocess
import time
import os

print("\n🚀 Starting E-Commerce Sales Analytics Pipeline...\n")

# Step 1: Run Spark Transformation
print("📦 Running PySpark Transformation...")
transform = subprocess.Popen(
    ["python", "scripts/transform_spark.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

# Print transform logs
for line in transform.stdout:
    print(line, end="")

transform.wait()

print("\n✅ Transformation complete!")

time.sleep(2)

# Step 2: Load into PostgreSQL
print("\n📥 Loading transformed data into PostgreSQL...")
load = subprocess.Popen(
    ["python", "scripts/load_postgres.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

# Print load logs
for line in load.stdout:
    print(line, end="")

load.wait()

print("\n🎉 ETL Pipeline Completed Successfully!")
print("🧾 Check table: ecommerce_sales in PostgreSQL.\n")
