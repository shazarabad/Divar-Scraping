import requests
from bs4 import BeautifulSoup
import time

def scrape_divar_info(url):
    data=[0,0,0]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            time.sleep(10)
            soup = BeautifulSoup(response.content, "html.parser")
            time.sleep(10)
            td_elements = soup.find_all("td", class_="kt-group-row-item kt-group-row-item__value kt-group-row-item--info-row")

            if len(td_elements) >= 3:
                data1 = td_elements[0].text.strip()
                data2 = td_elements[1].text.strip()
                data3 = td_elements[2].text.strip()
                

                data=[data1,data2,data3]
                print(data)
                
                return data
            else:
                data=[0,0,0]
                print(data)
                return data
        else:
            return data
    except Exception as e:
        return data