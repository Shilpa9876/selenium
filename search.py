                         # Search of null values

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#
# def test_search_with_null_input():
#     driver = webdriver.Chrome()
#     search_url = 'https://www.adventurehq.ae'
#
#     try:
#         driver.get(search_url)
#
#         # Find the search bar element and clear any existing input
#         search_bar = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "live-search-form-fields-inline"))
#         )
#         search_bar.clear()
#
#         # Perform the search with null input (empty string)
#         search_bar.send_keys(Keys.RETURN)
#
#         # Wait for the search results to load
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "live-search-button"))
#         )
#
#         # Find the search results element
#         search_results = driver.find_element(By.CLASS_NAME, "live-search-button")
#
#         # Check if the search results are displayed
#         if search_results.is_displayed():
#             print("Search bar is showing results with null input.")
#         else:
#             print("Search bar is not showing results with null input.")
#
#     except Exception as e:
#         print("Error occurred:", e)
#
#     finally:
#         driver.quit()
#
# if __name__ == "__main__":
#     test_search_with_null_input()
#


# from selenium import webdriver
#
# create webdriver object
# driver = webdriver.Chrome()
#
# URL of the website
# url = "https://www.adventurehq.ae/"
#
# Opening the URL
# driver.get(url)
#
# Getting current URL source code
# get_source = driver.page_source
#
# Text you want to search
# search_text = "tent"
#
# print True if text is present else False
# print(search_text in get_source)



                                      # for searching valid and invalid inputs
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# URL of the website
url = "https://www.adventurehq.ae/"

# Opening the URL
driver.get(url)

# Getting current URL source code
get_source = driver.page_source

# Text you want to search
search_text = "tent"

# print True if text is present else False
print(search_text.lower() in get_source.lower())
