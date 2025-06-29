import requests
import json
import pandas as pd

data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=ENV['AUTH_TOKEN']")

articles = data.json()['articles']

df = pd.DataFrame(articles)

print(df.columns)