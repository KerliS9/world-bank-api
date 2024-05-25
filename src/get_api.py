import requests

def get_api(url):
  response = requests.get(url)
  data = response.text
  print(response.status_code)
  print(data)
  return data

url = "https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50"
get_api(url)