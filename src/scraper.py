import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class PremierLeagueScraper:
    def __init__(self, url):
        self.url = url
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--window-size=1920,1080")

    def get_raw_data(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        try:
            driver.get(self.url)
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            html_content = driver.page_source
            dfs = pd.read_html(html_content)
            return dfs[0]
        finally:
            driver.quit()