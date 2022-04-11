"""
1) string formatting : 
age = 34
print(f"You are {age}")

2) Another (lesser used) syntax is variable.format(name=friend_name)

Start with 21.Tuples

=======================================================================

Object Oriented Programming:
Thinking in sequences (ETL) = Procedural
Thinking in objects and classes = OOO

Object = state(a.k.a attributes a.k.a properties represented with variables) + behaviour (a.k.a methods represented with function)
objectCustomer has state like email = laura@laura.com and behaviour like place order
objectButton on website has label and actions bundled together
distinctive feature of OOO is dont think data separately from actions, they are one unit representing a customer
think customer data and customer action in one single unit = encapsulation; dont think customer data as separate

class = blueprints to create object
class desribes possible states and behaviours that every object of certain type could have

customerClass = define the states and behaviour
customerObjectJohn = particular value of states; behaviour will come from class

Everything in python is an object e.g. DataFrame, function, int are objects of some class
type(object) will give the class
type(df) will be pandas.dataframe
dir(df) will give all attributes and methods
dir(df)
do dir on class and also on object
same way do help(df)

Digression : Python Interface : https://realpython.com/python-interface/
Interface acts as a blueprint for class

methods will have self as the first argument

self is standing for the future object
to call the method no need to put self

option (1) - attributes in methods
# Include a set_name method in a class
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee and then emp will have all methods that are part of the class
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)


option (1) - attributes in init constructor
define all attributes in one go while intial creation of object

class Employee:
    def __init__(self,name,salary=1000):
        self.name=name
        self.salary=salary

#All attributes will now get created when you create the object
John = Employee('John',10000)

Convention : classes in CamelCase starting with Capitals
methods and attributes : lower_snake_case

"""
