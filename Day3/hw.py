def check(num):
    num=str(num)

    twos=num.count('2')
    fours=num.count('4')
    eight=num.count('8')

    return twos==fours==eight and twos>0

def increment(N):
    count=0
    for num in range(1,N+1):
        if check(num):
            print(num)
            count+=1
    return count  
N=int(input())
print(increment(N))          