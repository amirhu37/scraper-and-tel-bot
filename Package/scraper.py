from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from datetime import datetime
from time import sleep

import regex

MIN = 1
MAX = 101
hour = 3600
# dates dat going to be run
dates = ['00:30','01:30' ,'02:30', '03:30', '04:30', '05:30', '06:30', '07:30', '08:30', '09:30', '10:30','11:30','12:30'
         '13:30', '14:30', '15:12', '16:30', '17:30', '18:30', '19:30', '20:30', '21:30', '22:30', '23:55']


# start Web Driver (dont forget to dl a geckodriver )
driver = webdriver.Firefox()
driver.get('https://coinmarketcap.com')
# Render The Pge
for i in range(4):
    driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
    sleep(.5)

# exctract data 
class do():
    # Target names:
    def get_name():
        names = list()
         # coins names
        for i in range(MIN, MAX):
            n = driver.find_element_by_xpath(
                f'//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[{i}]/td[3]/div/a/div/div/div/p').text
            names.append(n)
        return names 

    # Target Changes
    def get_delta():
        deltas = list()
         # coins changes
        for i in range(MIN, MAX):
            d = driver.find_element_by_xpath(
                f'//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[5]/span').text
            
            deltas.append(regex.sub(r',', '', d).strip('%'))

        deltas = list(map(float, deltas))

        return deltas 

# lts start scraping
def start():
    f = open('res.txt', 'w')    
    print('APP IS RUNNIG')
         
     # frst data
    d1 = list(zip(do.get_name(), do.get_delta()))  # First DAta 
    
    print(d1)
     #let app sleep for while
    sleep(15)
    
     # second data
    d2 = list(zip(do.get_name(), do.get_delta()))    # Socond DAta

         #debuginf stff
    print(d1)
    print(150*'*')
    print(d2)

    for i in range(len(d2)):
        delta_p = ( abs ((d2[i][1] - d1[i][1] )+1) / (( d2[i][1] + d1[i][1] )+1)  )*100         # MOST BE CHANGED / MODIFIED
        
        if delta_p >= 0:
            print(f'{i} , {d2[i][0]} , {delta_p}')
            f.write(f'{d2[i][0]} , {delta_p} \n')

    f.close()
    driver.close()


