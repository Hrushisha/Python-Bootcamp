'''errors are different types 
name error/syntax error 

to handle the exceptions we have exception handling
what are the problems 
2 types exception 1.checked except2.unchecked
try,except,else,finally are keywords'''

'''try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('divide by zero is not possible')   '''

'''try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('divide by zero is not possible')   ''' 
#without using exception 

'''a=10
b=0
print(a/b)
n1=1000
n2=2000
print(n1+n2)'''

'''try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('divide by zero is not possible')   
    n1=100
    n2=200
    print(n1+n2)
    a1=1000
    a2=2000'''

'''try:
    a=5
    print(b)
except NameError:
    print('variable b is not assigned')'''

'''try:
    arr=[1,7,8,12,36]
    print(arr[8]) #we can use 4 but the answer is 36
except IndexError:
    print('cannot access index value')'''

try:
    arr=[1,7,8,12,36]
    print(arr[8]) #we can use 4 but the answer is 36
except IndexError:
    print('cannot access index value')
else:
    print('no exception occured')
finally:
    print('finally wednesday is the last day of training')    





