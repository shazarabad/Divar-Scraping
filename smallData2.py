import requests
from bs4 import BeautifulSoup
import time   

def scrape_data1(url):
    data22=['N/A','N/A','N/A']
    try:
        
        response = requests.get(url)
        if response.status_code == 200:
            time.sleep(10)
            soup = BeautifulSoup(response.content, "html.parser")
            time.sleep(10)

            td_elements = None
            
            td_elements = soup.find_all("td", class_="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable")
            if len(td_elements) == 1:
                if td_elements[0].text.strip() == 'آسانسور':
                    data22[0] ='آسانسور'
                elif td_elements[0].text.strip() == 'پارکینگ':
                    data22[1] = 'پارکینگ'
                elif td_elements[0].text.strip() == 'انباری':
                    data22[2] = 'انباری'

            elif len(td_elements) == 2:
                
                if td_elements[0].text.strip() == 'آسانسور' and td_elements[1].text.strip() == 'پارکینگ':
                    data22[0] ='آسانسور'
                    data22[1] ='پارکینگ'
                elif td_elements[0].text.strip() == 'آسانسور' and td_elements[1].text.strip() == 'انباری':
                    data22[0] ='آسانسور'
                    data22[2]='انباری'
                elif td_elements[0].text.strip() == 'پارکینگ' and td_elements[1].text.strip() == 'انباری':
                    data22[1] ='پارکینگ'
                    data22[2]='انباری'
                
            elif len(td_elements) == 3:
                data22 = ['آسانسور', 'پارکینگ', 'انباری']
                    
            else:
                data22=['N/A','N/A','N/A']

        else:
             time.sleep(30)
             
    except Exception as e:
        print("here?")
        print(str(e))

    print(data22)

    return data22

#[<td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">آسانسور</td>, <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">انباری</td>]
#[<td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">آسانسور</td>, <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">پارکینگ</td>, <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">انباری</td>]
#[<td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">پارکینگ</td>, <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">انباری</td>]