from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

products = []
prices = []
ratings = []
driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uni')

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find('div', attrs={'class':'_4rR01T'})
    rating = a.find('div', attrs={'class':'_3LWZlK'})
    price = a.find('div', attrs={'class', '_3tbKJL _1_WHN1'})
    products.append(name.text)
    ratings.append(rating.text)
    prices.append(price.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

print(df.head())