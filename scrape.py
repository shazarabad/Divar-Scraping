from bs4 import BeautifulSoup
import requests

from selenium import webdriver
import time
import pandas as pd

from smallData1 import scrape_divar_info
from smallData2 import scrape_data1

# Create empty lists to store scraped data
prices = []
locations = []
links = []
m2s = []
years = []
roomss = []
elevator=[]
parking=[]
warehouse=[]


# Initialize Chrome webdriver
driver = webdriver.Chrome()

base_url = 'https://divar.ir/s/tehran/buy-apartment'
page_number = 1
rows_scraped = 0  # Counter to track the number of rows scraped

while rows_scraped < 3000:

    url = f'{base_url}?page={page_number}'
    driver.get(url)
    time.sleep(10)  # Allow time for the page to load

    # Scroll down to load more content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*2);")
    time.sleep(10)  # Allow time for the content to load

    # Get the HTML content after scrolling
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, 'html.parser')
    houses = soup.find_all('div', class_='post-list__widget-col-c1444')

    if not houses:
        break

    for house in houses:
        try:
            price = house.find('div', class_='kt-post-card__description').text.replace(' ', '')
        except AttributeError:
            price = 'N/A'

        try:
            location = house.find('span', class_='kt-post-card__bottom-description kt-text-truncate').text.split()[-1].replace(' ', '')
        except AttributeError:
            location = 'N/A'

        try:
            link =""
            link = house.find('a').get("href").replace(' ', '')
            link = "https://divar.ir" + link
            #response2 = requests.get(link)\
            print(link)
            time.sleep(10)
            data=scrape_divar_info(link)
            time.sleep(10)
            data2=scrape_data1(link)


            #td_elements = soup2.find_all("td", class_="kt-group-row-item kt-group-row-item__value kt-group-row-item--info-row")
            #m2 = 'N/A'
            #year = 'N/A'
            #rooms = 'N/A'

            #if len(td_elements) >= 3:
                #m2 = td_elements[0].text.strip()
                #year = td_elements[1].text.strip()
                #rooms = td_elements[2].text.strip()
                #print(soup2)


                
            #else:
                #print(soup2)
                #print(td_elements)
                #print("Not enough td elements found.")
                    
        except AttributeError:
            link = 'N/A'

        


        # Append scraped data to lists
        prices.append(price)
        locations.append(location)
        links.append(link)
        m2s.append(data[0])
        years.append(data[1])
        roomss.append(data[2])
        elevator.append(data2[0])
        parking.append(data2[1])
        warehouse.append(data2[2])
        print(rows_scraped)

        rows_scraped += 1  # Increment the counter

        if rows_scraped >= 3000:
            break  # Exit the loop once 100 rows are scraped

    page_number += 1
    

# Close the webdriver
driver.quit()

# Create a DataFrame from the lists
data = {
    'Price': prices,
    'Location': locations,
    'Link': links,
    'M2': m2s,
    'Rooms': roomss,
    'Year': years,
    'Elevator': elevator,
    'Parking': parking,
    'Warehouse': warehouse,

}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('scrape3.xlsx', index=False)


#kt-group-row-item kt-group-row-item__value kt-body kt-body--stable kt-group-row-item--disabled
#kt-group-row-item kt-group-row-item__value kt-group-row-item--info-row
