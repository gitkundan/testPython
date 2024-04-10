'''
reading code files e.g. csv module
import csv and run help(csv) and then dir(csv)

How to know which are the classes:
Option A: dir(csv) and then look at the capitalized ones : those are classes
throw help on class now : help(csv.DictReader)

Option B: IDE Ctrl-Shift-O and then colon :- will show the class at the top

Option C : use inspect module :- more on in later section

Inspect module : 
members = inspect.getmembers(csv)
for name, member in members:
    print(name, type(member))
    
# Filter members by Type
functions_and_classes = inspect.getmembers(csv, predicate=inspect.isfunction) + inspect.getmembers(csv, predicate=inspect.isclass)
for name, member in functions_and_classes:
    print(name, type(member))
    
# Get info about a specific member
doc = inspect.getdoc(csv.reader)
signature = inspect.signature(csv.reader)
print("Documentation:", doc)
print("Signature:", signature)

For classes, you can use inspect.getmembers() with inspect.ismethod or inspect.isfunction to get its methods:
methods = inspect.getmembers(csv.DictReader, predicate=inspect.isfunction)
for name, method in methods:
    print(name, type(method))
    
You can continue exploring further by using other inspect functions like inspect.ismodule(), inspect.isclass(), inspect.isfunction(), inspect.ismethod(), inspect.isbuiltin(), etc., to get more detailed information about the module, its classes, and their methods.
    
print(inspect.getdoc(obj)) # gets docstring for the object
print(inspect.getsourcelines(obj.__init__)) # gets source code for init method 

get list of all attributes of a class, including methods and properties

class ExampleClass:
    def method(self):
        pass

    @property
    def property(self):
        return "property"

members = inspect.getmembers(ExampleClass)
for name, member in members:
    print(name, type(member))

3. Inspecting a Method's Source Code
def example_function():
    print("Hello, World!")

source_code = inspect.getsource(example_function)
print(source_code)

4. Inspecting the Call Stack
def inner_function():
    stack = inspect.stack()
    for frame_record in stack:
        print(f"Function: {frame_record.function}, File: {frame_record.filename}, Line: {frame_record.lineno}")

def outer_function():
    inner_function()

outer_function()

5. Inspecting a Module's File Path
import os

file_path = inspect.getfile(os)
print(file_path)


6. Inspecting a Class's Base Classes
To get the base classes of a class, you can use inspect.getmro():

import inspect

class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

mro = inspect.getmro(DerivedClass)
for cls in mro:
    print(cls.__name__)

7. Inspecting a Function's Default Arguments
You can use inspect.signature() and inspect.Parameter.default to get the default arguments of a function:

def example_function(a, b=2, c=3):
    pass

signature = inspect.signature(example_function)
for name, param in signature.parameters.items():
    if param.default is not param.empty:
        print(f"{name} = {param.default}")


Inspect stack frames:

import inspect

def func1():
  frame = inspect.currentframe() 
  print(inspect.getframeinfo(frame))

def func2():
  func1()
  
func2()
This prints out filename, line number, function name, etc of where func1() was called.


Inspect call arguments:

def func(a, b, c):
  sig = inspect.signature(func)
  print(sig) # shows function signature
  print(sig.parameters) # shows parameters as dict
  
func(1, 2, 3)


Inspect classes and functions:

print(inspect.isclass(MyClass)) # True
print(inspect.isfunction(func1)) # True
print(inspect.getmembers(MyClass)) # all members






























'''
