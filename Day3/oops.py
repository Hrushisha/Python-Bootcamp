#blue print it is one template
 
'''class Student: it conatins function,constuctor,data 
it is a logical entity (class class_name)
object- properties,behaviour,entity

class is blueprint of an object
class is a logical entity
class contains functions,constructors,data 
OBJECT:
object is a real world entity
object is an instance of a class 
object is a subpart of a class 
it is physical entity 
objects contain properties,behaviour/function,identity (each and every should be unique)

CONSTRUCTOR:
constructor is  a special function or method which is used to invoked the instance variable 
cons does snot return any value 
while creating the object constructor will get invoked

there are 3 types of constructors 
default 
parametrized
non parametrized


how to create a construction '''

'''class Student:
    def __init__(self,Name,roll,branch,address,email):
        self.Name=Name
        self.roll=roll 
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print('Name is:',self.Name)
        print('roll is:',self.roll)
        print('branch is:',self.branch)
        print('address is :',self.address)
        print('email is :',self.email)

    s1=Student('hrushisha',2,'CSE','Hyderabad','hrushii@gmail.com')  
    s1.display()'''

'''class Student:
    def __init__(self,Name,roll,branch,address,email):
        self.Name=Name
        self.roll=roll 
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print('Name is:',self.Name)
        print('roll is:',self.roll)
        print('branch is:',self.branch)
        print('address is :',self.address)
        print('email is :',self.email)
        print()

s1=Student('hrushisha',2,'CSE','Hyderabad','hrushii@gmail.com')
s2=Student('Harshithaa',4,'EEE','hyderabad','harshitha@gamil.com')  
s1.display()
s2.display()'''

''' Static we don't have static keyword in python but also we are using 
   Static is used for memory management
   instead of creating individually a common data create a static data and pass the copy to all the objects'''

'''without using display()
we have to create '''

'''class Student:
    def __init__(self,Name,roll,branch,address,email):
        self.Name=Name
        self.roll=roll 
        self.branch=branch
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.Name} {self.roll} {self.branch} {self.address} {self.email}'

s1=Student('hrushisha',2,'CSE','Hyderabad','hrushii@gmail.com')
s2=Student('Harshithaa',4,'EEE','hyderabad','harshitha@gamil.com')  
print(s1)
print(s2)'''


'''abstractclass contains abstract method and non abstract method 

INHERITANCE:
single inheritance:'''

'''class JNTU:
    def schedule_academics():
        print("Scheduling Academics"
    def declare_holidays():
        print("national and summer holidays")
    def results():
        print("go to www.jntuhresults.com") 
                                                   
class SriDevi(JNTU):
    def fees():
        print('3rd year fee is 85k')
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )
sobj.=SriDevi
sobj.fees():
sobj.schedule_academics():
sobj.national and summer holidays():
sobj.3rd year fee is 85k():'''

'''multiple inheritance is not possible in java but it is possible in python 

abstract method       #abc- module ABC-class '''
'''from abc import ABC 
                         #import java.util.*;   we are not using in recent trends 
class RBIBank():
    def interest():      #abstract method 
        pass
    def loan():           #nonabstract method/concrete method 
        print("provides home loan")

class HDFC(RBIBank):
    def interest():
        print('7.5% interest')        

class SBI(RBIBank):
    def interest():
        print('9% interest')        

class AXIS(RBIBank):
    def interest():
        print('15% interest')        
               
                        
aobj=AXIS
aobj.interest()
aobj.loan()'''


'''create a abstract method and non abstract method using mobile phones'''
        
'''from Mobiles(datasets):        #python is mainly used  for libraries  
     def calling():'''
     

'''from abc import ABC

class vehicle():
    def speed():
        pass
    def milage():
        pass
    def model():
        pass
    def breaks():
        print('stop the vehicle')
    
class RangeRover(vehicle):
    def speed():
        print('450 max speed')
    def milage():
        print('15KMPH')
    def model():
        print('New Model')


class BMW(vehicle):
    def speed():
        print('500 max speed')
    def milage():
        print('15KMPH')
    def model():
        print('legender')


fobj=BMW
fobj.milage 
fobj.speed()
fobj.model()
fobj.breaks()    '''               


'''multiple inheritance is more than one children are inheriting from the single parent  '''




'''ENCAPSULATION:
binding data and methods into single component is called Encapsulation 

ex:
class is the best example for Encapsulate
adv: 
code integration 
security

access Modifiers:
  public,private (within the class we can access for 2 underscores),protected(access outside the class within the package 1 underscores_)'''

class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary   #private data

    def get_salary(self):       #public method 
        return self.__salary
    
    def Empdisplay(self):          #public method 
        print(self.name,self.role)   

class company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc

    def comdisplay(self):
        print(self.cname,self.loc)

    def _hiring(self):
        print('hiring for the manager role')    

cobj=company ('Accenture','USA')
eobj=Employee('Hrushisha','devc',95000)
eobj.Empdisplay()
print(cobj._hiring())

  
    