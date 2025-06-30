from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utils.translator import translate_text
from utils.image_downloader import download_image
from pages.opinion_page import OpinionPage
import time

class OpinionDetailPage(OpinionPage):
    def process_article(self, index):
        time.sleep(2)  # allow full render
        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        try:
            title_elem = soup.find("h1")
            title_es = title_elem.text.strip()
            if title_es.lower() in ["opinión", "editorial", "tribuna"]:
                title_es = soup.find("h2").text.strip()
            title_en = translate_text(title_es)
        except:
            title_es, title_en = "[Missing]", "[Translation Failed]"

        try:
            content = soup.find("article").text.strip()
        except:
            content = "[Missing]"

        print(f"Title (ES): {title_es}")
        print(f"Translated (EN): {title_en}")
        print(f"Content (ES): {content[:300]}{'...' if len(content) > 300 else ''}\n")

        download_image(soup, index)
        return title_en
