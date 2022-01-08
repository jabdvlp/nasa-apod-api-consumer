import requests
import json
from datetime import date, datetime

date_req = input("Ingrese una fecha específica en formato 'YYYY-MM-DD': " )
if (date_req):
    print(f"FECHA: {date_req}")
else:
    today = date.today()
    print(f"FECHA: {today}")
        

endpoint = "https://api.nasa.gov/planetary/apod"
api_key = "DEMO_KEY"
query_params = {"api_key":api_key,"date":date_req}
response = requests.get(endpoint, params=query_params)

# print(response.json())
description = response.json()["explanation"]
image = response.json()["hdurl"]


print(f"DESCRIPCIÓN: \n {description}")
print(f"URL DE LA IMAGEN: \n {image}")

