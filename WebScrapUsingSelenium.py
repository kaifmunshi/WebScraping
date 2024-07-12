# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# create option object
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# create webdriver object
driver = webdriver.Chrome(options=options)


# get geeksforgeeks.org
driver.get("https://www.1mg.com/search/all?name=dolo")


element = driver.find_element(By.XPATH, '//*[@id="category-container"]/div/div[3]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/a/div[2]/span')
element_P = driver.find_element(By.XPATH, '//*[@id="category-container"]/div/div[3]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/a/div[3]/div/div[1]')
# print complete elements list
print(element.text)
print(element_P.text)