#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
from flask import Flask
import requests, re




'''
TO DO:
 have to set up my urls, have to have endpoints for my frontend
 have to probably link up a db, will use pymsql for the reviews so that the site gets some reviews 
 will see about setting up comparisons on pricing using data analysis...which I will have to research to scale this up

'''
def scraper():

      app = Flask(__name__)
      rubbish = []
      urls =  [
    "https://thebullrun.co.za",
    "https://mrgeorge.co.za",
    "https://mezepoli.co.za",
    "https://sebule.co.za",
    "https://cuisino.co.za",
    "https://pappasrestaurant.co.za",
    "https://pigalle.co.za",
    "https://thebigmouth.co.za",
    "https://miha.co.za",
    "https://solosandton.co.za",
    "https://signaturerestaurant.co.za"
     ]
      for url in urls:
              response = requests.get(url, timeout=10)
              response.raise_for_status()
              rubbish.append(response)
              print(rubbish)
      

      if __name__ == "__main__":
             scraper()
             app.run()
            


      

      