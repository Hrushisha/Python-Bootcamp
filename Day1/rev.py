#s='sri devi is engineering college '

#egelloc gnireenigne si ived irs

def check(s):
    s=s.split()
    s=list(reversed(s))  # s became reverse list 
    for i in s:
        rev=i[::-1]  # characters of reverse list
        print(rev,end='')
s='sri devi is engineering college'  

check(s)