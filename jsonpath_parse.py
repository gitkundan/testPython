# Program to parse JSON data in Python using jsonpath
# https://codecary.com/python-jsonpath-examples/
# https://jsonpath.com/
# https://github.com/h2non/jsonpath-ng >>download UI locally
# https://goessner.net/articles/JsonPath/index.html#e2

import json
from jsonpath_ng import jsonpath, parse

with open("response_weather.json", 'r') as json_file:
    json_data = json.load(json_file)

dt_expression = parse('$..list[*]["dt"]')

final={}
for match in dt_expression.find(json_data):
    final["date"]=match.value
print(final)