"""
construct the expression in UI [download the binary from https://jsonpath.com/ and run]

Json Path : use . notation to traverse objects. [*] to be used if array
filter array with ?@ notation as described in https://goessner.net/articles/JsonPath/index.html#e2
library documentation : https://pypi.org/project/jsonpath-ng/
"""

import json
from pprint import pprint
from jsonpath_ng.ext import parse


json_str = '''
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
'''

json_obj=json.loads(json_str)
# jsonpath_expr = parse('$.store.book[?(@.price<9)]')
jsonpath_expr = parse('$.store.book[?price<9 & category=fiction]')
x=[match.value for match in jsonpath_expr.find(json_obj)]
pprint(x)
