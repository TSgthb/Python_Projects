# This script scrapes the data from a fictitious e-commerce store website that has been created using HTML.
# We have used LiveServer extension in VSCode to generate the webpage using the HTML file.

# Importing required libraries
from bs4 import BeautifulSoup
import csv
import pandas as pd

# This is the path of the HTML webpage.
html_path = "C:\\Users\\Admin\\Documents\\OneDrive\\Desktop\\Python\\Scrapping Projects\\Scrapping E-Commerce Site\\Scripts\\apple_store.html"

# Since this is a file itself, hence we can simply open and access the elements within it. In real scenerio, we would need to send
# a request to the website and fetch this HTML data.
with open(html_path, 'r' , encoding = 'utf-8' ) as html_file:
    html_content = html_file.read()

# Convert the HTML object into soup object
soup = BeautifulSoup(html_content, 'html.parser')

# Getting the website title
website_header = soup.find('h1').text.strip()

# Getting all the products' details from the website
products = soup.find_all('div', attrs = {'class' : 'product'})

# Initialize a file for saving scrapped data
with open('apple_scrapped_data.csv', 'w', encoding = 'utf-8' ) as file_csv:
    # Initializing a CSV writer
    writer = csv.writer(file_csv)
    
    # Initializing headers for the file
    writer.writerow(['product_name','product_price','product_stock','product_rating','product_shipping'])

    # Looping through all products
    for prod in products:
        
        # Getting products' names
        product_name = prod.find('h3').text
        
        # Getting products' details using `p` tag
        product_details = prod.find_all('p')

        # Getting products' price from `product_details`
        product_price = product_details[0].text.replace('Price: ', '')

        # Getting products' available quantity from `product_details`
        product_stock = product_details[1].text.replace('Quantity Available: ','')

        # Getting products' rating
        product_rating = prod.find('p', attrs = {'class' : 'rating'}).text
        
        # Getting shipping information of products
        product_shipping = product_details[-1].text.replace('Estimated Shipping: ', '')
        
        # Writing extracted data of a product to the CSV
        writer.writerow([product_name, product_price, product_stock, product_rating, product_shipping])

print('Data has been scrapped successfully.')

# Read the new file as a pandas DataFrame and print it
file_csv_read = pd.read_csv('apple_scrapped_data.csv' , encoding = 'utf-8')
file_df = pd.DataFrame(file_csv_read)
print(file_df)
