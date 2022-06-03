from pprint import pprint as print

#match
def http_error(status):
    match status:
        case 400|500:
            return "Bad Request"
        case 404 |500:
            return "Not Found"
        case _:
            return "Somethings wrong"

import requests
print(http_error(500)) 


#pattern matching
https://www.inspiredpython.com/course/pattern-matching/python-pattern-matching-examples-etl-and-dataclasses

#Run multiple files sequentially
https://stackoverflow.com/questions/48203912/how-to-run-the-sequence-of-python-scripts-one-after-another-in-a-loop

  #API pagination
  https://stackoverflow.com/questions/17777845/python-requests-arguments-dealing-with-api-pagination
    
 #filtering
https://datagy.io/python-filter/
  
#exploration tools:
dir()
help(class_name)

#OOP
encapsulation : store the state (properties) with methods (behaviour)
  
  
  #classes:
setter: set property value using a method. setter will not have return values, they will amend property value
better alternative is to get all properties and default them to some value in __init__ (constructor, dundee - gets called each time class is initiliazed), so arguments can be passed during class intialization. 
@classmethod before methods that are class wide and not for instance but for the whole class. Global variable inside class ==> useful for alternative constructor


