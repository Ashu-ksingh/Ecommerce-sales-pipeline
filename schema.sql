CREATE TABLE IF NOT EXISTS agg_category (
    category VARCHAR(50),
    total_revenue NUMERIC
);

CREATE TABLE IF NOT EXISTS agg_customer (
    customer_id INT,
    customer_name VARCHAR(100),
    customer_revenue NUMERIC
);

CREATE TABLE IF NOT EXISTS agg_top_products (
    product_id INT,
    product_name VARCHAR(100),
    revenue NUMERIC
);
