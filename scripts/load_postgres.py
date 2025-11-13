import os
import psycopg2
import pandas as pd
import json

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config
config_path = os.path.join(BASE_DIR, "config", "config.json")
with open(config_path) as f:
    config = json.load(f)

pg_cfg = config["postgres"]
processed_path = os.path.join(BASE_DIR, "data", "processed")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=pg_cfg["host"],
    port=pg_cfg["port"],
    user=pg_cfg["user"],
    password=pg_cfg["password"],
    dbname=pg_cfg["database"]
)
cur = conn.cursor()

def load_csv_to_pg(csv_folder, table_name):
    folder_path = os.path.join(processed_path, csv_folder)
    if not os.path.exists(folder_path):
        print(f"⚠️ Folder not found: {folder_path}")
        return
    csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
    if not csv_files:
        print(f"⚠️ No CSV found in {folder_path}")
        return
    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)
    print(f"📥 Loading {len(df)} rows into {table_name}...")

    for _, row in df.iterrows():
        cols = ','.join(df.columns)
        vals = ','.join(['%s'] * len(row))
        sql = f"INSERT INTO {table_name} ({cols}) VALUES ({vals})"
        cur.execute(sql, tuple(row))
    conn.commit()
    print(f"✅ Loaded {table_name}")

# Load each processed dataset
load_csv_to_pg("agg_category", "agg_category")
load_csv_to_pg("agg_customer", "agg_customer")
load_csv_to_pg("agg_top_products", "agg_top_products")

cur.close()
conn.close()
print("🎯 All processed data loaded into PostgreSQL successfully.")
