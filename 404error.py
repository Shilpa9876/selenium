# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://adventurehq.ae/")
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import requests
#
# driver = webdriver.Chrome()
# driver.get("https://adventurehq.ae/")
#
# #get all links
# all_links = driver.find_elements(By.CSS_SELECTOR,"a")
#
# #check each link if it is broken or not
# for link in all_links:
#     #extract url from href attribute
#     url = link.get_attribute('href')
#
#     #send request to the url and get the result
#     result = requests.head("https://adventurehq.ae/")
#
#     #if status code is not 200 then print the url (customize the i
#     # if result.status_code != 404:
#     #     print(url, result.status_code)
#     def find_pages_with_missing_images(url):
#         pages_with_missing_images = {}
#
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"Failed to fetch the website: {response.status_code}")
#             return pages_with_missing_images
#     website_url = "https://adventurehq.ae/"
#     pages_with_missing_images = find_pages_with_missing_images(website_url)
#     print("Pages with missing images:")
#     for page_url, missing_image_urls in pages_with_missing_images.items():
#         print(f"Page URL: {page_url}")
#         print("Missing image URLs:")
#         for image_url in missing_image_urls:
#             print(image_url)



# def find_pages_with_missing_images(url):
#     pages_with_missing_images = {}
#     import requests
#
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to fetch the website: {response.status_code}")
#         return pages_with_missing_images
#
# # Indentation fixed
# website_url = "https://adventurehq.ae/"
# pages_with_missing_images = find_pages_with_missing_images(website_url)
# print("Pages with missing images:")
# for page_url, missing_image_urls in pages_with_missing_images:
#     print(f"Page URL: {page_url}")
#     print("Missing image URLs:")
#     for image_url in missing_image_urls:
#         print(image_url)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://adventurehq.ae/")
#
# all_links = driver.find_elements(By.TAG_NAME, "a")
# total_links_count = len(all_links)
#
# print("Total number of links:", total_links_count)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import requests
#
# def find_pages_with_missing_images(url):
#     pages_with_missing_images = {}
#
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to fetch the website: {response.status_code}")
#         return pages_with_missing_images
#
#     # Replace this with your logic to find pages with missing images
#     # Populate the 'pages_with_missing_images' dictionary with your results
#     pages_with_missing_images = {
#         'page1': ['image1.jpg', 'image2.jpg'],
#         'page2': ['image3.jpg', 'image4.jpg']
#     }
#
#     return pages_with_missing_images
#
# driver = webdriver.Chrome()
# driver.get("https://www.adventurehq.ae/")
#
# all_links = driver.find_elements(By.CSS_SELECTOR, "a")
#
# website_url = "https://www.adventurehq.ae/"
# pages_with_missing_images = find_pages_with_missing_images(website_url)
#
# if pages_with_missing_images is not None:
#     print("Pages with missing images:")
#     for page_url, missing_image_urls in pages_with_missing_images.items():
#         print(f"Page URL: {page_url}")  # Updated line
#         print("page URLs:")
#         for image_url in missing_image_urls:
#             print(page_url)  # Updated line
# else:
#     print("No pages with missing images found.")




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import requests
#
# def find_pages_with_missing_images(url):
#     pages_with_missing_images = {}
#
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to fetch the website: {response.status_code}")
#         return pages_with_missing_images
#
#     # Replace this with your logic to find pages with missing images
#     # Populate the 'pages_with_missing_images' dictionary with your results
#     pages_with_missing_images = {
#         'page1': ['image1.jpg', 'image2.jpg'],
#         'page2': ['image3.jpg', 'image4.jpg']
#     }
#
#     return pages_with_missing_images
#
# driver = webdriver.Chrome()
# driver.get("https://www.adventurehq.ae/")
#
# all_links = driver.find_elements(By.CSS_SELECTOR, "a")
#
# website_url = "https://www.adventurehq.ae/"
# pages_with_missing_images = find_pages_with_missing_images(website_url)
#
# if pages_with_missing_images is not None:
#     print("Pages with missing images:")
#     for page_url, missing_image_urls in pages_with_missing_images.items():
#         print(f"Page URL: {page_url}")
#         print("Missing image URLs:")
#         for image_url in missing_image_urls:
#             print(image_url)
# else:
#     print("No pages with missing images found.")



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


                  ###  Missing images code
