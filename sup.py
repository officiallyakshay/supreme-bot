from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 

driver.find_element_by_partial_link_text('Script').click()

wait=WebDriverWait(driver, 10)

shirt=wait.until(EC.presence_of_element_located((By.ID, 's')))
Select(driver.find_element_by_id('s')).select_by_visible_text('Large')
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

driver.get('https://www.supremenewyork.com/checkout')

