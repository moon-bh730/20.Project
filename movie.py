import requests
from bs4 import BeautifulSoup as bs

req = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
html = req.text
soup = bs(html, "lxml")


movieContents = soup.select("#old_content > table > tbody > tr")
for movieContent in movieContents:
    try:
        movieName = movieContent.select_one("td.title > div > a").text
        print(movieName)
    except AttributeError:
        continue