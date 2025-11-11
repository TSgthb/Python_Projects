**Environment and Data Initialization**


```python
# Import the required libraries
import time
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import text
```


```python
# Read the dataset into the dataframe for the analysis
walmart_df = pd.read_csv("C:\\Users\\Admin\\Documents\\OneDrive\\Desktop\\Python\\Walmart Sales Analysis\\Datasets\\Walmart.csv")
```

**Data Transformation & Cleaning**


```python
# Check the srtucture of the dataframe
print(walmart_df.info())

# Check the shape of the dataframe
print('Shape:', walmart_df.shape)
```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10051 entries, 0 to 10050
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   invoice_id      10051 non-null  int64  
     1   Branch          10051 non-null  object 
     2   City            10051 non-null  object 
     3   category        10051 non-null  object 
     4   unit_price      10020 non-null  object 
     5   quantity        10020 non-null  float64
     6   date            10051 non-null  object 
     7   time            10051 non-null  object 
     8   payment_method  10051 non-null  object 
     9   rating          10051 non-null  float64
     10  profit_margin   10051 non-null  float64
    dtypes: float64(3), int64(1), object(7)
    memory usage: 863.9+ KB
    None
    Shape: (10051, 11)
    


```python
# Check the statistical summary of the dataframe
print(walmart_df.describe())

print('\n')

# Check for quantity of missing values in the dataframe
print(walmart_df.isnull().sum())

print('\n')

# Check for duplicate rows in the dataframe
duplicate_rows = walmart_df.duplicated().sum()
print('Number of duplicate rows:', duplicate_rows)
```

             invoice_id      quantity        rating  profit_margin
    count  10051.000000  10020.000000  10051.000000   10051.000000
    mean    5025.741220      2.353493      5.825659       0.393791
    std     2901.174372      1.602658      1.763991       0.090669
    min        1.000000      1.000000      3.000000       0.180000
    25%     2513.500000      1.000000      4.000000       0.330000
    50%     5026.000000      2.000000      6.000000       0.330000
    75%     7538.500000      3.000000      7.000000       0.480000
    max    10000.000000     10.000000     10.000000       0.570000
    
    
    invoice_id         0
    Branch             0
    City               0
    category           0
    unit_price        31
    quantity          31
    date               0
    time               0
    payment_method     0
    rating             0
    profit_margin      0
    dtype: int64
    
    
    Number of duplicate rows: 51
    


```python
# Handling dupicated rows
# For our case, we will remove the duplicated rows
if duplicate_rows > 0:
    walmart_df.drop_duplicates(inplace=True)
    print('Duplicate rows removed.')

# Verify removal of duplicate rows
print('Number of duplicate rows after removal:', walmart_df.duplicated().sum())
```

    Duplicate rows removed.
    Number of duplicate rows after removal: 0
    


```python
# Check the structure of the data
print(walmart_df.info())

print('\n')

# Check the shape of the data
print('Shape:', walmart_df.shape)
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 10000 entries, 0 to 9999
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   invoice_id      10000 non-null  int64  
     1   Branch          10000 non-null  object 
     2   City            10000 non-null  object 
     3   category        10000 non-null  object 
     4   unit_price      9969 non-null   object 
     5   quantity        9969 non-null   float64
     6   date            10000 non-null  object 
     7   time            10000 non-null  object 
     8   payment_method  10000 non-null  object 
     9   rating          10000 non-null  float64
     10  profit_margin   10000 non-null  float64
    dtypes: float64(3), int64(1), object(7)
    memory usage: 937.5+ KB
    None
    
    
    Shape: (10000, 11)
    


```python
# Dealing with missing values
# For our case, we will drop the rows with missing values
walmart_df.dropna(inplace=True)

# Verify removal of missing values
print('Missing values after removal:\n', walmart_df.isnull().sum())

print('\n')

# Final shape and structure of the cleaned dataframe
print(walmart_df.info())

print('\n')

print('Final shape of the dataframe:', walmart_df.shape)

