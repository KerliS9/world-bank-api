import requests
import json
import math

def get_api_pages(url):
    response = requests.get(url)
    pages = response.json()[0]
    total_pages = math.ceil(pages['total']/pages['per_page'])
    pages = []
    for page in range(total_pages):
        page = page + 1
        pages.append(page)
    return pages


def get_data():
  url = 'https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50'
  pages = get_api_pages(url)
  data = []
  for page in pages:
      url = f"https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page={page}&per_page=50"
      response = requests.get(url)
      response.raise_for_status()
      response_data = response.json()[1]
      print('data', page, response_data[0])
      data.extend(response_data)
  return data

#get_data()