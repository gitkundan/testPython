# https://www.appsloveworld.com/sample-rest-api-url-for-testing-with-authentication/#huserregistration

import json
from urllib import response
import requests
import json
from pprint import pprint
import pandas as pd

#constants
base_url='http://restapi.adequateshop.com'
page_num=1
last_page=3
api_user=f'{base_url}/api/Tourist?page={page_num}'

query_params={
    "users":"dd"
}

data=[]
while page_num < last_page:
    response=requests.get(api_user).json() #produces a dict
    data+=response['data']
    pprint(len(data))
    page_num=int(response['page'])
    last_page=int(response['total_pages'])
    # file=json.dumps(data)
    with open('result.json','w') as f:
        json.dump(data,f,indent=4)
