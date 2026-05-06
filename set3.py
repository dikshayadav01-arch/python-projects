from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='C:\Users\Diksha\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver.get('http://www.amazon.in')
driver.maximize_window()

time.sleep(5)
select=driver.find_element_by_link_text('Electronics')
select.click()

time.sleep(5)
select1=driver.find_element_by_link_text('Audio')
select1.click()