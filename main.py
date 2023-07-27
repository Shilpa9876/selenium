import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.adventurehq.ae")
driver.maximize_window()
Login_link = driver.find_element(By.LINK_TEXT, 'Login')
Login_link.click()

Email_input = driver.find_element(By.ID, 'customer_email')
Password_input = driver.find_element(By.ID, 'customer_password')
Email_input.send_keys('sam@yopmail.com')  # Replace with your email
Password_input.send_keys('Sam@1234')  # Replace with your password
button = driver.find_element(By.CLASS_NAME, "form-action--submit")
button.click()

home_link = driver.find_element(By.CLASS_NAME, 'site-logo-image')
home_link.click()

# brand_link = driver.find_element(By.ID, "slick-slide012")
# driver.execute_script("arguments[0].scrollIntoView();", brand_link)
# brand_link.click()

# search_input = WebDriverWait(driver, 10).until(
#  EC.visibility_of_element_located((By.CLASS_NAME, "form-field-input")))
# # Enter search keyword
# search_input.send_keys('Dry Bags')
#
#
# # Wait for the dropdown to be visible and click on the first option
# dropdown_element = WebDriverWait(driver, 10).until(
# EC.visibility_of_element_located((By.CLASS_NAME, "search-flydown--product-title"))
# )
# dropdown_element.click()
#
# button = driver.find_element(By.CLASS_NAME, "live-search-button")
# button.click()
# Logout_link = driver.find_element(By.LINK_TEXT, 'Logout')
# Logout_link.click()

camera_link = driver.find_element(By.CLASS_NAME, "promo-block--content")
driver.execute_script("arguments[0].scrollIntoView();", camera_link)
camera_link.click()

# button = driver.find_element(By.CLASS_NAME, "blogposts--footer-link")
# driver.execute_script("arguments[0].scrollIntoView();", button)
# button.click()

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://www.adventurehq.ae")
# driver.maximize_window()
# Login_link = driver.find_element(By.LINK_TEXT, 'Login')
# Login_link.click()
# Email_input = driver.find_element(By.ID, 'customer_email')
# Password_input = driver.find_element(By.ID, 'customer_password')
# Email_input.send_keys('sam@yopmail.com')  # Replace with your email
# Password_input.send_keys('Sam@1234')  # Replace with your password
# button = driver.find_element(By.CLASS_NAME, "form-action--submit")
# button.click()
# home_link = driver.find_element(By.CLASS_NAME, 'site-logo-image')
# home_link.click()
# Logout_link = driver.find_element(By.LINK_TEXT, 'Logout')
# Logout_link.click

# camera_link = driver.find_element(By.CLASS_NAME, "promo-block--content")
# driver.execute_script("arguments[0].scrollIntoView();", camera_link)
# camera_link.click()
time.sleep(10)
driver.close()


# import requests
# import urllib3
# from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# URL = "https://www.adventurehq.ae"
# iBrokenImageCount = 0
# driver = webdriver.Chrome()
# driver.get("https://www.adventurehq.ae")
#
# driver.maximize_window()
# driver.get(URL)
#
# image_list = driver.find_elements(By.TAG_NAME, "img")
# print('Total number of images on ' + URL + ' are ' + str(len(image_list)))
#
# for img in image_list:
#     try:
#         response = requests.get(img.get_attribute('src'), stream=True)
#         if (response.status_code != 200):
#             print(img.get_attribute('outerHTML') + " is broken.")
#             iBrokenImageCount = (iBrokenImageCount + 1)
#
#     except requests.exceptions.MissingSchema:
#         print("Encountered MissingSchema Exception")
#     except requests.exceptions.InvalidSchema:
#         print("Encountered InvalidSchema Exception")
#     except:
#         print("Encountered Some other Exception")
#
# driver.quit()
#
# print('The page ' + URL + ' has ' + str(iBrokenImageCount) + ' broken images')