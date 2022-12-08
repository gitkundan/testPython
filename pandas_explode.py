#https://plainenglish.io/blog/data-extraction-parse-a-3-nested-json-object-23cb978b66ad

with open(input_file,mode='r',encoding='utf-8') as f:
    obj=json.load(f)


#once you get de-nested json i.e. as list of records (qlik style) then you can throw json_normalize
df=pd.json_normalize(obj['data'][0]['screen_data']['data'])

or you can simply invoke the dataframe constructor

df2=pd.DataFrame(obj['data'][0]['screen_data']['data'])

