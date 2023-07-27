# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome()
# from selenium.webdriver.common.by import By
#
# def click_collection_page_by_class(driver, collection_class):
#     collection_elements = driver.find_elements(By.CLASS_NAME, "menu__mobile")
#     for element in collection_elements:
#         if element.text == "Women":  # Replace with the text on the collection link
            # element.click()
            # break
#
# driver.get("https://forever21.ae/products/jacquard-zebra-mini-dress?variant=44185087639785")
# button = driver.find_element(By.CLASS_NAME, "shopify-payment-button__button")
# button.click()
# Email_input = driver.find_element(By.ID, 'checkout_email_or_phone')
# Email_input.send_keys("test123@gmail.com")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_country")
# Email_input.send_keys("india")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_first_name")
# Email_input.send_keys("test")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_last_name")
# Email_input.send_keys("tester")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_address1")
# Email_input.send_keys("house no. 222, Panchkula,Haryana, 134204")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_address2")
# Email_input.send_keys("house no. 222, Panchkula,Haryana, 134204")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_city")
# Email_input.send_keys("haryana")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_province")
# Email_input.send_keys("dubai")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_phone")
# Email_input.send_keys("+9711234567890")
#
# button = driver.find_element(By.ID,"continue_button")
# button.click()






                            # Add to cart complete process

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#set chromodriver.exe path
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.forever21.ae")
#object of ActionChains
a = ActionChains(driver)
# #identify element
# m = driver.find_element(By.LINK_TEXT, "WOMEN")
# #hover over element
# a.move_to_element(m).perform()
# #identify sub menu element
# n = driver.find_element(By.LINK_TEXT, "Date Night")
# # hover over element and click
# a.move_to_element(n).click().perform()
# o = driver.find_element(By.XPATH, "/html/body/div[4]/main/div/div[2]/div[3]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div[1]/a/span/picture/img")
# a.move_to_element(o).click().perform()
#
# print("Page title: " + driver.title)
# #close browser
# # driver.close()
# button = driver.find_element(By.CLASS_NAME, "shopify-payment-button__button")
# button.click()
# Email_input = driver.find_element(By.ID, 'checkout_email_or_phone')
# Email_input.send_keys("test123@gmail.com")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_country")
# Email_input.send_keys("india")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_first_name")
# Email_input.send_keys("test")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_last_name")
# Email_input.send_keys("tester")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_address1")
# Email_input.send_keys("house no. 222, Panchkula,Haryana, 134204")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_address2")
# Email_input.send_keys("house no. 222, Panchkula,Haryana, 134204")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_city")
# Email_input.send_keys("haryana")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_province")
# Email_input.send_keys("dubai")
# Email_input = driver.find_element(By.ID,"checkout_shipping_address_phone")
# Email_input.send_keys("+9711234567890")

# button = driver.find_element(By.ID,"continue_button")
# button.click()



                                        # Add to Wishlist

o = driver.find_element(By.CLASS_NAME, "forever-img")
a.move_to_element(o).click().perform()

k = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[1]/div[2]/div[2]/div/div[2]/div[2]/a/div[2]")
a.move_to_element(k).click().perform()

r = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[3]/div/span")
a.move_to_element(r).click().perform()
# print("Page title: " + driver.title)

s = driver.find_element(By.CLASS_NAME, "wishlist-text")
a.move_to_element(s).click().perform()
# print("Product title")