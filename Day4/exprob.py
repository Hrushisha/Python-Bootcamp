

'''print this pattern 
*
**
***
****
*****'''

'''n=5
for i in range(1,n+1):
    print('*'* i)'''

'''n=3 
i have print the  stars in diagonal form '''

n=3
for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')     
    print()



