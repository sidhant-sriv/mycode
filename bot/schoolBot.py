from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
def getToClass(username,pw):
    # driver = webdriver.Chrome( "C:\Program Files (x86)\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
    driver.get("https://entrar.in/")

    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/div/a").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/div[2]/input")\
        .send_keys(username)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/div[3]/input")\
        .send_keys(pw)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/div[5]/div/button").click()
    sleep(4)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/nav/div[2]/div/div[1]/div/ul/li[8]/a/span[2]")\
        .click()
    sleep(4)
getToClass('BE/0007331','Sidhant123')

#add this later

'''

import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

'''


#TODO:
#check for join button 
# switch tab
# start again after specified time
#check for refresh if button not there
