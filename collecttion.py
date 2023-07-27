# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Function to find elements by name
# def find_elements_by_name(driver, element_name):
#     return driver.find_elements(By.NAME, element_name)
#
# # Example URLs (replace these with your website URLs)
# website_url = 'https://www.adventurehq.ae'
# collection_url = 'https://www.adventurehq.ae/collection/sup'
# product_url = 'https://www.adventurehq.ae/products/reid-santa-monica-10-6-paddleboard-baby-blue-grey'
#
# # Initialize the web driver
# driver = webdriver.Chrome()  # Replace 'Chrome' with 'Firefox', 'Edge', etc., if you prefer a different browser.
#
# try:
#     # Step 1: Open the website's home page
#     driver.get(website_url)
#
#     # Step 2: Click on the collection page
#     driver.get(collection_url)
#
#     # Step 3: Find elements with a specific name
#     element_name_to_find = 'SUP'
#     # elements = find_elements_by_name(driver, element_name_to_find)
#     #
#     # # Step 4: Print the results
#     # if elements:
#     #     print(f"Found {len(elements)} elements with name '{element_name_to_find}':")
#     #     for element in elements:
#     #         print(element.text)  # You can perform actions on each element here if needed.
#     # else:
#     #     print(f"No elements found with name '{element_name_to_find}'.")
#
#     # Step 5: Open the product page
#     driver.get(product_url)
#
#     # You can add further actions on the product page if needed.
#     # For example, interact with product elements, add to cart, etc.
#
# finally:
#     # Close the browser window when done
#     driver.quit()





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to click on a collection page by class name
# def click_collection_page_by_class(driver, collection_class):
#     collection_elements = driver.find_elements(By.CLASS_NAME, collection_class)
#     for element in collection_elements:
#         if element.text == "Biking":  # Replace with the text on the collection link
#             element.click()
#             break
#     # Add any necessary waiting logic if needed
#     # For example: WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='collection-content']")))
#
# # Function to click on a product page from the collection page
# def click_product_page(driver, product_url):
#     # Find the element to click on the product page within the collection page
#     product_element = driver.find_element(By.CLASS_NAME '')]")
#     product_element.click()
#     # Add any necessary waiting logic if needed
#     # For example: WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-details']")))
#
# # Example URLs (replace these with the actual URLs of your collection and product pages)
# collection_url = 'https://www.adventurehq.ae/bike-chain'
# product_url = 'https://www.adventurehq.ae/navmenu-link.navmenu-link-depth-145'
#
# # Initialize the web driver (You'll need the appropriate web driver for your browser installed)
# driver = webdriver.Chrome()  # Replace 'Chrome' with 'Firefox', 'Edge', etc., if you prefer a different browser.
#
# try:
#     # Step 1: Click on the collection page
#     collection_class_name = 'navmenu-link.navmenu-link-depth-1'  # Replace with the actual class name of the collection link
#     click_collection_page_by_class(driver, collection_class_name)
#
#     # Step 2: Click on the product page from the collection page
#     click_product_page(driver, product_url)
#
#     # You can add further actions on the product page if needed.
#     # For example, interact with product elements, add to cart, etc.
#
# finally:
#     # Close the browser window when done
#     driver.quit()






