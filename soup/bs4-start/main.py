from icecream import ic
from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
ic(soup.title)
ic(soup.title.name)
ic(soup.title.string)

# print(soup.prettify())
ic(soup.a.string)
ic(soup.find_all('a'))

# iterate through find all
for link in soup.find_all('a'):
    ic(link.get('href'),link.getText())
    

# isolating elements
heading = soup.find(name="h1", id="name")
ic(heading, heading.getText())

section_heading = soup.find(name="h3",class_="heading")
ic(section_heading.name, section_heading.getText())

# querying css selectors
company_url = soup.select_one(selector="p a")
ic(company_url)

name = soup.select_one("#name")
headings = soup.select(".heading")

ic(name, headings)
