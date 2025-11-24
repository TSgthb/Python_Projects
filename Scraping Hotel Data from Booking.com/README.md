
# Scraping Data from Booking.com

<p align="justify">
This project demonstrates scraping of hotel listing data from Booking.com using <code>Python</code>, <code>Requests</code>, and <code>BeautifulSoup</code>. It programmatically fetches the search results page and extracts structured information such as hotel name, location, price, rating, review score, total reviews, and booking link.
<p>

<p align="justify">
The script sends an HTTP request to the <b>Booking.com</b> search URL, parses relevant hotel attributes, saves them to a CSV file, and validates by loading the output into a <code>Pandas</code> DataFrame.
<p>

> <p align="justify"><i><b>Important!</b> Scraping commercial websites may violate terms of service and can fail due to frequent layout changes and anti-bot measures. Use this code for learning purposes, respect the site's robots.txt and policies, and consider official APIs where available.</i></p>

## Objectives
- Send an HTTP request to the Booking.com search results URL and retrieve HTML content.
- Parse and extract hotel details (name, location, price, rating, score, total reviews, link).
- Save the scraped data into a CSV dataset.
- Validate the dataset by loading it into a Pandas DataFrame and printing the results.

## Operations & Tasks

#### 1. Import Required Libraries
```python
import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
import time
```

#### 2. Define Default URL and File Path
```python
website_url = "https://www.booking.com/searchresults.html?...&checkin=2025-11-29&checkout=2025-12-01"
file_name = "C:\\Users\\...\\Booking.com_scraped.csv"
```

#### 3. Accept User Inputs with Fallback Defaults
```python
user_input_url = input("Enter the link for the website to scrape: ")
user_input_file_name = input("Enter the file path (with the file name) to save scraped data: ")

if user_input_url in ['', ' ', 0, 'No'] and user_input_file_name in ['', ' ', 0, 'No']:
    user_input_url = website_url
    user_input_file_name = file_name
```

#### 4. Send HTTP Request and Handle Status Codes

- Use custom headers to mimic a browser and reduce blocking.
- Implement retry logic for `202 Accepted` responses with incremental delays.
- Handle `403 Forbidden` and unexpected errors gracefully.

```python
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(website_link, headers=custom_headers)

if response.status_code == 202:
    print(f"Processing. Retrying in {3*tries} seconds.")
    time.sleep(3*tries)
    response = requests.get(website_url, headers = custom_headers)
    tries+=1
elif response.status_code == 403:
    print('Access forbidden (error:403). Likely anti-bot protection.')
    break
elif response.status_code == 200:
    connection_established = True
else:
    print(f'Stopping. Unexpected error (error:{response.status_code})')
```

#### 5. Parse HTML with BeautifulSoup
```python
soup = BeautifulSoup(response.text, 'lxml')
hotels_container = soup.find_all('div', attrs={'role': 'listitem'})
```

#### 6. Extract Hotel Attributes
- Hotel name
- Location
- Price (converted to integer)
- Rating
- Score
- Total reviews
- Booking link

```python
hotel_name = hotel.find('div', attrs = {'class' : 'b87c397a13 a3e0b4ffd1'}).text.strip()
location = hotel.find('span', attrs = {'class' : 'd823fbbeed f9b3563dd4'}).text.strip().replace('ManÄli','Manali')
price = int(hotel.find('span', class_ = 'b87c397a13 f2f358d1de ab607752a2').text.strip().replace('â¹Â ','').replace(',',''))
rating = hotel.find('div', class_ = 'f63b14ab7a f546354b44 becbee2f63').text.strip()
score = hotel.find('div', class_ = 'f63b14ab7a dff2e52086').text.strip()
tot_reviews = hotel.find('div', class_ = 'fff1944c52 fb14de7f14 eaa8455879').text.strip()
hotel_link = hotel.find('a', attrs = {'href' : True}).get('href')
```

#### 7. Save Data to CSV
```python
with open(file_to_save, mode='w', encoding='utf-8') as scraped_file:
    writer = csv.writer(scraped_file)
    writer.writerow(['name','location','price(in ₹)','rating','score','total_reviews','link'])
    # Write rows for each hotel
    for hotel in hotels_container:
        writer.writerow([hotel_name,location,price,rating,score,tot_reviews,hotel_link])
```

#### 8. Validate Output with Pandas
```python
read_file = pd.read_csv(file_to_save, encoding='utf-8')
file_df = pd.DataFrame(read_file)
print(file_df)
```
![image](TSgthb/Python_Projects/Scraping Hotel Data from Booking.com/Images/DataFrame_Booking.com.png)

## Conclusion
- Successfully fetched and parsed Booking.com search results to extract hotel details.
- Stored the output into a CSV file for portability and downstream analysis.
- Quick validation via Pandas confirmed the dataset is readable and structured.
- With robust error handling and dynamic selector management, this approach can be adapted to other destinations and integrated into ETL pipelines.