from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='C:\Users\Diksha\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver.get('http://www.google.com')

driver.maximize_window()

time.sleep(5)

driver.refresh()