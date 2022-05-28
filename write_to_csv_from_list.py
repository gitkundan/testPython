import pandas as pd
from unittest import result
import requests
import json
import csv

"""
url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

querystring = {"q":"San Francisco"}

headers = {
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
	"X-RapidAPI-Key": "5ecc639b78mshfcabb11048814d3p1782afjsn64ac99145dab"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

with open ('response_weather.json','w') as f:
    json.dump(response,f)
"""
with open('response_weather.json','r') as f:
    response=json.load(f)

# whenever working with lists initialize an empty list
final=[]
for i in response['list']:
    date=i['dt']
    humidity=i['humidity']
    average=i['temp']['average']
    city=response['city']['name']
    final.append([date,humidity,average,city])
    # df=pd.array(final)
    # print (df)
    with open('results.csv','w') as f:
        writer=csv.writer(f)
        writer.writerows(final)
    # print(final)
# print(response['list']['dt']['temp']['average'])
# print(response['list']['temp']['wind_speed'])
# for i in response['city']:
#     city=i
#     print(i)
    # country=i['country']
    # date=i['list']['dt']
    # temperature=i['list']['temp']['average']
    # windspeed=i['list']['wind_speed']
    # result-(city,country,date,temperature,windspeed)
    # print(result)
