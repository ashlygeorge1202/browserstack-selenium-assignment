import requests
import os

def download_image(soup, index):
    try:
        img = soup.find("img")
        if img and img.get("src"):
            url = img["src"]
            data = requests.get(url).content
            with open(f"images/article_{index}_image.jpg", "wb") as f:
                f.write(data)
            print(f"Image saved as images/article_{index}_image.jpg\n")
    except Exception as e:
        print(f"Image download failed: {e}")
