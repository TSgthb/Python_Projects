# Analyzing Helicopter Prison Escape Attempts
> _This project was created using documentation available on [Dataquest](https://www.dataquest.io/blog/data-analyst-projects-for-beginners/)._

<p align="justify">
This project explores a unique dataset of <i> <a href="https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes#Actual_attempts">prison escapes attempted using helicopters</a></i>. 
<p>

<p align="justify">
The dataset, sourced from Wikipedia, includes details such as the date of the attempt, prison name, country, success status, and escapee names. The goal is to uncover patterns and insights related to these rare and high-risk escape attempts.
<p>

Jump to end for *[Analysis & Findings](https://github.com/TSgthb/Python_Projects/tree/main/Analyzing%20Helicopter%20Prison%20Escapes#analysis--findings).*

## Project Outline

1. **Environment Setup and Data Acquisition**  
   - Configured Python environment and imported helper functions from `helper.py`.  
   - Retrieved data from the Wikipedia page using a custom function `data_from_url()`.

2. **Data Loading and Preprocessing**  
   - Extracted relevant columns: Date, Prison Name, Country, Success Status, and Escapee(s).  
   - Removed unnecessary description fields and standardized the dataset structure.  
   - Converted date values to extract the year for temporal analysis.

3. **Feature Engineering**  
   - Created frequency tables for escape attempts per year and per country.  
   - Added a custom column for the number of escapees per attempt for deeper analysis.

4. **Exploratory Data Analysis (EDA)**  
   - Identified trends in helicopter escape attempts across years and countries.  
   - Visualized yearly attempt distribution using bar plots.  
   - Computed success rates and compared them across countries.

5. **Advanced Analysis**  
   - Determined countries with higher-than-average successful escape attempts.  
   - Calculated success ratios for each country and identified high-success regions.  
   - Analyzed the relationship between the number of escapees and success probability.

6. **Insights and Interpretation**  
   - Highlighted years and countries with the most helicopter escape attempts.  
   - Derived actionable insights on factors influencing success rates.

Check out the complete code, *[Analysis Notebook](https://github.com/TSgthb/Python_Projects/blob/main/Analyzing%20Helicopter%20Prison%20Escapes/Notebooks/Analysing%20Helicopter%20Prison%20Escapes.ipynb).*

## Analysis & Findings

1. **Time Series Analysis**  
   - Most helicopter escape attempts occurred in **1986, 2001, 2007, and 2009**, each recording **9 attempts**.

2. **Country Specific Insights**  
   - **France** leads with **15 attempts**, followed by **United States (8)** and **Canada (4)**.  
   - Countries with consistently high success rates and above-average attempts include **United States (75%)**, **France (73%)** and **Canada (75%)**.

3. **Success Rate Analysis**  
   - Overall success rate across all countries: **34 successful attempts out of 48 total attempts**.  
   - Countries with single attempts (e.g., Russia, Puerto Rico) show 100% success but lack statistical significance.

4. **Impact of Escapee Count**  
   - Success rates are highest for **groups of 2 or 3 escapees**, while single escapees have the most failures.  
   - Larger groups (4–5 escapees) show reduced success probability as well.

## Strategic Recommendations

Based on the analysis, the following recommendations can be made for further research or operational planning:

1. **Focus on High-Risk Regions**  
   - Countries like **France, United States, and Canada** should be prioritized for enhanced security measures during helicopter operations.

2. **Temporal Monitoring**  
   - Increased vigilance during months historically associated with higher escape attempts (e.g., mid-year and year-end).

3. **Group Dynamics Analysis**  
   - Investigate why smaller groups (2–3 escapees) succeed more often and design countermeasures accordingly.

4. **Data Enrichment**  
   - Collect additional details such as helicopter type, security protocols, and weather conditions to improve predictive modeling.


