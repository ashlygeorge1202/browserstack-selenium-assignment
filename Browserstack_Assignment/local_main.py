from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.opinion_listing_page import OpinionListingPage
from data.analyzer import analyze_titles
import os

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def main():
    os.makedirs("images", exist_ok=True)
    driver = setup_driver()
    try:
        listing_page = OpinionListingPage(driver)
        links = listing_page.get_article_links(limit=5)

        translated_titles = []
        for i, link in enumerate(links, 1):
            detail_page = listing_page.open_article(link)
            title_en = detail_page.process_article(i)
            translated_titles.append(title_en)

        analyze_titles(translated_titles)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
