import bs4
import requests as req

basic_url=f"https://books.toscrape.com/catalogue/page-7.html"

books=req.get(basic_url)
print(books)

soup= bs4.BeautifulSoup(books.text, "lxml")
print(soup.select(".product_pod"))