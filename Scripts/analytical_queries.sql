-- Get top 5 sales records where total sales exceed 500
SELECT TOP 5 *              
    FROM dbo.walmart_sales      
    WHERE total_sales > 500 
GO;

-- Get the total number of records in the walmart_sales table
SELECT COUNT(*) AS total_records    
FROM dbo.walmart_sales 
GO;

-- Get the total number of unique branches in the walmart_sales table
SELECT COUNT(DISTINCT branch) AS total_records               
FROM dbo.walmart_sales  
GO;

-- Get the maximum and minimum total sales amounts from the walmart_sales table
SELECT                                                        
    MAX(total_sales) AS max_sale_amount,                      
    MIN(total_sales) AS min_sale_amount                       
FROM dbo.walmart_sales                                        
GO;

-- Find different payment methods, their counts and total corresponding sales and quantity sold
SELECT                                              
    payment_method,                                 
    COUNT(*) AS count_payments,                     
    SUM(total_sales) AS tot_sales,                  
    CAST(SUM(quantity) AS INT) AS tot_quantity      
FROM dbo.walmart_sales                              
GROUP BY payment_method
GO;


-- Get 10 top-rated branches based on the average customer ratings on each category within the branc
WITH cat_rank AS                                                                            
    (                                                                                           
    SELECT                                                                                      
        branch,                                                                                 
        category,                                                                               
        ROUND(AVG(rating), 2) AS avg_rating,                                                    
        ROW_NUMBER() OVER(PARTITION BY branch ORDER BY AVG(rating) DESC) AS rank_category       
    FROM dbo.walmart_sales                                                                      
    GROUP BY                                                                                    
        branch,                                                                                 
        category                                                                                
    )                                                                                           
    SELECT TOP 10                                                                               
        cr.branch,                                                                              
        cr.category,                                                                            
        cr.avg_rating                                                                           
    FROM cat_rank cr                                                                            
    WHERE rank_category = 1                                                                     
    ORDER BY cr.avg_rating DESC  

-- Get the top-rated category for each branch based on average customer ratings
WITH cat_rank AS
(
SELECT
    branch,
    category,
    ROUND(AVG(rating), 2) AS avg_rating,
    ROW_NUMBER() OVER(PARTITION BY branch ORDER BY AVG(rating) DESC) AS rank_category
FROM walmart_sales
GROUP BY 
    branch, 
    category
)
SELECT
    cr.branch,
    cr.category,
    cr.avg_rating
FROM cat_rank cr
WHERE rank_category = 1
GO;

-- Find the busiest day for each branch based on total transactions
WITH per_day_trans AS
(
    SELECT
        ws.branch,
        CAST(ws.date AS DATE) AS date_sale,
        FORMAT(ws.date,'dddd') AS day_name,
        COUNT(*) AS tot_transactions,
        ROW_NUMBER() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS rank_trans
    FROM dbo.walmart_sales ws
    GROUP BY
        ws.branch,
        ws.date
)
SELECT
    pdt.branch,
    pdt.date_sale,
    pdt.day_name,
    pdt.tot_transactions
FROM per_day_trans pdt
WHERE
    rank_trans = 1
GO;

-- Get city and category-wise maximum, minimum, and average ratings
SELECT
    city,
    category,
    MAX(rating) AS max_rat,
    MIN(rating) AS min_rat,
    ROUND(AVG(rating), 1) AS avg_rat
FROM dbo.walmart_sales
GROUP BY
    city,
    category
ORDER BY
    city,
    category
GO;

-- Get total profit for each category
SELECT
    fsq.category,
    ROUND(SUM(fsq.total_sales), 2) AS tot_sales,
    ROUND(SUM(fsq.profit_of_all_sales), 2) AS tot_profit
FROM
    (
        SELECT
            category,
            total_sales,
            total_sales * profit_margin AS profit_of_all_sales
        FROM
            dbo.walmart_sales
    ) AS fsq
GROUP BY
    fsq.category
ORDER BY
    tot_profit DESC

-- Find the most popular payment method for each branch
SELECT
    fsq.branch,
    fsq.payment_method
FROM
    (
        SELECT
            branch,
            payment_method,
            COUNT(*) AS total_transactions,
            ROW_NUMBER() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS transaction_rank
        FROM 
            dbo.walmart_sales
        GROUP BY
            branch,
            payment_method
    ) AS fsq
WHERE
    fsq.transaction_rank = 1
ORDER BY
    fsq.branch

-- Categorize sales into Morning, Afternoon, and Night based on time and get total transactions for each category
WITH categorized_sales AS
(
    SELECT 
        *,
        CASE 
            WHEN time >= '00:00:00' AND time < '12:00:00' THEN 'Morning'
            WHEN time < '17:00:00' THEN 'Afternoon'
            ELSE 'Night'
        END AS sale_time_category
    FROM dbo.walmart_sales ws
)
SELECT
    cs.sale_time_category,
    COUNT(*) AS total_transactions
FROM categorized_sales cs
GROUP BY
    cs.sale_time_category
ORDER BY
    total_transactions DESC
GO;

-- Year-over-Year sales analysis to find top 5 branches with lowest percentage increase in sales from 2022 to 2023
WITH yoy_analysis AS
(
    SELECT
        branch,
        YEAR(date) AS year_of_sale,
        ROUND(SUM(total_sales), 2) AS tot_sales,
        LAG(ROUND(SUM(total_sales), 2)) OVER(PARTITION BY branch ORDER BY YEAR(date)) AS prev_tot_sales
    FROM    
        dbo.walmart_sales
    WHERE
        YEAR(date) in (2022,2023)
    GROUP BY
        branch,
        YEAR(date)
)
SELECT TOP 5
    ya.branch,
    ya.tot_sales,
    ya.prev_tot_sales,
    ROUND(((ya.tot_sales - ya.prev_tot_sales)/ya.prev_tot_sales) * 100, 2) AS perc_change
FROM
    yoy_analysis ya
WHERE
    ya.prev_tot_sales IS NOT NULL
ORDER BY
    perc_change