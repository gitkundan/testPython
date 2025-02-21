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

========================================================================================
#Vectorized conditional if-then in pandas
Source : Rob Mulla (https://youtu.be/SAFmrTnEHLg)
	
%%timeit
df['reward']=df['hate_food'] #default option
condition= ((df['pct_sleeping']>0.05) & (df['time_in_bed']>5)) | (df['age']>90)

df.loc[condition,'reward']=df['favourite_food']




========================================================================================
# Add file path to Windows PATH
import os
mingw_path = r'C:\mingw-w64\mingw64\bin'
os.environ['PATH']=mingw_path + ';' + os.environ['PATH']
print(os.environ['PATH'])

========================================================================================
# Generate mock data
from faker import Faker

fake = Faker()

person = {}
# person['id'] = fake.ssn()
person = type(random.randrange(1,9))
person=range(11,14)
person=random.randint(11,14)
# person['first_name'] = fake.first_name()
# person['last_name'] = fake.last_name()
# person['email'] = fake.unique.ascii_email()
# person['company'] = fake.company()
# person['phone'] = fake.phone_number()
print(person)

========================================================================================
# Unzip file to temporary directory
import tempfile
input_file=r"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip"

#create a temporary folder, download the zip file from web, extract the file and read the file into pandas

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory',tmpdirname)

    with requests.get(input_file) as r:
        with open(f'{tmpdirname}/bank.zip','wb') as f:
            f.write(r.content)

    with zipfile.ZipFile(f'{tmpdirname}/bank.zip','r') as zip_ref:
        zip_ref.extractall(path=f'{tmpdirname}') #extract all files into tempdir
        
        df=pd.read_csv(f'{tmpdirname}/bank-full.csv')
        print(df.head())
min(1,2,3)

========================================================================================
sklearn

#important that the dataset is split into features and response variables earlier
# (Option A) : without validation set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# (Option B) : with validation set perform extra step
X_train, X_val, y_train, y_val=train_test_split(X_train,y_train,test_size=0.33,random_state=42)







=======================================================================================
Matplotlib functional interface 

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Note the below methods are on plt but they are actually
# methods on axes object not at figure level

plt.figure(figsize=(6,4),dpi=100) # this is at figure level
x=np.linspace(1,10,10)
y=x**2
z=x**3
# plot the first line
plt.plot(x,y,'--m',linewidth=2,label='line 1')

# plot the second line on the same axis
plt.plot(x,z,'^r',label='line 2')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Seals and Profit')
plt.legend() #calling this will display the legend box in chart
plt.grid(True)

LINE STYLES
- means solid line
-- means dashed line
: means dotted line
-. means dash-dot line

MARKERS
. means point marker
, means pixel marker
o
v
^
<
>
1...8 has different number based markers styles

COLORS
cmyk rgb

To display legend : plt.legend()

=======================================================================================
get all methods of an object 
import inspect
members = inspect.getmembers(df.index)
methods = [m[0] for m in members if not m[0].startswith('_') and callable(m[1])]
methods

=======================================================================================




