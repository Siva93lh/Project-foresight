# 🚀 Project FORESIGHT

## AI-Powered Demand and Inventory Intelligence Platform

### 🔗 Project Links

- 💻 [Source Code](https://colab.research.google.com/drive/1RIO6snK8Q13afRpnWi8Urhg9F6usvLvz?usp=sharing)
- 🚀 [Live Streamlit Dashboard](http://localhost:8501/)
- [Stremalit Dashboards.pdf](https://drive.google.com/file/d/1Lahq0u-KXLz5U3DU0DuUKlCpSbla7wVC/view?usp=sharing)

 
# 📌 INTRODUCTION
Project Foresight is an AI-powered demand forecasting and inventory intelligence platform designed to help businesses optimize stock planning and supply chain decisions. It combines Machine Learning, data analytics, and Power BI to forecast SKU-level demand, identify potential stockout and overstock risks, and provide actionable insights through an interactive Executive Dashboard.

# 🎯 OBJECTIVES

<ul>
<li>Forecast SKU-level demand using Machine Learning.</li>
<li>Identify potential stockout and overstock risks.</li>
<li>Analyze sales, inventory, and product performance.</li>
<li>Optimize inventory planning and stock management.</li>
<li>Create meaningful KPIs and DAX measures in Power BI.</li>
<li>Develop an interactive Executive Dashboard for data-driven decision-making.</li>
<li>Generate predictive and actionable business insights.</li>
</ul>

## 🚀 Project Resources

### 📊 Dashboards
- 🔗 [Power BI Dashboard](https://drive.google.com/file/d/1GPi8tSglUhy8l0QNr-Mgli-ceiIMTph0/view)
- 🌐 [Streamlit Dashboard](http://localhost:8501/)

### 📄 Project Documentation
- 📑 [View Project Documentation PDF](https://drive.google.com/file/d/125Ons3pcfdMVOp0_HidO6r-9xo9qRr_H/view)

### 📂 Datasets
- 📁 [ML Inventory Execution Dataset](https://docs.google.com/spreadsheets/d/1bZLiKhOEdLksPd-JxZCpiahjZHnvfuLT/edit?gid=1830116320#gid=1830116320)
- 📁 [Sku master dataset](https://docs.google.com/spreadsheets/d/1zGx8timgjNy4tImztdaYsLwJjGhk7Gpw/edit?gid=609439121#gid=609439121)
- 📁 [Customer Business ML Dataset](https://docs.google.com/spreadsheets/d/1mOEo-wIpo6N370-Sa_CmCbKXW3TnLzyK/edit?gid=545674598#gid=545674598)
- 📁 [Inventory Seasonality Dataset](https://docs.google.com/spreadsheets/d/1mOEo-wIpo6N370-Sa_CmCbKXW3TnLzyK/edit?gid=545674598#gid=545674598)
- 📁 [Promotional Datset](https://docs.google.com/spreadsheets/d/1nMYQqYIcREuX5Hli6yvjSNHEzF69IaLl/edit?gid=595165876#gid=595165876)
- 📁 [Overstock Dataset](https://docs.google.com/spreadsheets/d/1nbMJ3Cwpz74THDzN82Qhnx0xW0MrWWr-/edit?gid=1678652439#gid=1678652439)


## 🛠️ Tools & Technologies

<ul>
<li>Python</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Machine Learning</li>
<li>Microsoft Excel</li>
<li>Power BI</li>
<li>Power Query</li>
<li>DAX</li>
<li>GitHub</li>
</ul>


<h2>📊 Key KPIs</h2>

<ul>
<li>Total Sales</li>
<li>Total Quantity Sold</li>
<li>Total Demand</li>
<li>Forecasted Demand</li>
<li>Total Inventory</li>
<li>Inventory Value</li>
<li>Stockout Products</li>
<li>Low Stock Products</li>
<li>Overstock Products</li>
<li>Reorder Quantity</li>
<li>Safety Stock</li>
<li>Reorder Point</li>
<li>Forecast Accuracy</li>
<li>Inventory Turnover</li>
<li>Inventory Coverage</li>
</ul>

<h2>🧮 DAX Formulas Used</h2>
<ul>
<li>Total Sales = SUM('Inventory Data'[Sales])</li>
<li>Total Quantity Sold = SUM('Inventory Data'[Quantity Sold])</li>
<li>Total Inventory = SUM('Inventory Data'[Inventory Quantity])</li>
<li>Total Demand = SUM('Inventory Data'[Demand])</li>
<li>Average Demand = AVERAGE('Inventory Data'[Demand])</li>
<li>Forecasted Demand = SUM('Inventory Data'[Forecasted Demand])</li>
<li>Inventory Value = SUMX('Inventory Data', 'Inventory Data'[Inventory Quantity] * 'Inventory Data'[Unit Price])</li>
<li>Stockout Products = CALCULATE(DISTINCTCOUNT('Inventory Data'[Product ID]), 'Inventory Data'[Inventory Quantity] = 0)</li>
<li>Low Stock Products = CALCULATE(DISTINCTCOUNT('Inventory Data'[Product ID]), 'Inventory Data'[Inventory Quantity] &lt; 'Inventory Data'[Reorder Point])</li>
<li>Overstock Products = CALCULATE(DISTINCTCOUNT('Inventory Data'[Product ID]), 'Inventory Data'[Inventory Quantity] &gt; 'Inventory Data'[Maximum Stock Level])</li>
<li>Reorder Quantity = SUMX('Inventory Data', MAX(0, 'Inventory Data'[Reorder Point] - 'Inventory Data'[Inventory Quantity]))</li>
<li>Safety Stock = AVERAGEX('Inventory Data', 'Inventory Data'[Safety Stock])</li>
<li>Reorder Point = AVERAGEX('Inventory Data', 'Inventory Data'[Reorder Point])</li>
<li>Forecast Accuracy = 1 - DIVIDE(ABS([Total Demand] - [Forecasted Demand]), [Total Demand], 0)</li>
</ul>

  ## 📁 Project Repository Structure

```text
ML-Business-Analytics/
│
├── 📂 Dataset/
│   ├── Dataset_01.xlsx
│   ├── Dataset_02.xlsx
│   ├── Dataset_03.xlsx
│   ├── ...
│   └── Dataset_12.xlsx
│
├── 📂 Machine_Learning/
│   └── ML_Model.ipynb
│
├── 📂 PowerBI/
│   └── Executive_Dashboard.pbix
│
├── 📂 Screenshots/
│   ├── Executive_Dashboard.png
│   ├── Sales_Analysis.png
│   └── Inventory_Analysis.png
│
├── 📂 Documentation/
│   └── Project_Documentation.pdf
│
└── 📄 README.md
```

📌 **Conclusion**
- FORESIGHT integrates Data Analytics, Machine Learning, Power BI, DAX, and Streamlit into an end-to-end demand and inventory intelligence solution.
- The project transforms raw sales and inventory data into meaningful business insights through data preprocessing, EDA, feature engineering, and predictive analysis.
- The machine learning component helps forecast future product demand and identify changing demand patterns.
- Inventory analytics identifies stockout risks, overstock conditions, and replenishment requirements.
- Power BI provides interactive dashboards with KPIs, trends, filters, and inventory performance analysis.
- Streamlit provides a user-friendly interface for exploring forecasts, inventory insights, and recommendations.
- The project demonstrates how predictive analytics and business intelligence can support data-driven inventory planning and decision-making.








