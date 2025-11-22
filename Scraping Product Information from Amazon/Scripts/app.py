# This is a simple application to demonstrate web scraping from Amazon using BeautifulSoup.

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Defining the URL of the Amazon product page
url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJB8CW4/ref=sr_1_4?crid=24EOE2Z5JRDCH&dib=eyJ2IjoiMSJ9.FdEYEGrB--Vj-ui9YHu7vCeL9DJlNRdTwPeY2KKxdKNKFlUom0GhYPcC1GJ4-OUBk21JoJsn1JgnG9R9z_hyRoUIMZuMaEhBfBsONt0XdA9ySdY2fS2YUksU-NrGuY8oqSgaBNti8HRXcBEQfSihql3RAVfKhIrh4i7hIrFnilB_v8XavCrromxasgcVyU62G3M0WLLq3oSzEvCKI-JBcZ3Ritbmz2RMTuAK3VDwovo.Gs2spgZOgnSKbO4NDXdfeviKOhTAJIUVH2bnvEcMXwc&dib_tag=se&keywords=apple%2Bairpod%2Bmax&nsdOptOutParam=true&qid=1763529058&sprefix=Apple%2Bairpod%2Bma%2Caps%2C295&sr=8-4&th=1"

# Setting up headers to mimic a browser visit
custom_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
          }

# Sending a GET request to the URL
response = requests.get(url, headers = custom_headers)

# Print the status code of the response and store the html content as text
if response.status_code == 200:
    print("Successfully accessed the page.")
    html_content = response.text
else:
    print(f"Failed to access the page. Status code: {response.status_code}")

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')

# Extracting product information
product_title = soup.find('span', id = 'productTitle').text.strip()
product_price = soup.find('span', class_ = 'a-price-whole').text.strip()
product_rating = soup.find('span', id = 'acrPopover').text.strip()
product_about = soup.find('div', class_ = 'a-unordered-list a-vertical a-spacing-mini').text.strip()
product_description = soup.find('div', id = 'productDescription').text.strip()
product_reviews = soup.find('ul', id = 'cm-cr-dp-review-list').text.strip()

# Saving the data into a CSV file
filename = 'C:\\Users\\tejvesin\\OneDrive - Capgemini\\Desktop\\Personal\\Python\\Projects\\Web Scrapping\\Amazon Data Scrapping\\AmazonScrapped_AppleAirpodProMax.csv'
with open(filename, mode = 'w', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title", "product_description", "product_price", "product_rating", "product_about", "product_reviews"])
    writer.writerow([product_title, product_description, product_price, product_rating, product_about, product_reviews])

print(f'Data scrapped successfully at {filename}!')

read_file = pd.read_csv(filename, encoding = 'utf-8')
file_df = pd.DataFrame(read_file) 
print(file_df)
