# 🧪 BrowserStack Selenium Automation Assignment

This project is a Python-based automation script using **Selenium** and **BrowserStack** to:

✅ Scrape the first 5 opinion articles from [El País - Opinión](https://elpais.com/opinion/)  
✅ Translate article titles from Spanish to English using Google Translate  
✅ Extract article content  
✅ Download article images  
✅ Run tests in **parallel** across 5 different browsers/devices via **BrowserStack**

---

## 📁 Project Structure

browserstack-assignment/ │
├── pages/

│ ├── opinion_page.py # Common methods for opinion pages
│ ├── opinion_listing_page.py # For fetching article links
│ └── opinion_detail_page.py # For scraping individual articles


├── utils/
│ ├── credentials.py # Your BrowserStack credentials
│ └── translator.py # Google Translate logic


├── images/ # Folder for downloaded images


├── browserstack_main.py # Main test runner script
├── requirements.txt # Required Python libraries
└── README.md # This documentation


## 🧰 Prerequisites

- Python 3.7+
- A [BrowserStack](https://www.browserstack.com/) account
- An internet connection

---

## 🧪 Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/browserstack-assignment.git
cd browserstack-assignment