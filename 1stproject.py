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
from os import listdir
from PIL import Image

for filename in listdir('./'):
    if filename.endswith('.png'):
        try:
            img = Image.open('./' + filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)  # print out the names of corrupt files