# def find_pages_with_missing_images(url):
#     pages_with_missing_images = {}
#
#     driver = webdriver.Chrome()
#     driver.get(url)
#
#     all_links = driver.find_elements(By.CSS_SELECTOR, "a")
#
#     for link in all_links:
#         page_url = link.get_attribute('href')
#         if page_url and not page_url.startswith('javascript:'):
#             try:
#                 response = requests.get(page_url)
#                 if response.status_code != 200:
#                     if page_url not in pages_with_missing_images:
#                         pages_with_missing_images[page_url] = []
#                     pages_with_missing_images[page_url].append(page_url)
#             except requests.exceptions.RequestException as e:
#                 print(f"Error occurred while checking page URL: {page_url}")
#                 print(e)
#
#     driver.quit()
#     return pages_with_missing_images
#
# website_url = "https://www.adventurehq.ae"
# pages_with_missing_images = find_pages_with_missing_images(website_url)
#
# if pages_with_missing_images:
#     print("Pages with missing images:")
#     for page_url, missing_image_urls in pages_with_missing_images.items():
#         print(f"Page URL: {page_url}")
#         print("Missing image URLs:")
#         for image_url in missing_image_urls:
#             print(image_url)
# else:from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import requests
#
# def find_pages_with_missing_images(url):
#     pages_with_missing_images = {}
#
#     driver = webdriver.Chrome()
#     driver.get(url)
#
#     all_links = driver.find_elements(By.CSS_SELECTOR, "a")
#
#     for link in all_links:
#         page_url = link.get_attribute('href')
#         if page_url and not page_url.startswith(('http://', 'https://', 'ftp://', 'ftps://')):
#             continue  # Skip unsupported URL schemes
#
#         try:
#             response = requests.get(page_url)
#             if response.status_code != 200:
#                 if page_url not in pages_with_missing_images:
#                     pages_with_missing_images[page_url] = []
#                 pages_with_missing_images[page_url].append(page_url)
#         except requests.exceptions.RequestException as e:
#             print(f"Error occurred while checking page URL: {page_url}")
#             print(e)
#
#     driver.quit()
#     return pages_with_missing_images
#
# website_url = "https://www.adventurehq.ae"
# pages_with_missing_images = find_pages_with_missing_images(website_url)
#
# if pages_with_missing_images:
#     print("Pages with missing images:")
#     for page_url, missing_image_urls in pages_with_missing_images.items():
#         print(f"Page URL: {page_url}")
#         print("Missing image URLs:")
#         for image_url in missing_image_urls:
#             print(image_url)
# else:
#     print("No pages with missing images found.")





from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from urllib.parse import urlparse

def find_pages_with_missing_images(url):
    pages_with_missing_images = {}

    driver = webdriver.Chrome()
    driver.get(url)

    all_links = driver.find_elements(By.CSS_SELECTOR, "a")

    for link in all_links:
        page_url = link.get_attribute('href')
        if page_url:
            parsed_url = urlparse(page_url)
            if parsed_url.scheme == 'javascript' or parsed_url.scheme == 'tel':
                continue  # Skip unsupported URL schemes

            try:
                response = requests.get(page_url)
                if response.status_code != 200:
                    if page_url not in pages_with_missing_images:
                        pages_with_missing_images[page_url] = []
                    pages_with_missing_images[page_url].append(page_url)
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while checking page URL: {page_url}")
                print(e)

    driver.quit()
    return pages_with_missing_images

website_url = "https://www.adventurehq.ae"
pages_with_missing_images = find_pages_with_missing_images(website_url)

if pages_with_missing_images:
    print("Pages with missing images:")
    for page_url, missing_image_urls in pages_with_missing_images.items():
        print(f"Page URL: {page_url}")
        print("Missing image URLs:")
        for image_url in missing_image_urls:
            print(image_url)
else:
    print("No pages with missing images found.")













