#!/usr/bin/env python
# coding: utf-8

# In[84]:


#%%time
#reference : https://www.youtube.com/watch?v=0gguceHbWPg
#https://www.youtube.com/watch?v=2FNcJKCfrzI
import nest_asyncio
nest_asyncio.apply()
import requests
import httpx
import logging
import asyncio
from timeit import time

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'


# In[85]:


async def log_request(request):
    print(f'Request: {request.method} {request.url}')
    
async def log_response(response):
    request=response.request
    print(f'Response: {request.method} {request.url} - Status {response.status_code}')


# In[87]:


async def get_episode(ep_id: int):
    async with httpx.AsyncClient(event_hooks={'request':[log_request],'resonse':[log_response]}) as client:
        r=await client.get(f'https://rickandmortyapi.com/api/episode/{ep_id}')
        results.append(r.json())
        return
    
async def main():
    tasks=[]
    for ep_id in range(1,11):
        tasks.append(get_episode(ep_id))
    await asyncio.gather(*tasks)
    
results=[]
asyncio.run(main())

print(len(results))
        


# In[104]:


url='https://httpbin.org/uuid'
h={
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-6316dce3-0f9d76ed4adc534a1d154b5f"
  }

result=[]
for i in range(3):
    r=requests.get(url,headers=h)
    response=r.json()
    result.append(response['uuid'])
print(result)

