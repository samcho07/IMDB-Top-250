#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:33:06 2022

@author: mertsamast
"""

# =============================================================================
# IMDB Top 250 filmlerini çekmek
# =============================================================================


import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)    #url'yi istek olarak atadık.


html_icerik = response.content      #içeriği aldık
soup = BeautifulSoup(html_icerik, "html.parser") #alınan içeriği parse ettik.

a = float(input("Rating giriniz:"))


## td class= "titlecolum"   kısmını çekeceğiz.

film_isimleri = soup.find_all("td", {"class": "titleColumn"})  #İsimleri listeye aldık
ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})   #puanları listeye aldık.

for film, rating in zip(film_isimleri, ratingler):
    film = film.text
    rating = rating.text
    
    film = film.strip()
    film = film.replace("\n", "")
    
    rating = rating.strip()
    rating = rating.replace("\n", "")
    
    if(float(rating) > a):
        print("Film: {} Puanı: {}".format(film, rating))
    
    




