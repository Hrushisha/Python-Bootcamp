arr=[1,3,6,2,5,3,7,5,1]

'''
1:2
3:2
6:1
2:1
5:2
7:1
'''

#count the  frequency of each number
'''
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:   
        d[key]+=1
print(d)  '''       

#print unique number(which is not repeated)in above program 
d={}
unique=[]
for key in arr:
    if key not in d:
        d[key]=1
    else:   
        d[key]+=1
for num,count in d.items():
    if count>1:
        print(num)
print(d)  