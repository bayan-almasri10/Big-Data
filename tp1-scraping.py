import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = [book.h3.a["title"] for book in soup.find_all("article", class_="product_pod")]

df = pd.DataFrame({"Book Title": titles})
df.to_csv("books.csv", index=False)

print("Scraping complete! Saved to books.csv")
