from selenium import webdriver
import schedule
from time import sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()


def getToClass(username, pw):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
    # open website
    driver.get("https://entrar.in/")

    sleep(1)
    # find and click the login button
    driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav/div/div/a").click()
    sleep(1)
    # input username
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/div[2]/input")\
        .send_keys(username)
    # input password
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/form/div[3]/input")\
        .send_keys(pw)
    sleep(1)
    # click the submit button
    driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/form/div[5]/div/button").click()
    sleep(4)
    # click the classroom option

    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/nav/div[2]/div/div[1]/div/ul/li[8]/a/span[2]")\
        .click()
    sleep(4)

    # refresh OR search button
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/input")\
        .click()
    # click the join button
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/table/tbody/tr[1]/td[4]/a")\
        .click()
    # click listen only
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i")\
        .click()
    # switch tabs


getToClass('BE/0007331', 'Sidhant123')


# TODO:
# check for join button
# switch tab
# start again after specified time
# check for refresh if button not there
