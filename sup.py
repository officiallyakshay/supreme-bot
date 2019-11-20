from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException

buyerName='Supreme Shay'
buyerMail='supremeshay@email.com'
buyerTele='9254206969'
buyerAdress='In The Ville'
buyerCity='Beverly Hills'
buyerZIP='90210'
buyerCountry='USA'
buyerCardNumber='4242424242424242'
buyerCardExpMonth='09'
buyerCardExpYear='2022'
cvv='420'

driver = webdriver.Chrome(executable_path = '/Users/casual_shay/Downloads/chromedriver')
driver.get('http://www.supremenewyork.com/shop/all/sweatshirts')

while True:
	try:
 		driver.find_element_by_partial_link_text('Script')
 		break
 	except (NoSuchElementException):
	  	wait=WebDriverWait(driver, 10)
	  	waitBis=wait.until(EC.presence_of_element_located((By.ID, 'time-zone-name')))
	  	driver.refresh()


driver.find_element_by_partial_link_text('Script').click()

wait=WebDriverWait(driver, 10)

shirt=wait.until(EC.presence_of_element_located((By.ID, 's')))
Select(driver.find_element_by_id('s')).select_by_visible_text('Large')
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

try:
    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'button checkout'))
    )
finally:
	driver.get('https://www.supremenewyork.com/checkout')

	ord_billing_name=driver.find_element_by_id('order_billing_name')
	ord_billing_name.send_keys(buyerName)

	ord_email=driver.find_element_by_id('order_email')
	ord_email.send_keys(buyerMail)

	ord_tele=driver.find_element_by_id('order_tel')
	ord_tele.send_keys(buyerTele)

	ord_adress=driver.find_element_by_id('bo')
	ord_adress.send_keys(buyerAdress)

	ord_billing_city=driver.find_element_by_id('order_billing_city')
	ord_billing_city.send_keys(buyerCity)

	ord_zip=driver.find_element_by_id('order_billing_zip')
	ord_zip.send_keys(buyerZIP)

	Select(driver.find_element_by_id('order_billing_country')).select_by_visible_text(buyerCountry)

	ord_cnb=driver.find_element_by_id('rnsnckrn')
	ord_cnb.send_keys(buyerCardNumber)

	Select(driver.find_element_by_id('credit_card_month')).select_by_visible_text(buyerCardExpMonth)
	Select(driver.find_element_by_id('credit_card_year')).select_by_visible_text(buyerCardExpYear)

	ccv=driver.find_element_by_id('orcer')
	ccv.send_keys(cvv)

	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()