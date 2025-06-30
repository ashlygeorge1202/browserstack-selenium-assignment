import threading
from selenium import webdriver
from pages.opinion_listing_page import OpinionListingPage
from utils.translator import translate_text
from utils.image_downloader import download_image
from utils.credentials import USERNAME, ACCESS_KEY
import time

# BrowserStack hub URL
bs_url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Desired capabilities for different browser-device combinations
browsers = [
    {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '11',
            'sessionName': 'Parallel Test 1',
            'buildName': 'BrowserStack Assignment'
        },
        'browserName': 'Chrome',
        'browserVersion': 'latest'
    },
    {
        'bstack:options': {
            'os': 'OS X',
            'osVersion': 'Monterey',
            'sessionName': 'Parallel Test 2',
            'buildName': 'BrowserStack Assignment'
        },
        'browserName': 'Safari',
        'browserVersion': 'latest'
    },
    {
        'bstack:options': {
            'deviceName': 'Samsung Galaxy S22',
            'realMobile': 'true',
            'osVersion': '12.0',
            'sessionName': 'Parallel Test 3',
            'buildName': 'BrowserStack Assignment'
        },
        'browserName': 'Chrome'
    },
    {
        'bstack:options': {
            'deviceName': 'iPhone 13',
            'realMobile': 'true',
            'osVersion': '15',
            'sessionName': 'Parallel Test 4',
            'buildName': 'BrowserStack Assignment'
        },
        'browserName': 'Safari'
    },
    {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': 'Parallel Test 5',
            'buildName': 'BrowserStack Assignment'
        },
        'browserName': 'Firefox',
        'browserVersion': 'latest'
    },
]

def create_driver(capabilities):
    try:
        options = webdriver.ChromeOptions()
        for key, value in capabilities.items():
            if key != 'bstack:options':
                options.set_capability(key, value)
        options.set_capability('bstack:options', capabilities['bstack:options'])
        driver = webdriver.Remote(command_executor=bs_url, options=options)
        return driver
    except Exception as e:
        print(f"Failed to create driver for {capabilities.get('browserName', 'Unknown')}: {e}")
        return None

def worker(capabilities, article_url, index):
    driver = create_driver(capabilities)
    if not driver:
        print(f"Skipping article {index} due to driver initialization failure.")
        return

    try:
        detail_page = OpinionListingPage(driver).open_article(article_url)
        title_en = detail_page.process_article(index)
    except Exception as e:
        print(f"Error processing article {index}: {e}")
    finally:
        try:
            if driver.session_id:  # Only quit if session is active
                driver.quit()
        except Exception as quit_error:
            print(f"Error quitting driver for article {index}: {quit_error}")


def main():
    print("Fetching article URLs from desktop Chrome session...")
    desktop_driver = create_driver(browsers[0])
    if not desktop_driver:
        print("Could not fetch article URLs due to Chrome session failure.")
        return

    list_page = OpinionListingPage(desktop_driver)
    try:
        article_urls = list_page.get_article_links()
    except Exception as e:
        print(f"Failed to fetch article URLs: {e}")
        article_urls = []
    finally:
        try:
            desktop_driver.quit()
        except Exception as e:
            print(f"Error quitting desktop Chrome session: {e}")

    threads = []
    for i in range(min(len(article_urls), len(browsers))):
        t = threading.Thread(target=worker, args=(browsers[i], article_urls[i], i + 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n All parallel tests completed.")

if __name__ == "__main__":
    main()
