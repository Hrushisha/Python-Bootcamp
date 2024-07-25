'''POLYMORPHISM:

HUMAN BEING :
in college student
in THeater auidence
in market customer 
in sports players 
in home child 


compile time --> 
run time-->
overriding can possible same function with differnt parameters 
overloading can possible same function with same parameters    '''

'''class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'  
      #f string with 2 parameters we have name and age
      
class student(person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch

    def __str__(self):
        res=super().__str__()
        return f'{res},{self.roll},{self.branch}'
    
obj=student('hrushisha',24,2,'CSE')
print(obj) '''  

class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'  
      #f string with 2 parameters we have name and age
      #  
class student(person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch

    def __str__(self):
        perdetails=super().__str__()
        return f'{perdetails},{self.roll},{self.branch}'
    
obj=student('hrushisha',24,2,'CSE')
print(obj)    

class AnnualDay(student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studetails =super().__str__()
        return f'{studetails},{self.program}'

aobj=AnnualDay('Hrushisha',20,'d3','CSE','Solo')    
print(aobj) 
    