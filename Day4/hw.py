#password validation problem 
'''Requirements
s
for
if 
elif
else
count
lcount,ucount,dcount,scount'''

s=input()
ucount,lcount,dcount,scount=0,0,0,0

for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1

if len(s)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('valid')                
else:
    print('Invalid')




