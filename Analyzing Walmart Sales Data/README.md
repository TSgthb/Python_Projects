# Analyzing Shopping Store Sales Data

<p align="justify">
This project showcases the implementation of an end-to-end data analysis pipeline using a sample retail dataset from Walmart, a global hyperstore chain. It leverages SQL Server, Python, and Jupyter Notebook to cover the entire process, from connecting to the data source and retrieving data via API, to cleaning, transforming, and standardizing it for database loading in SQL Server using Python. The pipeline also enables exploratory analysis and delivers actionable business insights through advanced SQL techniques, including CTEs, subqueries, and window functions. The entire pipeline has been set-up using a Jupyter Notebook.
<p>

Jump to end for [Findings & Conclusion](https://github.com/TSgthb/Python_Projects/edit/main/Analyzing%20Walmart%20Sales%20Data/README#findings--conclusion)

## Project Overview

- Set-up environment for ingesting Walmart dataset from Kaggle using API and Python module `kaggle`.
- Create a Jupyter Notebook and import the required Python modules for setting up DataFrame `walmart_df`, connecting to SQL Server database and carrying out analysis.
- Import the dataset to Python dataframe using `pandas`. Additionally, clean, transform and standardize the data within to facilitate EDA and advanced analytics.
- Establish a connection to SQL Server, create a database `walmart_db` and export the DataFrame to table, `walmart_sales` using `pyodbc` and `sqlalchemy`.
- Analyze dataset using SQL queries to extract insights and answer business questions related to revenue trends, best selling categories, profit analysis and more.

Check out the complete code here: [Analysis Notebook](https://github.com/TSgthb/Python_Projects/blob/main/Analyzing%20Walmart%20Sales%20Data/Notebooks/analysis_notebook.ipynb)

## Findings & Conclusion