```

    Missing values after removal:
     invoice_id        0
    Branch            0
    City              0
    category          0
    unit_price        0
    quantity          0
    date              0
    time              0
    payment_method    0
    rating            0
    profit_margin     0
    dtype: int64
    
    
    <class 'pandas.core.frame.DataFrame'>
    Index: 9969 entries, 0 to 9999
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   invoice_id      9969 non-null   int64  
     1   Branch          9969 non-null   object 
     2   City            9969 non-null   object 
     3   category        9969 non-null   object 
     4   unit_price      9969 non-null   object 
     5   quantity        9969 non-null   float64
     6   date            9969 non-null   object 
     7   time            9969 non-null   object 
     8   payment_method  9969 non-null   object 
     9   rating          9969 non-null   float64
     10  profit_margin   9969 non-null   float64
    dtypes: float64(3), int64(1), object(7)
    memory usage: 934.6+ KB
    None
    
    
    Final shape of the dataframe: (9969, 11)
    


```python
# If we check the data again, we can see that the unit_price column has object data type which is not correct as it should be float.
print(walmart_df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 9969 entries, 0 to 9999
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   invoice_id      9969 non-null   int64  
     1   Branch          9969 non-null   object 
     2   City            9969 non-null   object 
     3   category        9969 non-null   object 
     4   unit_price      9969 non-null   object 
     5   quantity        9969 non-null   float64
     6   date            9969 non-null   object 
     7   time            9969 non-null   object 
     8   payment_method  9969 non-null   object 
     9   rating          9969 non-null   float64
     10  profit_margin   9969 non-null   float64
    dtypes: float64(3), int64(1), object(7)
    memory usage: 934.6+ KB
    None
    


```python
# Therefore, we need to convert the unit price column to float data type. 
# The presence of $ sign does not allow us to convert the column directly to float. Hence, we will first remove the $ sign from the column and then convert it to float.
walmart_df['unit_price'] = walmart_df['unit_price'].str.replace('$', '').astype(float)

# Verify the data type conversion
print(walmart_df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 9969 entries, 0 to 9999
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   invoice_id      9969 non-null   int64  
     1   Branch          9969 non-null   object 
     2   City            9969 non-null   object 
     3   category        9969 non-null   object 
     4   unit_price      9969 non-null   float64
     5   quantity        9969 non-null   float64
     6   date            9969 non-null   object 
     7   time            9969 non-null   object 
     8   payment_method  9969 non-null   object 
     9   rating          9969 non-null   float64
     10  profit_margin   9969 non-null   float64
    dtypes: float64(4), int64(1), object(6)
    memory usage: 934.6+ KB
    None
    


```python
# We also need to convert the date and time columns to a date data type.
walmart_df['date'] = pd.to_datetime(walmart_df['date'])
walmart_df['time'] = pd.to_datetime(walmart_df['time'], format='%H:%M:%S').dt.time

# Verify the date data type conversion
print(walmart_df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 9969 entries, 0 to 9999
    Data columns (total 11 columns):
     #   Column          Non-Null Count  Dtype         
    ---  ------          --------------  -----         
     0   invoice_id      9969 non-null   int64         
     1   Branch          9969 non-null   object        
     2   City            9969 non-null   object        
     3   category        9969 non-null   object        
     4   unit_price      9969 non-null   float64       
     5   quantity        9969 non-null   float64       
     6   date            9969 non-null   datetime64[ns]
     7   time            9969 non-null   object        
     8   payment_method  9969 non-null   object        
     9   rating          9969 non-null   float64       
     10  profit_margin   9969 non-null   float64       
    dtypes: datetime64[ns](1), float64(4), int64(1), object(5)
    memory usage: 934.6+ KB
    None
  
```python
# Check the first few rows of the cleaned dataframe
walmart_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>invoice_id</th>
      <th>Branch</th>
      <th>City</th>
      <th>category</th>
      <th>unit_price</th>
      <th>quantity</th>
      <th>date</th>
      <th>time</th>
      <th>payment_method</th>
      <th>rating</th>
      <th>profit_margin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>WALM003</td>
      <td>San Antonio</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7.0</td>
      <td>2019-05-01</td>
      <td>13:08:00</td>
      <td>Ewallet</td>
      <td>9.1</td>
      <td>0.48</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>WALM048</td>
      <td>Harlingen</td>
      <td>Electronic accessories</td>
      <td>15.28</td>
      <td>5.0</td>
      <td>2019-08-03</td>
      <td>10:29:00</td>
      <td>Cash</td>
      <td>9.6</td>
      <td>0.48</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>WALM067</td>
      <td>Haltom City</td>
      <td>Home and lifestyle</td>
      <td>46.33</td>
      <td>7.0</td>
      <td>2019-03-03</td>
      <td>13:23:00</td>
      <td>Credit card</td>
      <td>7.4</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>WALM064</td>
      <td>Bedford</td>
      <td>Health and beauty</td>
      <td>58.22</td>
      <td>8.0</td>
      <td>2019-01-27</td>
      <td>20:33:00</td>
      <td>Ewallet</td>
      <td>8.4</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>WALM013</td>
      <td>Irving</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7.0</td>
      <td>2019-08-02</td>
      <td>10:37:00</td>
      <td>Ewallet</td>
      <td>5.3</td>
      <td>0.48</td>
    </tr>
  </tbody>
</table>

```python
# Now that the unit_price column is in the correct format, we can proceed further with our transformations.
# We will create a new column, total_sales, which will be the product of quantity and unit_price columns.
walmart_df['total_sales'] = walmart_df['quantity'] * walmart_df['unit_price']

# We will also rename the column `Branch` to `branch` and `City` to `city` for consistency.
walmart_df.rename(columns={'Branch': 'branch', 'City': 'city'}, inplace=True)
```


```python
# The dataframe is now cleaned and ready for further analysis.
walmart_df.head(10)
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>invoice_id</th>
      <th>branch</th>
      <th>city</th>
      <th>category</th>
      <th>unit_price</th>
      <th>quantity</th>
      <th>date</th>
      <th>time</th>
      <th>payment_method</th>
      <th>rating</th>
      <th>profit_margin</th>
      <th>total_sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>WALM003</td>
      <td>San Antonio</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7.0</td>
      <td>2019-05-01</td>
      <td>13:08:00</td>
      <td>Ewallet</td>
      <td>9.1</td>
      <td>0.48</td>
      <td>522.83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>WALM048</td>
      <td>Harlingen</td>
      <td>Electronic accessories</td>
      <td>15.28</td>
      <td>5.0</td>
      <td>2019-08-03</td>
      <td>10:29:00</td>
      <td>Cash</td>
      <td>9.6</td>
      <td>0.48</td>
      <td>76.40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>WALM067</td>
      <td>Haltom City</td>
      <td>Home and lifestyle</td>
      <td>46.33</td>
      <td>7.0</td>
      <td>2019-03-03</td>
      <td>13:23:00</td>
      <td>Credit card</td>
      <td>7.4</td>
      <td>0.33</td>
      <td>324.31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>WALM064</td>
      <td>Bedford</td>
      <td>Health and beauty</td>
      <td>58.22</td>
      <td>8.0</td>
      <td>2019-01-27</td>
      <td>20:33:00</td>
      <td>Ewallet</td>
      <td>8.4</td>
      <td>0.33</td>
      <td>465.76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>WALM013</td>
      <td>Irving</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7.0</td>
      <td>2019-08-02</td>
      <td>10:37:00</td>
      <td>Ewallet</td>
      <td>5.3</td>
      <td>0.48</td>
      <td>604.17</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>WALM026</td>
      <td>Denton</td>
      <td>Electronic accessories</td>
      <td>85.39</td>
      <td>7.0</td>
      <td>2019-03-25</td>
      <td>18:30:00</td>
      <td>Ewallet</td>
      <td>4.1</td>
      <td>0.48</td>
      <td>597.73</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>WALM088</td>
      <td>Cleburne</td>
      <td>Electronic accessories</td>
      <td>68.84</td>
      <td>6.0</td>
      <td>2019-02-25</td>
      <td>14:36:00</td>
      <td>Ewallet</td>
      <td>5.8</td>
      <td>0.33</td>
      <td>413.04</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>WALM100</td>
      <td>Canyon</td>
      <td>Home and lifestyle</td>
      <td>73.56</td>
      <td>10.0</td>
      <td>2019-02-24</td>
      <td>11:38:00</td>
      <td>Ewallet</td>
      <td>8.0</td>
      <td>0.18</td>
      <td>735.60</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>WALM066</td>
      <td>Grapevine</td>
      <td>Health and beauty</td>
      <td>36.26</td>
      <td>2.0</td>
      <td>2019-10-01</td>
      <td>17:15:00</td>
      <td>Credit card</td>
      <td>7.2</td>
      <td>0.33</td>
      <td>72.52</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>WALM065</td>
      <td>Texas City</td>
      <td>Food and beverages</td>
      <td>54.84</td>
      <td>3.0</td>
      <td>2019-02-20</td>
      <td>13:27:00</td>
      <td>Credit card</td>
      <td>5.9</td>
      <td>0.33</td>
      <td>164.52</td>
    </tr>
  </tbody>
</table>


**Connecting to SQL Server & Initializing Database**


```python
# Now we will create a connection to the SQL Server, create a new database and store the cleaned dataframe into a new table in that database.
# Define the connection parameters
server = 'ANHADSLAPTOP\\SQLEXPRESS'
driver = 'ODBC Driver 17 for SQL Server'
Trusted_Connection = 'yes'
TrustServerCertificate = 'yes'

# Close existing connection if any
if 'sql_connection' in locals():
    sql_connection.close()

# Create new connection to master database with autocommit
connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE=master;Trusted_Connection={Trusted_Connection};TrustServerCertificate={TrustServerCertificate}'
sql_connection = pyodbc.connect(connection_string, autocommit=True)
cursor = sql_connection.cursor()

```


```python
# Define and execute the database creation query
query = """
IF DB_ID('walmart_db') IS NOT NULL
BEGIN
    ALTER DATABASE walmart_db SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE walmart_db;
END;

CREATE DATABASE walmart_db;
"""

cursor.execute(query)
```




    <pyodbc.Cursor at 0x1b94d46c330>




```python
# Now let's connect to the newly created database
sql_connection.close()
connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE=walmart_db;Trusted_Connection={Trusted_Connection};TrustServerCertificate={TrustServerCertificate}'
sql_connection = pyodbc.connect(connection_string, autocommit=True)
driver_encoded = 'ODBC+Driver+17+for+SQL+Server'

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine(
    f"mssql+pyodbc://@{server}/walmart_db?driver={driver_encoded}&trusted_connection=yes&TrustServerCertificate=yes"
)

try:
    # Store the cleaned dataframe into a new table in the database
    walmart_df.to_sql('walmart_sales', con=engine, if_exists='replace', index=False)
    print("DataFrame successfully stored in the database table 'walmart_sales'.")
except:
    print("An error occurred while storing the DataFrame in the database.")
```

    DataFrame successfully stored in the database table 'walmart_sales'.
    


```python
# Let's create a function that takes a SQL query as input and returns the result as a pandas dataframe.
def execute_query(query):
    start = time.time()
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df_result = pd.DataFrame(result.fetchall(), columns=result.keys())
    print(f"Query executed in {time.time() - start:.3f} seconds.")
    return df_result
```

**Preliminary Analysis & Data Exploration**


```python
# Test the data query 
query1 = \
"   SELECT TOP 5 *              \
    FROM dbo.walmart_sales      \
    WHERE total_sales > 500     "
execute_query(query1)
```

    Query executed in 0.022 seconds.
    
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>invoice_id</th>
      <th>branch</th>
      <th>city</th>
      <th>category</th>
      <th>unit_price</th>
      <th>quantity</th>
      <th>date</th>
      <th>time</th>
      <th>payment_method</th>
      <th>rating</th>
      <th>profit_margin</th>
      <th>total_sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>WALM003</td>
      <td>San Antonio</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7.0</td>
      <td>2019-05-01</td>
      <td>13:08:00</td>
      <td>Ewallet</td>
      <td>9.1</td>
      <td>0.48</td>
      <td>522.83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>WALM013</td>
      <td>Irving</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7.0</td>
      <td>2019-08-02</td>
      <td>10:37:00</td>
      <td>Ewallet</td>
      <td>5.3</td>
      <td>0.48</td>
      <td>604.17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>WALM026</td>
      <td>Denton</td>
      <td>Electronic accessories</td>
      <td>85.39</td>
      <td>7.0</td>
      <td>2019-03-25</td>
      <td>18:30:00</td>
      <td>Ewallet</td>
      <td>4.1</td>
      <td>0.48</td>
      <td>597.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>WALM100</td>
      <td>Canyon</td>
      <td>Home and lifestyle</td>
      <td>73.56</td>
      <td>10.0</td>
      <td>2019-02-24</td>
      <td>11:38:00</td>
      <td>Ewallet</td>
      <td>8.0</td>
      <td>0.18</td>
      <td>735.60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15</td>
      <td>WALM031</td>
      <td>Lewisville</td>
      <td>Health and beauty</td>
      <td>71.38</td>
      <td>10.0</td>
      <td>2019-03-29</td>
      <td>19:21:00</td>
      <td>Cash</td>
      <td>5.7</td>
      <td>0.48</td>
      <td>713.80</td>
    </tr>
  </tbody>
</table>

```python
# Get the total number of records in the walmart_sales table
query2 = \
"   SELECT COUNT(*) AS total_records    \
    FROM dbo.walmart_sales               "
execute_query(query2)
```
    Query executed in 0.006 seconds.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_records</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9969</td>
    </tr>
  </tbody>
</table>



```python
# Get the number of distinct stores
query3 = \
"   SELECT COUNT(DISTINCT branch) AS total_records               \
    FROM dbo.walmart_sales                                       "
execute_query(query3)
```

    Query executed in 0.060 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_records</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
    </tr>
  </tbody>
</table>



```python
# Get the maximum and minimum sales overall
query4 = \
"   SELECT                                                        \
        MAX(total_sales) AS max_sale_amount,                      \
        MIN(total_sales) AS min_sale_amount                       \
    FROM dbo.walmart_sales                                        "
execute_query(query4)
```

    Query executed in 0.008 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>max_sale_amount</th>
      <th>min_sale_amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>993.0</td>
      <td>10.17</td>
    </tr>
  </tbody>
</table>

```python
# Get payment method-wise total sales, total quantity sold, and count of payments
query5 = \
"   SELECT                                              \
        payment_method,                                 \
        COUNT(*) AS count_payments,                     \
        SUM(total_sales) AS tot_sales,                  \
        CAST(SUM(quantity) AS INT) AS tot_quantity      \
    FROM dbo.walmart_sales                              \
    GROUP BY payment_method                             "
execute_query(query5)
```

    Query executed in 0.052 seconds.
    

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>payment_method</th>
      <th>count_payments</th>
      <th>tot_sales</th>
      <th>tot_quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Credit card</td>
      <td>4256</td>
      <td>488821.02</td>
      <td>9567</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cash</td>
      <td>1832</td>
      <td>263589.29</td>
      <td>4984</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ewallet</td>
      <td>3881</td>
      <td>457316.07</td>
      <td>8932</td>
    </tr>
  </tbody>
</table>


**Analytics Using Advanced SQL Concepts**

```python
# Get 10 top-rated branches based on the average customer ratings on each category within the branch
query6 = \
"   WITH cat_rank AS                                                                            \
    (                                                                                           \
    SELECT                                                                                      \
        branch,                                                                                 \
        category,                                                                               \
        ROUND(AVG(rating), 2) AS avg_rating,                                                    \
        ROW_NUMBER() OVER(PARTITION BY branch ORDER BY AVG(rating) DESC) AS rank_category       \
    FROM dbo.walmart_sales                                                                      \
    GROUP BY                                                                                    \
        branch,                                                                                 \
        category                                                                                \
    )                                                                                           \
    SELECT TOP 10                                                                               \
        cr.branch,                                                                              \
        cr.category,                                                                            \
        cr.avg_rating                                                                           \
    FROM cat_rank cr                                                                            \
    WHERE rank_category = 1                                                                     \
    ORDER BY cr.avg_rating DESC                                                                 "
execute_query(query6)
```

    Query executed in 0.113 seconds.
    
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>branch</th>
      <th>category</th>
      <th>avg_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WALM034</td>
      <td>Health and beauty</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WALM060</td>
      <td>Health and beauty</td>
      <td>9.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WALM086</td>
      <td>Health and beauty</td>
      <td>9.9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WALM098</td>
      <td>Health and beauty</td>
      <td>9.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WALM027</td>
      <td>Health and beauty</td>
      <td>9.7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>WALM067</td>
      <td>Sports and travel</td>
      <td>9.7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>WALM068</td>
      <td>Electronic accessories</td>
      <td>9.7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>WALM009</td>
      <td>Sports and travel</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>WALM048</td>
      <td>Electronic accessories</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>WALM073</td>
      <td>Food and beverages</td>
      <td>9.6</td>
    </tr>
  </tbody>
</table>



```python
# Get the top-rated category for each branch based on average customer ratings
query7 = \
"   WITH cat_rank AS (                                            \
        SELECT                                                    \
            branch,                                               \
            category,                                             \
            ROUND(AVG(rating), 2) AS avg_rating,                  \
            ROW_NUMBER() OVER(PARTITION BY branch ORDER BY AVG(rating) DESC) AS rank_category \
        FROM walmart_sales                                        \
        GROUP BY branch, category                                 \
    )                                                             \
    SELECT                                                        \
        cr.branch, cr.category, cr.avg_rating                     \
    FROM cat_rank cr                                              \
    WHERE rank_category = 1                                       "
execute_query(query7)
```

    Query executed in 0.068 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>branch</th>
      <th>category</th>
      <th>avg_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WALM001</td>
      <td>Electronic accessories</td>
      <td>7.45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WALM002</td>
      <td>Food and beverages</td>
      <td>8.25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WALM003</td>
      <td>Sports and travel</td>
      <td>7.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WALM004</td>
      <td>Food and beverages</td>
      <td>9.30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WALM005</td>
      <td>Health and beauty</td>
      <td>8.37</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>WALM096</td>
      <td>Sports and travel</td>
      <td>9.60</td>
    </tr>
    <tr>
      <th>96</th>
      <td>WALM097</td>
      <td>Food and beverages</td>
      <td>7.67</td>
    </tr>
    <tr>
      <th>97</th>
      <td>WALM098</td>
      <td>Health and beauty</td>
      <td>9.80</td>
    </tr>
    <tr>
      <th>98</th>
      <td>WALM099</td>
      <td>Electronic accessories</td>
      <td>5.95</td>
    </tr>
    <tr>
      <th>99</th>
      <td>WALM100</td>
      <td>Health and beauty</td>
      <td>6.90</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 3 columns</p>



```python
# Get the day with the highest number of transactions for each branch
query8 = \
"   WITH per_day_trans AS (                                       \
        SELECT                                                    \
            ws.branch,                                            \
            CAST(ws.date AS DATE) AS date_sale,                   \
            FORMAT(ws.date,'dddd') AS day_name,                   \
            COUNT(*) AS tot_transactions,                         \
            ROW_NUMBER() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS rank_trans \
        FROM dbo.walmart_sales ws                                 \
        GROUP BY ws.branch, ws.date                               \
    )                                                             \
    SELECT                                                        \
        pdt.branch, pdt.date_sale, pdt.day_name, pdt.tot_transactions \
    FROM per_day_trans pdt                                        \
    WHERE rank_trans = 1                                          "
execute_query(query8)
```

    Query executed in 0.057 seconds.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>branch</th>
      <th>date_sale</th>
      <th>day_name</th>
      <th>tot_transactions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WALM001</td>
      <td>2019-03-22</td>
      <td>Friday</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WALM002</td>
      <td>2023-12-10</td>
      <td>Sunday</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WALM003</td>
      <td>2020-11-27</td>
      <td>Friday</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WALM004</td>
      <td>2021-07-08</td>
      <td>Thursday</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WALM005</td>
      <td>2023-08-30</td>
      <td>Wednesday</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>WALM096</td>
      <td>2022-12-26</td>
      <td>Monday</td>
      <td>2</td>
    </tr>
    <tr>
      <th>96</th>
      <td>WALM097</td>
      <td>2022-08-29</td>
      <td>Monday</td>
      <td>2</td>
    </tr>
    <tr>
      <th>97</th>
      <td>WALM098</td>
      <td>2022-12-18</td>
      <td>Sunday</td>
      <td>2</td>
    </tr>
    <tr>
      <th>98</th>
      <td>WALM099</td>
      <td>2021-12-23</td>
      <td>Thursday</td>
      <td>3</td>
    </tr>
    <tr>
      <th>99</th>
      <td>WALM100</td>
      <td>2019-02-24</td>
      <td>Sunday</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
</div>




```python
# Get the city and category-wise maximum, minimum, and average customer ratings
query9 = \
"   SELECT                                                        \
        city,                                                     \
        category,                                                 \
        MAX(rating) AS max_rat,                                   \
        MIN(rating) AS min_rat,                                   \
        ROUND(AVG(rating), 1) AS avg_rat                          \
    FROM dbo.walmart_sales                                        \
    GROUP BY city, category                                       \
    ORDER BY city, category                                       "
execute_query(query9)

```

    Query executed in 0.097 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>category</th>
      <th>max_rat</th>
      <th>min_rat</th>
      <th>avg_rat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Abilene</td>
      <td>Electronic accessories</td>
      <td>8.8</td>
      <td>7.1</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Abilene</td>
      <td>Fashion accessories</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>6.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Abilene</td>
      <td>Food and beverages</td>
      <td>8.9</td>
      <td>6.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Abilene</td>
      <td>Health and beauty</td>
      <td>9.7</td>
      <td>9.7</td>
      <td>9.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Abilene</td>
      <td>Home and lifestyle</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>6.1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>508</th>
      <td>Weslaco</td>
      <td>Fashion accessories</td>
      <td>9.5</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>509</th>
      <td>Weslaco</td>
      <td>Food and beverages</td>
      <td>9.8</td>
      <td>7.1</td>
      <td>8.7</td>
    </tr>
    <tr>
      <th>510</th>
      <td>Weslaco</td>
      <td>Health and beauty</td>
      <td>9.2</td>
      <td>4.3</td>
      <td>6.8</td>
    </tr>
    <tr>
      <th>511</th>
      <td>Weslaco</td>
      <td>Home and lifestyle</td>
      <td>9.2</td>
      <td>3.0</td>
      <td>5.2</td>
    </tr>
    <tr>
      <th>512</th>
      <td>Weslaco</td>
      <td>Sports and travel</td>
      <td>7.1</td>
      <td>4.1</td>
      <td>5.6</td>
    </tr>
  </tbody>
</table>
<p>513 rows × 5 columns</p>



```python
# Get the category-wise total sales and total profit, ordered by total profit in descending order
query10 = \
"   SELECT                                                        \
        fsq.category,                                             \
        ROUND(SUM(fsq.total_sales), 2) AS tot_sales,              \
        ROUND(SUM(fsq.profit_of_all_sales), 2) AS tot_profit      \
    FROM (                                                        \
        SELECT                                                    \
            category,                                             \
            total_sales,                                          \
            total_sales * profit_margin AS profit_of_all_sales    \
        FROM dbo.walmart_sales                                    \
    ) AS fsq                                                      \
    GROUP BY fsq.category                                         \
    ORDER BY tot_profit DESC                                      "
execute_query(query10)
```

    Query executed in 0.014 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>tot_sales</th>
      <th>tot_profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Fashion accessories</td>
      <td>489480.90</td>
      <td>192314.89</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Home and lifestyle</td>
      <td>489250.06</td>
      <td>192213.64</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Electronic accessories</td>
      <td>78175.03</td>
      <td>30772.49</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Food and beverages</td>
      <td>53471.28</td>
      <td>21552.86</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sports and travel</td>
      <td>52497.93</td>
      <td>20613.81</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Health and beauty</td>
      <td>46851.18</td>
      <td>18671.73</td>
    </tr>
  </tbody>
</table>



```python
# Get the most popular payment method for each branch
query11 = \
"   SELECT                                                        \
        fsq.branch, fsq.payment_method                            \
    FROM (                                                        \
        SELECT                                                    \
            branch, payment_method,                               \
            COUNT(*) AS total_transactions,                       \
            ROW_NUMBER() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS transaction_rank \
        FROM dbo.walmart_sales                                    \
        GROUP BY branch, payment_method                           \
    ) AS fsq                                                      \
    WHERE fsq.transaction_rank = 1                                \
    ORDER BY fsq.branch                                           "
execute_query(query11)
```

    Query executed in 0.057 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>branch</th>
      <th>payment_method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WALM001</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WALM002</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WALM003</td>
      <td>Credit card</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WALM004</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WALM005</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>WALM096</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>96</th>
      <td>WALM097</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>97</th>
      <td>WALM098</td>
      <td>Ewallet</td>
    </tr>
    <tr>
      <th>98</th>
      <td>WALM099</td>
      <td>Credit card</td>
    </tr>
    <tr>
      <th>99</th>
      <td>WALM100</td>
      <td>Ewallet</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 2 columns</p>



```python
# Get the distribution of sales transactions across different times of the day
query12 = \
"   WITH categorized_sales AS (                                   \
        SELECT *,                                                 \
            CASE                                                  \
                WHEN time >= '00:00:00' AND time < '12:00:00' THEN 'Morning' \
                WHEN time < '17:00:00' THEN 'Afternoon'           \
                ELSE 'Night'                                      \
            END AS sale_time_category                             \
        FROM dbo.walmart_sales ws                                 \
    )                                                             \
    SELECT                                                        \
        cs.sale_time_category, COUNT(*) AS total_transactions     \
    FROM categorized_sales cs                                     \
    GROUP BY cs.sale_time_category                                \
    ORDER BY total_transactions DESC                              "
execute_query(query12)
```

    Query executed in 0.022 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sale_time_category</th>
      <th>total_transactions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Night</td>
      <td>4273</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afternoon</td>
      <td>3609</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Morning</td>
      <td>2087</td>
    </tr>
  </tbody>
</table>


```python
# Identify bottom 5 branches based on Year-over-Year (YoY) percentage change in total sales from 2022 to 2023
query13 = \
"   WITH yoy_analysis AS (                                        \
        SELECT                                                    \
            branch,                                               \
            YEAR(date) AS year_of_sale,                           \
            ROUND(SUM(total_sales), 2) AS tot_sales,              \
            LAG(ROUND(SUM(total_sales), 2)) OVER(PARTITION BY branch ORDER BY YEAR(date)) AS prev_tot_sales \
        FROM dbo.walmart_sales                                    \
        WHERE YEAR(date) IN (2022, 2023)                          \
        GROUP BY branch, YEAR(date)                               \
    )                                                             \
    SELECT TOP 5                                                  \
        ya.branch, ya.tot_sales, ya.prev_tot_sales,               \
        ROUND(((ya.tot_sales - ya.prev_tot_sales)/ya.prev_tot_sales) * 100, 2) AS perc_change \
    FROM yoy_analysis ya                                          \
    WHERE ya.prev_tot_sales IS NOT NULL                           \
    ORDER BY perc_change                                          "
execute_query(query13)
```

    Query executed in 0.028 seconds.
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>branch</th>
      <th>tot_sales</th>
      <th>prev_tot_sales</th>
      <th>perc_change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WALM045</td>
      <td>647.0</td>
      <td>1731.0</td>
      <td>-62.62</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WALM047</td>
      <td>1069.0</td>
      <td>2581.0</td>
      <td>-58.58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WALM098</td>
      <td>1030.0</td>
      <td>2446.0</td>
      <td>-57.89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WALM033</td>
      <td>931.0</td>
      <td>2099.0</td>
      <td>-55.65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WALM081</td>
      <td>850.0</td>
      <td>1723.0</td>
      <td>-50.67</td>
    </tr>
  </tbody>
</table>

