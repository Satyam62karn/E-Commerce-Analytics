# 🛒 E-Commerce Analytics

An end-to-end **E-Commerce Data Analytics project** focused on transforming raw e-commerce data into meaningful business insights using **Python, Pandas, NumPy, Matplotlib, and Seaborn**.

The project covers data cleaning, exploratory data analysis (EDA), sales analysis, customer analysis, product performance, order trends, reviews, and delivery performance.

---

## 📌 Project Overview

E-commerce businesses generate large volumes of data across customers, orders, products, payments, sellers, reviews, and deliveries.

The goal of this project is to analyze these datasets and identify patterns that can help understand:

* Sales performance
* Customer behavior
* Product and category performance
* Order trends
* Delivery performance
* Customer review patterns
* Business growth opportunities

---

## 🎯 Objectives

* Clean and prepare raw e-commerce datasets for analysis
* Perform Exploratory Data Analysis (EDA)
* Analyze sales and order trends
* Identify top-performing product categories
* Understand customer purchasing behavior
* Analyze delivery performance
* Examine customer review scores
* Generate meaningful visualizations and business insights

---

## 🗂️ Dataset

The project uses the **Brazilian E-Commerce Public Dataset by Olist**, containing information related to:

* Customers
* Orders
* Order Items
* Payments
* Products
* Sellers
* Reviews
* Geolocation
* Product Categories

The raw datasets are stored inside the `data/raw/` directory.

---

## 🛠️ Technologies & Tools

| Technology     | Purpose                        |
| -------------- | ------------------------------ |
| **Python**     | Data analysis and processing   |
| **Pandas**     | Data cleaning and manipulation |
| **NumPy**      | Numerical operations           |
| **Matplotlib** | Data visualization             |
| **Seaborn**    | Statistical visualization      |
| **Git**        | Version control                |
| **GitHub**     | Project repository             |

---

## 🔄 Project Workflow

```text
Raw E-Commerce Data
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Processed Datasets
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Visualization
        │
        ▼
Business Insights
```

---

## 📊 Analysis Performed

### 💰 Sales Analysis

* Monthly sales trends
* Sales performance over time
* Revenue distribution
* Top-performing categories

### 🛍️ Product Analysis

* Product category performance
* Number of products
* Top categories by sales
* Product-related trends

### 👥 Customer Analysis

* Customer distribution
* Customer purchasing behavior
* Customer-related sales patterns

### 📦 Order Analysis

* Order status distribution
* Order trends
* Delivery performance
* Order completion patterns

### ⭐ Review Analysis

* Review score distribution
* Customer satisfaction patterns
* Relationship between reviews and orders

---

## 📈 Visualizations

The project includes several visualizations, including:

* 📊 Monthly Sales Trend
* 📊 Top Categories by Sales
* 🥧 Order Status Distribution
* ⭐ Review Score Distribution
* 🚚 Delivery Performance

All generated charts are available in:

```text
data/processed/charts/
```

---

## 📁 Project Structure

```text
E-Commerce-Analytics/
│
├── data/
│   │
│   ├── raw/
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_geolocation_dataset.csv
│   │   ├── olist_order_items_dataset.csv
│   │   ├── olist_order_payments_dataset.csv
│   │   ├── olist_order_reviews_dataset.csv
│   │   ├── olist_orders_dataset.csv
│   │   ├── olist_products_dataset.csv
│   │   ├── olist_sellers_dataset.csv
│   │   └── product_category_name_translation.csv
│   │
│   └── processed/
│       ├── customers_cleaned.csv
│       ├── geolocation_cleaned.csv
│       ├── order_items_cleaned.csv
│       ├── orders_cleaned.csv
│       ├── payments_cleaned.csv
│       ├── products_cleaned.csv
│       ├── reviews_cleaned.csv
│       ├── sellers_cleaned.csv
│       │
│       └── charts/
│           ├── delivery_performance.png
│           ├── monthly_sales_trend.png
│           ├── order_status_distribution.png
│           ├── review_score_distribution.png
│           └── top_categories_sales.png
│
├── scripts/
│   ├── clean_data.py
│   └── eda.py
│
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Satyam62karn/E-Commerce-Analytics.git
```

### 2. Navigate to the project

```bash
cd E-Commerce-Analytics
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run data cleaning

```bash
python scripts/clean_data.py
```

### 5. Run exploratory data analysis

```bash
python scripts/eda.py
```

---

## 💡 Key Business Questions

This project aims to answer questions such as:

* How are sales changing over time?
* Which product categories generate the highest sales?
* What is the distribution of order statuses?
* How well are orders being delivered?
* What review scores are most common?
* Which areas of the business require improvement?
* What patterns can be identified from customer and order data?

---

## 🔮 Future Improvements

Planned improvements include:

* Building an interactive **Power BI dashboard**
* Adding SQL-based analysis
* Creating customer segmentation
* Adding advanced business KPIs
* Performing deeper statistical analysis
* Developing predictive analytics models

---

## 👨‍💻 Author

### Satyam Kumar Karn

**MCA – Data Analytics**

Interested in:

* Data Analytics
* Business Analytics
* Python
* SQL
* Power BI
* Machine Learning

🔗 **GitHub:**
https://github.com/Satyam62karn

---

## ⭐ Project Status

## 📌 Project Status

**Completed:** Data Cleaning + EDA + SQL Analysis + Visualizations + Interactive Power BI Dashboard

---

⭐ If you find this project useful, consider giving it a star!