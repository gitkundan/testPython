import pandas as pd
import requests
url_1='https://api.datamuse.com/words?sp=hipopatamus'
response_1=requests.get(url_1)
df1=pd.DataFrame(response_1.json())

url_2="https://api.datamuse.com/words?sp=animal"
response_2=requests.get(url_2)
df2=pd.DataFrame(response_2.json())

# df_final=pd.merge(df1,df2,how='outer',on='word')
df_final=pd.concat([df1,df2],axis=1)
print(df_final)