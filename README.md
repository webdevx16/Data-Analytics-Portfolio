# Data Analytics Portfolio
**Author:** webdevx16

Project 1: Enterprise Sales & Operations Infrastructure
**Core Stack:** Excel, Power BI, SQL (Relational Modeling)

* **Objective:** Transformed raw, local Excel transactional logs into an automated executive business intelligence dashboard.

* **Key Features 1:** Created dynamic visual relationships between datasets without formula overhead, implemented manager-specific slicers, and designed a top-level KPI revenue card.
* **2:** Data Engineering & Relational Design (SQL Blueprint)
Before visualizing metrics, data must be structured to prevent relational corruption and memory leaks. I utilize structured queries to isolate, aggregate, and join disparate relational entities. 

Key architectural patterns implemented include:
* **Multi-Table Normalization:** Employing `INNER JOIN` mechanics across keys (e.g., matching `Orders` transactional logs with `Customers` attributes) to minimize redudant flat-file dimensions.
* **Granular Row vs. Categorical Filtering:** Applying optimal execution-order pipelines using `WHERE` to restrict row memory prior to compilation, alongside `HAVING` predicates to isolate aggregated performance targets (e.g., filtering `AVG(Revenue) > 500` post-grouping).
* **Corporate Aggregations:** Constructing executive summary views leveraging `GROUP BY` paired with mathematical statistical functions (`SUM`, `AVG`, `COUNT`) to compress millions of rows into dynamic analytical views.

**3:** **Tech Stack & Engineering Pipeline**

* **Database Engine:** SQL / MySQL (Relational storage hosting transactional records)
* **Core Logic:** Python 3.x (Pandas, Datetime engines)
* **Version Control:** Git & GitHub



### 🔄 Data Flow Architecture
1.  **Extract:** Python connects to the underlying SQL environment to fetch raw sales and staff execution logs.
2.  **Transform:** The engine enforces strict data cleaning constraints—handling missing attributes, formatting timestamp fields, and calculating derived metrics.
3.  **Load:** The pipeline outputs structured, high-performing CSV analytical reports (`sales_staff_analytics.csv`) ready to feed directly into visualization tools.

### 📂 Repository Contents
* `pipeline.py` - The core automation script containing data extraction and transformation logic.
* `sales_staff_analytics.csv` - The clean, calculated analytical output layer.
* `my_first_pipeline_output.csv` - Initial transactional processing execution logs.