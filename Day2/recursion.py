#recursion:calling by itself
#adv; program execution faster 
#reduces number of lines of code

#same set of 
#it is work on base condition ,to break the recursion we have to do (don't use loops)
#factorial code
'''n=5
fact=1  #using loops 
for i in range'''




#without using the loops
'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input())

print(fact(n))'''


def sum_of_natural(n):
    if n==1:
         return 1
    else:
         return n+sum_of_natural(n-1) 
print(sum_of_natural(5))

