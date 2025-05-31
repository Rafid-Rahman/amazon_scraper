# 🛒 Amazon Product Scraper

This is a Python-based automation project that scrapes detailed product data from **Amazon search results**, including **title**, **price**, **rating**, **number of reviews**, **stock status**, **product URL**, and the unique **ASIN code** of each item. It's built using **Selenium WebDriver** with optimized Chrome options for efficient and headless scraping.

---

## 🚀 Features

- 🔍 Scrapes up to a specified number of products based on a search term (e.g., "laptops")
- 📦 Collects essential product info:
  - Product Title
  - Price (USD)
  - Rating (out of 5)
  - Total Number of Reviews
  - Stock Status
  - Product Link
  - ASIN (Amazon Standard Identification Number)
- ✅ Automatically removes duplicate products based on ASIN
- 📄 Exports all data to a structured Excel file
- 🧠 Headless browser setup using Selenium for smooth and fast scraping

---

## 📁 Project Structure
📦 Amazon Product Scraper
- 📜 amazon_scraper.py # Main Python script
- 📄 amazon_products.xlsx # Output Excel file (auto-generated)


---

## 🛠️ Technologies Used

- Python 3
- Selenium WebDriver
- Webdriver Manager
- Pandas
- ChromeDriver (Headless)

---

## 📦 Output Example

Each row in the Excel file contains:
- **Title:** "Acer Aspire 5 Slim Laptop..."
- **Price:** 399.99
- **Rating:** 4.5
- **Reviews:** 1,253
- **Stock:** Available
- **Product Link:** https://www.amazon.com/...
- **ASIN:** B0BS4BP8FB

---

## 🧪 How to Run This Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/amazon-scraper.git
   ```
   ```bash
   cd amazon-scraper
   ```
2. **Install all dependencies**
   ```bash
   pip install selenium pandas webdriver-manager openpyxl
   ```
3. **Run the script**
   ```bash
   python amazon_scraper.py
   ```
4. **The data will be saved as an Excel file.**

---


## 🎯 Use Case
This project is part of my Upwork portfolio, demonstrating my capabilities in:

- ✅ Web scraping and data extraction
- ✅ Automating browser tasks using Selenium
- ✅ Structured product data handling
- ✅ Data cleaning and deduplication
- ✅ Saving results into well-formatted Excel files

---

## 📬 Contact
For project collaboration, feedback, or hiring:
-  📧 Email: rafidrahman00@gmail.com
-  💼 Upwork: [Upwork Profile](https://www.upwork.com/freelancers/~01d564beb96daefba0?mp_source=share)


