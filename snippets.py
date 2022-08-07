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
async version of requests : https://github.com/ross/requests-futures
		
#Generic REST API consumer
https://codereview.stackexchange.com/questions/8455/a-generic-rest-api-consuming-python-library

#Test API for query:
https://www.appsloveworld.com/free-online-sample-rest-api-url-for-testing/
	
	
	
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

#file reads
filename="C:/Users/Dell/Downloads/PPR-2022-01-Meath(1).csv"

with open(filename,'r') as f:
    lines=f.readlines()
    print(lines)

#reading archive files (zip)
#remember to save the intenet requested get file on local before calling zip
# Import the required method
from zipfile import ZipFile
# path: /tmp/dependencies/data/source/downloaded_at=2021-02-01/PPR-ALL.zip

with ZipFile(path, "r") as f:
    # Get the list of files
    file_names = f.namelist()
    print(file_names)
    # Extract the CSV file
    csv_file_path = f.extract(file_names[0])
    print(csv_file_path)

#reading / writing csv
import csv
from pprint import pprint as print
filename="C:/Users/Dell/Downloads/PPR-2022-01-Meath(1).csv"

with open(filename,'r') as f:
    reader=csv.DictReader(f)
    row=next(reader)
    print(row)

#write to csv
import csv

with open(path, mode="r", encoding="windows-1252") as reader_csv_file:
    reader = csv.DictReader(reader_csv_file)
    # The new file is called "PPR-2021-Dublin-new-headers.csv"
    # and will be saved inside the "tmp" folder    
    with open("/tmp/PPR-2021-Dublin-new-headers.csv",
                    mode="w",
                    encoding="windows-1252",
                ) as writer_csv_file:
        writer = csv.DictWriter(writer_csv_file, fieldnames=new_column_names)
        # Write header as first line
        writer.writerow(new_column_names)
        for row in reader:
	        # Write all rows in file
	        writer.writerow(row)

            
#dictionary iterations
students=[]
Peter=[{"name": "Peter", "gender": "Male", "age": 20}]
Mary=[{"name": "Mary", "gender": "Female", "age": 30}]
students=Peter+Mary
pprint(students)


my_dict = {1: 'blue', 2: 'green', 3: 'red', 4: 'yellow', 5: 'orange'}
new={}
for k,v in my_dict.items():
    new[k]=v

#ETL Framework:
a) ETL framework : pygrametl (https://chrthomsen.github.io/pygrametl/doc/quickstart/install.html, https://www.integrate.io/blog/building-an-etl-pipeline-in-python/)
b) will load into datawarehouse in OOP pattern
c) Airflow for orchestration


#openpyxl
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Fill
import openpyxl
file_path=r"C:\Users\John\Downloads\MOCK_DATA.xlsx"
wb=load_workbook(file_path, read_only=False)
ws=wb['data']

wb.defined_names.delete('data5') #this range needs to be created beforehand
new_range = openpyxl.workbook.defined_name.DefinedName('data5', attr_text='data!$a$1:$c$24') #snot needed as range will be dynamic with offset
wb.defined_names.append(new_range)
wb.save(file_path)
wb.close()
#=OFFSET(data!$A$1,0,0,COUNTA(data!$B:$B),6)
# for sheet_title, sheet_coords in range.destinations:
#     sheet = ws
#     for row in sheet[sheet_coords]:
#         x= "\t".join(str(cell.value) for cell in row)
#         print(x)
# new_range = openpyxl.workbook.defined_name.DefinedName('newrange', attr_text='Sheet!$A$1:$A$5')
# wb.defined_names.append(new_range)

=OFFSET('data'!$a$1,0,0,COUNTA('data'!$B:$B)-2,6)


#zip files
import zipfile
url=r'https://github.com/CoatiSoftware/Sourcetrail/releases/download/2021.4.19/Sourcetrail_2021_4_19_Windows_64bit_Portable.zip'
# url=r'https://stackoverflow.com/questions/69651204/python-download-a-file-from-url'

import requests
with open ('sourcetrail.zip','wb') as file:
    file.write(requests.get(url).content)

with zipfile.ZipFile('sourcetrail.zip','r') as f:
    f.extractall()
