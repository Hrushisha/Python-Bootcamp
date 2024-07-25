class Student:
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
s1.display() 
    
        

