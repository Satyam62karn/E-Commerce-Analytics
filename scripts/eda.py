import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = BASE_DIR / "data" / "processed" / "charts"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load Data
# -----------------------------
orders = pd.read_csv(DATA_DIR / "orders_cleaned.csv")
order_items = pd.read_csv(DATA_DIR / "order_items_cleaned.csv")
products = pd.read_csv(DATA_DIR / "products_cleaned.csv")
reviews = pd.read_csv(DATA_DIR / "reviews_cleaned.csv")

# -----------------------------
# Date Conversion
# -----------------------------
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"]
)

# -----------------------------
# 1. Monthly Sales Trend
# -----------------------------
delivered = orders[orders["order_status"] == "delivered"].copy()

sales = order_items.merge(
    delivered[["order_id"]],
    on="order_id",
    how="inner"
)

sales["month"] = sales["order_id"].map(
    orders.set_index("order_id")["order_purchase_timestamp"]
).dt.to_period("M").astype(str)

monthly_sales = sales.groupby("month")["price"].sum()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

# -----------------------------
# 2. Top 10 Categories by Sales
# -----------------------------
category_sales = sales.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left"
)

top_categories = (
    category_sales.groupby("product_category_name")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
top_categories.plot(kind="barh")
plt.title("Top 10 Product Categories by Sales")
plt.xlabel("Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_categories_sales.png", dpi=300)
plt.close()

# -----------------------------
# 3. Review Score Distribution
# -----------------------------
review_counts = reviews["review_score"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
review_counts.plot(kind="bar")
plt.title("Customer Review Score Distribution")
plt.xlabel("Review Score")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "review_score_distribution.png", dpi=300)
plt.close()

# -----------------------------
# 4. Order Status Distribution
# -----------------------------
status_counts = orders["order_status"].value_counts()

plt.figure(figsize=(9, 5))
status_counts.plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "order_status_distribution.png", dpi=300)
plt.close()

# -----------------------------
# 5. Delivery Performance
# -----------------------------
delivery = delivered.copy()

delivery["delivery_diff_days"] = (
    delivery["order_delivered_customer_date"]
    - delivery["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

performance = pd.Series({
    "On Time / Early": (delivery["delivery_diff_days"] <= 0).sum(),
    "Late": (delivery["delivery_diff_days"] > 0).sum()
})

plt.figure(figsize=(7, 5))
performance.plot(kind="bar")
plt.title("Delivery Performance")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "delivery_performance.png", dpi=300)
plt.close()

print("EDA completed successfully!")
print(f"Charts saved in: {OUTPUT_DIR}")