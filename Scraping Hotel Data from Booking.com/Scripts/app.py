import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
import time

website_url = "https://www.booking.com/searchresults.html?ss=Man%C4%81li%2C+Himachal+Pradesh%2C+India&efdco=1&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AouYhckGwAIB0gIkZmZkMzMyNTMtYzgwYS00YzNjLWJhMzMtMjUyZjNiNTMwMzJj2AIB4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2103603&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xu&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=5cb727852c7601ac&ac_meta=GhA1Y2I3Mjc4NTJjNzYwMWFjIAAoATICeHU6BE1hbmE%3D&checkin=2025-11-29&checkout=2025-12-01&group_adults=2&no_rooms=1&group_children=0"
file_name = 'C:\\Users\\tejvesin\\OneDrive - Capgemini\\Desktop\\Personal\\Python\\Projects\\Web Scrapping\\Booking.com Data Scraping\\Datasets\\Booking.com_scraped.csv'

user_input_url = input('Enter the link for the website to scrape: ')
user_input_file_name = input('Enter the file path (with the file name) to save scraped data: ')

if user_input_url in ['',' ',0,'No'] and user_input_file_name in ['',' ',0,'No']:
    user_input_url = website_url
    user_input_file_name = file_name

def web_scraper(website_link, file_to_save):

    custom_headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36" ,
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(website_link , headers = custom_headers)

    connection_established = False
    tries = 1

    while connection_established != True and tries < 5:
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

    if response.status_code == 200:
        print("Successfully accessed the page.")

        html_content = response.text
        soup = BeautifulSoup(html_content,'lxml')
        
        hotels_container = soup.find_all('div', attrs = {'role' : 'listitem'})

        with open(file_to_save, mode = 'w', encoding = 'utf-8') as scraped_file:
            writer = csv.writer(scraped_file)
            writer.writerow(['name','location','price(in ₹)','rating','score','total_reviews','link'])

            for hotel in hotels_container:
            
                hotel_name = hotel.find('div', attrs = {'class' : 'b87c397a13 a3e0b4ffd1'}).text.strip()
                location = hotel.find('span', attrs = {'class' : 'd823fbbeed f9b3563dd4'}).text.strip().replace('ManÄli','Manali')
                price = int(hotel.find('span', class_ = 'b87c397a13 f2f358d1de ab607752a2').text.strip().replace('â¹Â ','').replace(',',''))
                rating = hotel.find('div', class_ = 'f63b14ab7a f546354b44 becbee2f63').text.strip()
                score = hotel.find('div', class_ = 'f63b14ab7a dff2e52086').text.strip()
                tot_reviews = hotel.find('div', class_ = 'fff1944c52 fb14de7f14 eaa8455879').text.strip()
                hotel_link = hotel.find('a', attrs = {'href' : True}).get('href')

                writer.writerow([hotel_name,location,price,rating,score,tot_reviews,hotel_link])
            
        read_file = pd.read_csv(file_to_save, encoding = 'utf-8')
        file_df = pd.DataFrame(read_file)
        print(file_df)
        return None

    else:
        print(f"Failed to access the page. Status code: {response.status_code if response else 'no response'}.")
        return None

web_scraper(user_input_url, user_input_file_name)

