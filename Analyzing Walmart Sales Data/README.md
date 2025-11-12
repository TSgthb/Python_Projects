# Analyzing Shopping Store Sales Data

## Overview

<p align="justify">
This project showcases the implementation of an end-to-end data analysis pipeline using a sample retail dataset from Walmart, a global hyperstore chain.
<p>

<p align="justify">
It leverages SQL Server, Python, and Jupyter Notebook to cover the entire process, from connecting to the data source and retrieving data via API, to cleaning, transforming, and standardizing it for database loading in SQL Server using Python. 
<p>

<p align="justify">  
The pipeline also enables exploratory analysis and delivers actionable business insights through advanced SQL techniques, including CTEs, subqueries, and window functions. The entire pipeline has been set-up using a Jupyter Notebook.
<p>

Jump to end for *[Analysis & Findings](https://github.com/TSgthb/Python_Projects/tree/main/Analyzing%20Walmart%20Sales%20Data#analysis--findings).*

## Project Outline

1. **Environment Setup and Data Acquisition**  
   - Configured the Python environment using VSCode and installed required libraries, `pandas`, `sqlalchemy`, and `pyodbc`.  
   - Ingested the Walmart *[dataset](https://www.kaggle.com/najir0123/walmart-10k-sales-datasets)* from Kaggle using the Kaggle API and Python module `kaggle`.

2. **Notebook Initialization and Library Imports**  
   - Created a Jupyter Notebook as the central workspace for the data loading, tranformation and analysis.  
   - Imported essential Python libraries for data manipulation, database connectivity, and SQL execution.  

3. **Data Loading and Exploration**  
   - Loaded the dataset into a Pandas DataFrame (`walmart_df`).  
   - Performed initial checks on data structure, shape, and column types using `.info()` and `.describe()`.

4. **Data Cleaning and Transformation**  
   - Removed duplicate rows and handled missing values(by deleting them) to ensure data integrity.  
   - Converted `unit_price` from object to numeric by stripping currency symbols and casting to `float`.  
   - Parsed `date` and `time` columns into appropriate `datetime` formats for time-series analysis.  
   - Created a new calculated column `total_sales` for revenue analysis.  
   - Standardized column names for consistency.

5. **Database Integration**  
   - Established a secure connection to SQL Server using `pyodbc` and `sqlalchemy`.  
   - Created a new database `walmart_db` and exported the cleaned DataFrame to a table `walmart_sales`.  
   - Verified successful data persistence in SQL Server for subsequent queries.

6. **Exploratory Data Analysis (EDA)**  
   - Queried the database to validate record counts and data integrity.  
   - Generated summary statistics for sales, quantity, and profit margins.  
   - Identified maximum and minimum sales values and overall transaction distribution.  

7. **Advanced SQL Analytics**  
   - Implemented SQL queries using adavced SQL concepts such as CTEs, window functions, and aggregations to derive insights on:  
     * Payment method-wise sales and quantity distribution.  
     * Category-level revenue and profitability analysis.  
     * Customer rating trends across branches and categories.  
     * Time-of-day transaction patterns (Morning, Afternoon, Night).  
     * Year-over-Year (YoY) performance analysis for branches.

Check out the complete code, *[Analysis Notebook](https://github.com/TSgthb/Python_Projects/blob/main/Analyzing%20Walmart%20Sales%20Data/Notebooks/analysis_notebook.ipynb).*

## Analysis & Findings

Based on the analysis of the data conducted, following are the key findings that could be targeted upon for maximizing business, improving customer engagement and reverse negative sales trends:

1. **Data Integrity and Preparation**  
   - The original dataset was cleaned from 10,051 records to 9,969 valid transactions after removing duplicates and missing values.
   - Key transformations included converting `unit_price` to numeric, parsing date and time fields, and creating a calculated column, `total_sales` for enriching data quality.  

2. **Sales and Profitability**  
   - The Fashion Accessories and Home & Lifestyle categories dominate revenue with approximately $489,480 and $489,250 respectively. These categories not only lead in total sales but also contribute the highest profits, indicating that they are core drivers of business growth. 
   - Health and Beauty, despite generating the lowest revenue ($46,851), achieved the highest customer satisfaction ratings (average ~9.7), indicating strong brand loyalty potential.  
   - Overall profit margins average around 39%, reflecting consistent profitability across transactions. 

3. **Customer Payment Preferences**  
   - Payment preferences strongly favor digital methods. Credit Card transactions account for $488,821, closely followed by Ewallet at $457,316, while Cash lags behind at $263,589.
   - This trend highlightes the importance of maintaining convenient and robust digital payment infrastructure to meet customer expectations.

4. **Customer Behavior and Time-of-Day Trends**  
   - Customer shopping patterns show that Night transactions are the most frequent with 4,273 records, followed by Afternoon (3,609) and Morning (2,087).
   - This indicates that promotional campaigns and staffing strategies should prioritize evening hours to maximize engagement and sales.

5. **Branch-Level Performance**  
   - Year-over-Year analysis (2022 to 2023) reveals significant declines in some branches. The bottom five branches experienced declines exceeding 50%, with WALM045 showing the steepest drop at -62.62%.
   - These declines indicate operational or market challenges that require targeted interventions to reverse negative trends.

<p align="justify">  
<b>Conclusion:</b> Walmart’s business is driven by a few high-performing categories and strong digital payment adoption. However, branch-level declines and underperforming categories require focused intervention strategies. Leveraging time-of-day trends and enhancing customer experience in high-rated but low-revenue categories can create balanced growth oppurtunities.
<p>

## Strategic Recommendations

Below are the few actionable strategies that could help the business grow by leveraging high-value oppurtunities and reversing negative sales trends:

1. **Enhance Digital Payment Experience**  
   - Invest in secure, fast, and user-friendly digital payment systems to strengthen customer trust and convenience.  
   - Introduce loyalty rewards for Ewallet and Credit Card users to reinforce adoption.  

2. **Category-Level Growth Strategy**  
   - Expand product range and marketing for Fashion Accessories and Home & Lifestyle to sustain revenue leadership.  
   - Develop targeted campaigns for Health and Beauty to convert high satisfaction into higher sales.  

3. **Branch Performance Improvement**  
   - Conduct operational audits for branches with >50% YoY decline.  
   - Implement localized promotions and community engagement programs to revive sales.  

4. **Time-of-Day Optimization**  
   - Schedule promotional offers and flash sales during evening hours to leverage peak transaction periods.  
   - Adjust staffing and inventory management to align with night-time demand.  

5. **Customer Experience and Personalization**  
   - Use rating insights to personalize recommendations and improve service quality in categories with mixed ratings.  
   - Deploy targeted surveys to understand customer expectations in underperforming branches.


