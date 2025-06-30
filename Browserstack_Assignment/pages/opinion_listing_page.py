from selenium.webdriver.common.by import By
from pages.opinion_page import OpinionPage
from pages.opinion_detail_page import OpinionDetailPage

class OpinionListingPage(OpinionPage):
    URL = "https://elpais.com/opinion/"

    def __init__(self, driver):
        super().__init__(driver)
        self.visit(self.URL)

    def get_article_links(self, limit=5):
        print("Waiting for article elements to be visible…")
        self.wait_for(By.CSS_SELECTOR, "article")
        elements = self.driver.find_elements(By.CSS_SELECTOR, "article a")

        links = []
        seen = set()
        for elem in elements:
            href = elem.get_attribute("href")
            if href and href.startswith(self.URL) and href not in seen:
                seen.add(href)
                links.append(href)
            if len(links) == limit:
                break

        print(f"\nSelected {len(links)} valid article URLs\n")
        return links

    def open_article(self, url):
        self.visit(url)
        return OpinionDetailPage(self.driver)
