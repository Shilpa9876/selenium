# import requests
#
# def find_broken_images(url):
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to fetch the website: {response.status_code}")
#         return
#
#     html = response.text
#     image_urls = extract_image_urls(html)
#
#     print(f"Total {len(image_urls)} image(s) found.")
#
#     for image_url in image_urls:
#         image_response = requests.get(image_url)
#         if image_response.status_code != 200:
#             print(f"Broken image found: {image_url}")
#
# def extract_image_urls(html):
#     # You can use a library like BeautifulSoup to parse the HTML and extract the image URLs.
#     # Here, we'll use a simple regex pattern to find the URLs.
#     import re
#
#     pattern = re.compile(r'<img.*?src="(.*?)"', re.IGNORECASE)
#     matches = re.findall(pattern, html)
#     return matches
#
# # Example usage
# website_url = "https://adventurehq.ae/"
# find_broken_images(website_url)
import requests

def find_pages_with_missing_images(url):
    pages_with_missing_images = {}

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the website: {response.status_code}")
        return pages_with_missing_images

    html = response.text
    image_urls = extract_image_urls(html)

    print(f"Total {len(image_urls)} image(s) found.")

    for image_url in image_urls:
        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            page_url = image_response.request.url
            if page_url not in pages_with_missing_images:
                pages_with_missing_images[page_url] = []
            pages_with_missing_images[page_url].append(image_url)

    return pages_with_missing_images

def extract_image_urls(html):
    import re

    pattern = re.compile(r'<img.*?src="(.*?)"', re.IGNORECASE)
    matches = re.findall(pattern, html)
    return matches

# Example usage
website_url = "https://adventurehq.ae/"
pages_with_missing_images = find_pages_with_missing_images(website_url)

print("Pages with missing images:")
for page_url, missing_image_urls in pages_with_missing_images.items():
    print(f"Page URL: {page_url}")
    print("Missing image URLs:")
    for image_url in missing_image_urls:
        print(image_url)
    print()

