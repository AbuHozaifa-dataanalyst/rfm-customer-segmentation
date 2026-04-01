# 🛍️ Customer Segmentation using RFM Analysis

## 📌 Overview

This project applies **RFM (Recency, Frequency, Monetary) Analysis** on retail transaction data to segment customers and generate actionable business insights.

The project is designed using a **production-level structure**, combining:

* Python (modular package)
* SQL (analytical queries)
* Business intelligence thinking

---

## 🎯 Objectives

* Understand customer purchasing behavior
* Segment customers into meaningful groups
* Identify high-value and at-risk customers
* Provide data-driven business recommendations

---

## 🧱 Project Architecture

```
rfm_customer_segmentation/
│
├── src/                         # Reusable Python package
├── notebooks/                   # Step-by-step analysis
├── data/                        # Raw & processed datasets
├── sql/                         # SQL scripts (schema, ingestion, analysis)
├── reports/                     # Visualizations & summaries
├── dashboards/                 # BI dashboards (Power BI)
└── README.md
```

---

## 📊 Dataset

* Source: Online Retail Dataset
* Contains transactional data such as:

  * Customer ID
  * Invoice Date
  * Product Code
  * Quantity
  * Unit Price

---

## 🔄 Workflow

### 1️⃣ Data Preprocessing

* Removed missing customer IDs
* Filtered out returns (negative quantities)
* Cleaned and standardized data types
* Created `TotalAmount` column

---

### 2️⃣ Feature Engineering (RFM Metrics)

* **Recency (R):** Days since last purchase
* **Frequency (F):** Number of transactions
* **Monetary (M):** Total customer spending

---

### 3️⃣ RFM Scoring

* Applied quantile-based scoring (1–5 scale)
* Higher scores indicate better customer value

---

### 4️⃣ Customer Segmentation

Customers were grouped into:

| Segment                | Description                         |
| ---------------------- | ----------------------------------- |
| 🟢 Champions           | High value, frequent, recent buyers |
| 🟡 Loyal Customers     | Consistent repeat customers         |
| 🔵 Potential Loyalists | Recent but low frequency            |
| 🔴 At Risk             | Previously active, now inactive     |
| ⚫ Lost Customers       | Inactive and low value              |

---

### 5️⃣ SQL Implementation

* Built RFM logic using **CTEs and window functions**
* Used `NTILE()` for scoring
* Created reusable **views** for reporting

---

## 📈 Key Insights

* A small percentage of customers (**Champions**) contribute the majority of revenue
* A significant portion of customers are **At Risk or Lost**
* Customer retention presents a major opportunity for revenue growth

---

## 💡 Business Recommendations

### 🟢 Champions

* Loyalty programs
* VIP access and rewards

### 🟡 Loyal Customers

* Cross-selling and upselling
* Personalized offers

### 🔵 Potential Loyalists

* Engagement campaigns
* Incentives for repeat purchases

### 🔴 At Risk

* Win-back campaigns
* Discount offers

### ⚫ Lost Customers

* Re-engagement strategies or cost optimization

---

## 📊 Visualizations

### Customer Segment Distribution

![Segment Distribution](reports/figures/segment_distribution.png)

### Revenue by Segment

![Revenue by Segment](reports/figures/revenue_by_segment.png)

---

## 🛠️ Tech Stack

* **Python:** Pandas, NumPy, Matplotlib
* **SQL:** SQL Server (CTEs, Window Functions)
* **BI Tools:** Power BI
* **Environment:** VS Code, Jupyter Notebook

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/rfm_customer_segmentation.git
cd rfm_customer_segmentation
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Notebooks

```bash
jupyter notebook
```

---

## 🧠 Advanced Features

* Modular Python package (`src/`)
* SQL-based RFM pipeline
* Business-driven segmentation logic
* Reusable analytical workflows

---

## 🚀 Future Improvements

* Implement **K-Means clustering** for segmentation validation
* Add **Customer Lifetime Value (CLV)** modeling
* Build interactive dashboards
* Automate data pipeline

---

## 🧪 Testing

Basic unit tests included for core RFM functions.

---

## 📌 Key Takeaway

This project demonstrates how customer transaction data can be transformed into **actionable insights**, enabling businesses to improve retention, increase revenue, and optimize marketing strategies.

---

## 👤 Author

**Your Name**
Retail / Data Analyst

---

## 📜 License

This project is licensed under the MIT License.
