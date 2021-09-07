from icecream import ic
from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response =requests.get(url)
web_html = response.text # all html text of specified page

soup = BeautifulSoup(web_html, 'html.parser')

movie_elements = soup.find_all(class_="jsx-4245974604")
movie_titles = [movie for movie in movie_elements ]

data=soup.select("img.jsx-952983560.loading")
lst= (set([i['alt'].replace("'","").replace(",","") for i in data if i['alt']!=""  ]))
ic(lst)
