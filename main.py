from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

import requests
from bs4 import BeautifulSoup as bs

app = FastAPI()

class Movies(BaseModel):
    name : str

@app.get("/")
def root():
    return {"Hello":"World!"}

@app.get("/movies")
def get_movies():
    result = []

    req = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
    html = req.text
    soup = bs(html, "lxml")

    movieContents = soup.select("#old_content > table > tbody > tr")
    for movieContent in movieContents:
        try:
            movieName = movieContent.select_one("td.title > div > a").text
            result.append({'name':movieName})
            # print(movieName)
        except AttributeError:
            continue    

    return result

uvicorn.run(app,host='0.0.0.0', port=8000)