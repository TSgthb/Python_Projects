# Scraping Data from Amazon Product Page

<p align="justify">
This project demonstrates how to <b>scrape product data</b> from an Amazon product page using <b>Python</b> and <b>BeautifulSoup</b>. It programmatically fetches the page HTML and extracts structured information such as title, price, rating, description, and reviews.
</p>

<p align="justify">
The scraping script leverages <code>requests</code>, <code>BeautifulSoup</code>, <code>CSV</code>, and <code>Pandas</code> to retrieve the page, parse relevant product attributes, persist them to a CSV file, and validate by loading the output into a DataFrame.
</p>

> <p align="justify"><i><b>Important!</b> Scraping commercial websites may violate terms of service and can fail due to frequent layout changes and anti-bot measures. Use this code for learning purposes, respect the site's robots and policies, and consider official APIs where available.</i></p>

## Objectives
- Send an HTTP request to the Amazon product URL and retrieve HTML content.
- Parse and extract product details (title, price, rating, key points, description, reviews).
- Save the scraped data into a CSV dataset.
- Validate the dataset by loading it into a Pandas DataFrame and printing the results.

## Operations & Tasks

<p>
1. Import required Python libraries for HTTP, parsing, and data handling.
</p>

```python
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
```

<p>
2. Define the target Amazon product URL and set browser-like headers to avoid basic blocking.
</p>

```python
url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJB8CW4/ref=sr_1_4?crid=24EOE2Z5JRDCH&dib=eyJ2IjoiMSJ9.FdEYEGrB--Vj-ui9YHu7vCeL9DJlNRdTwPeY2KKxdKNKFlUom0GhYPcC1GJ4-OUBk21JoJsn1JgnG9R9z_hyRoUIMZuMaEhBfBsONt0XdA9ySdY2fS2YUksU-NrGuY8oqSgaBNti8HRXcBEQfSihql3RAVfKhIrh4i7hIrFnilB_v8XavCrromxasgcVyU62G3M0WLLq3oSzEvCKI-JBcZ3Ritbmz2RMTuAK3VDwovo.Gs2spgZOgnSKbO4NDXdfeviKOhTAJIUVH2bnvEcMXwc&dib_tag=se&keywords=apple%2Bairpod%2Bmax&nsdOptOutParam=true&qid=1763529058&sprefix=Apple%2Bairpod%2Bma%2Caps%2C295&sr=8-4&th=1"

custom_headers = 
{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
```

<p>
3. Send the GET request, check the HTTP status, and capture the HTML response.
</p>

```python
response = requests.get(url, headers=custom_headers)

if response.status_code == 200:
    print("Successfully accessed the page.")
    html_content = response.text
else:
    print(f"Failed to access the page. Status code: {response.status_code}")
```

<p>
4. Parse the HTML content using <code>BeautifulSoup</code> with the <code>lxml</code> parser.
</p>

```python
soup = BeautifulSoup(html_content, 'lxml')
```

<p>
5. Extract product attributes using appropriate selectors and clean text values.
</p>

```python
product_title = soup.find('span', id='productTitle').text.strip()
product_price = soup.find('span', class_='a-price-whole').text.strip()
product_rating = soup.find('span', id='acrPopover').text.strip()
product_about = soup.find('div', class_='a-unordered-list a-vertical a-spacing-mini').text.strip()
product_description = soup.find('div', id='productDescription').text.strip()
product_reviews = soup.find('ul', id='cm-cr-dp-review-list').text.strip()
```

<p>
6. Persist the extracted data into a structured CSV file.
</p>

```python
filename = 'C:\\Users\\tejvesin\\OneDrive - Capgemini\\Desktop\\Personal\\Python\\Projects\\Web Scrapping\\Amazon Data Scrapping\\AmazonScrapped_AppleAirpodProMax.csv'
with open(filename, mode='w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title", "product_description", "product_price", "product_rating", "product_about", "product_reviews"])
    writer.writerow([product_title, product_description, product_price, product_rating, product_about, product_reviews])

print(f'Data scrapped successfully at {filename}!')
```

<p>
7. Load the CSV file into a Pandas DataFrame and print the dataset for validation.
</p>

```python
read_file = pd.read_csv(filename, encoding='utf-8')
file_df = pd.DataFrame(read_file)
print(file_df)
```

## Conclusion
- Successfully fetched and parsed an Amazon product page to extract title, price, rating, description, key points, and reviews.
- Stored the output into a CSV file for portability and downstream analysis.
- Quick validation via Pandas confirmed the dataset is readable and structured.
- With robust error handling and dynamic selector management, this approach can be adapted to other product pages and integrated into ETL pipelines.
