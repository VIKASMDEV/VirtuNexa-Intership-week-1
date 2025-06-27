# 🕷️ Python Web Scraper with BeautifulSoup and Requests

## 📌 Goal

Create a Python web scraper using libraries such as `BeautifulSoup` and `requests` to extract data from a website. The scraper collects relevant information (e.g., headlines, links, or product details) and stores it in a structured format like CSV or JSON for easy analysis. It handles different HTML elements and is built to work with various websites.

---

## 📖 About the Project

This project is a simple yet powerful web scraper that:

- Accepts a website URL from the user.
- Fetches and parses the webpage content.
- Extracts all headlines (`<h1>`, `<h2>`, `<h3>` elements).
- Saves the extracted data into:
  - `output.csv`
  - `output.json`

It uses Python’s `requests` and `BeautifulSoup` libraries for HTTP communication and HTML parsing.

---

## 🚀 Features

- 🔍 Extracts `h1`, `h2`, and `h3` tags from any public website.
- 📦 Outputs data into both CSV and JSON formats.
- 🛠️ Handles missing or malformed URLs gracefully.
- ⚙️ Easily extendable to scrape additional data (e.g., links, products, prices).

---

## 📁 Requirements

- Python 3.x
- Install the required libraries:

```bash
pip install requests beautifulsoup4
