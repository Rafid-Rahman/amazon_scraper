import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

# Initialize WebDriver with optimized options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_amazon_search_results(search_query, num_products=100):
    base_url = f"https://www.amazon.com/s?k={search_query}"
    driver.get(base_url)
    time.sleep(3)
    
    products = []
    product_links = set()
    asin_set = set()
    
    while len(products) < num_products:
        product_elements = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")
        
        for product in product_elements:
            if len(products) >= num_products:
                break
            
            try:
                title = product.find_element(By.CSS_SELECTOR, "h2 span").text.strip()
            except:
                title = "N/A"
            
            try:
                price_whole = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip()
                price_fraction = product.find_element(By.CSS_SELECTOR, "span.a-price-fraction").text.strip()
                price = f"{price_whole}.{price_fraction}"
            except:
                price = "N/A"
            
            try:
                init_rating = product.find_element(By.CSS_SELECTOR, "a.a-popover-trigger.a-declarative").get_attribute("aria-label")
                rating = init_rating.split()[0]
            except:
                rating = "N/A"
            
            try:
                num_reviews = product.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text.strip()
            except:
                num_reviews = "N/A"
            
            stock = "Available" if "Currently unavailable" not in product.text else "Out of stock"
            
            try:
                link = product.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-line-clamp-2.s-link-style.a-text-normal").get_attribute("href")
                if link in product_links:
                    continue  
                product_links.add(link)
            except:
                link = "N/A"
            
            if title == "N/A" or link == "N/A":
                continue  
            
            # Extract ASIN from product link
            try:
                asin = link.split("/dp/")[1].split("/")[0]
            except:
                asin = "N/A"
            
            # Skip if ASIN already seen
            if asin == "N/A" or asin in asin_set:
                continue
            asin_set.add(asin)

            products.append({
                "Product Title": title,
                "Price (USD)": price,
                "Rating (out of 5)": rating,
                "Total Number of Reviews": num_reviews,
                "Stock Status": stock,
                "Product Link": link,
                "ASIN": asin
            })

        
        # Go to the next page if needed
        try:
            next_page = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            next_page.click()
            time.sleep(3)
        except NoSuchElementException:
            break  # Exit loop if no next page
    
    return products

# Define search term
search_term = "laptops"
data = scrape_amazon_search_results(search_term, num_products=100)

# Save data to Excel
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"F:\\Upwork\\Portfolio Projects\\Projects\\amazon_products_1.xlsx"

df = pd.DataFrame(data)
df.to_excel(file_path, index=False)

# Close WebDriver
driver.quit()

print(f"Scraping completed. Data saved at {file_path}")