#https://finance.yahoo.com/quote/%5EBVSP/history/

import requests

response = requests.get("https://finance.yahoo.com/quote/%5EBVSP/history/")
print(response.text[:600])
