import pandas as pd
import os

# Paths
RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

print("Starting data cleaning...\n")

# -----------------------------
# 1. Orders
# -----------------------------
orders = pd.read_csv(f"{RAW_PATH}/olist_orders_dataset.csv")

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

orders.to_csv(
    f"{PROCESSED_PATH}/orders_cleaned.csv",
    index=False
)

print("Orders cleaned:", orders.shape)


# -----------------------------
# 2. Customers
# -----------------------------
customers = pd.read_csv(
    f"{RAW_PATH}/olist_customers_dataset.csv"
)

customers.to_csv(
    f"{PROCESSED_PATH}/customers_cleaned.csv",
    index=False
)

print("Customers cleaned:", customers.shape)


# -----------------------------
# 3. Order Items
# -----------------------------
order_items = pd.read_csv(
    f"{RAW_PATH}/olist_order_items_dataset.csv"
)

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

order_items.to_csv(
    f"{PROCESSED_PATH}/order_items_cleaned.csv",
    index=False
)

print("Order items cleaned:", order_items.shape)


# -----------------------------
# 4. Payments
# -----------------------------
payments = pd.read_csv(
    f"{RAW_PATH}/olist_order_payments_dataset.csv"
)

payments.to_csv(
    f"{PROCESSED_PATH}/payments_cleaned.csv",
    index=False
)

print("Payments cleaned:", payments.shape)


# -----------------------------
# 5. Reviews
# -----------------------------
reviews = pd.read_csv(
    f"{RAW_PATH}/olist_order_reviews_dataset.csv"
)

reviews["review_comment_title"] = reviews[
    "review_comment_title"
].fillna("No comment")

reviews["review_comment_message"] = reviews[
    "review_comment_message"
].fillna("No comment")

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

reviews.to_csv(
    f"{PROCESSED_PATH}/reviews_cleaned.csv",
    index=False
)

print("Reviews cleaned:", reviews.shape)


# -----------------------------
# 6. Products + Translation
# -----------------------------
products = pd.read_csv(
    f"{RAW_PATH}/olist_products_dataset.csv"
)

translation = pd.read_csv(
    f"{RAW_PATH}/product_category_name_translation.csv"
)

# Fill missing product category
products["product_category_name"] = products[
    "product_category_name"
].fillna("unknown")

# Merge English category names
products = products.merge(
    translation,
    on="product_category_name",
    how="left"
)

# Manual translation for categories
manual_translation = {
    "pc_gamer": "gaming_pc",
    "portateis_cozinha_e_preparadores_de_alimentos":
        "portable_kitchen_food_preparers"
}

products["product_category_name_english"] = (
    products["product_category_name_english"]
    .fillna(
        products["product_category_name"].map(manual_translation)
    )
    .fillna("unknown")
)

products.to_csv(
    f"{PROCESSED_PATH}/products_cleaned.csv",
    index=False
)

print("Products cleaned:", products.shape)


# -----------------------------
# 7. Sellers
# -----------------------------
sellers = pd.read_csv(
    f"{RAW_PATH}/olist_sellers_dataset.csv"
)

sellers.to_csv(
    f"{PROCESSED_PATH}/sellers_cleaned.csv",
    index=False
)

print("Sellers cleaned:", sellers.shape)


# -----------------------------
# 8. Geolocation
# -----------------------------
geolocation = pd.read_csv(
    f"{RAW_PATH}/olist_geolocation_dataset.csv"
)

# Remove exact duplicate rows
geolocation = geolocation.drop_duplicates()

geolocation.to_csv(
    f"{PROCESSED_PATH}/geolocation_cleaned.csv",
    index=False
)

print("Geolocation cleaned:", geolocation.shape)


# -----------------------------
# Final message
# -----------------------------
print("\nData cleaning completed successfully!")
print(f"Cleaned files saved in: {PROCESSED_PATH}")