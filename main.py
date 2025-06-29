import requests
import json
import pandas as pd

data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=0f724149a2ee4ce18362146d56781a22")

articles = data.json()['articles']

df = pd.DataFrame(articles)

print(df.columns)