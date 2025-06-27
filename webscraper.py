import requests
from bs4 import BeautifulSoup
import json
import csv

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_data(soup):
    # Customize this part based on your target website
    headlines = soup.find_all(['h1', 'h2', 'h3'])
    data = [{"headline": h.get_text(strip=True)} for h in headlines if h.get_text(strip=True)]
    return data

def save_to_csv(data, filename="output.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["headline"])
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def main():
    url = input("Enter the website URL to scrape: ")
    soup = fetch_and_parse(url)
    if soup:
        data = extract_data(soup)
        if data:
            save_to_csv(data)
            save_to_json(data)
            print(f"Data extracted and saved successfully.")
        else:
            print("No data found.")
    else:
        print("Failed to parse website.")

if __name__ == "__main__":
    main()
