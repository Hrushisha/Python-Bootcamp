n=5

def check(n):    #userdefined we are using define function 
    first=0
    second=1
    print(first,second,end=' ')
    count=2
    while count<=n:
        third=first+second
        print(third,end=' ')
        first=second
        second=third
        count+=1
check(9)        
