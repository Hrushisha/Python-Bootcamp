'''arr[1,36,9,24,4,2,12]

count how many number are divisible of 4 and 6
pass this array as function parameter'''

def check(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
                print(i,end=' ')
        count+=1
    return count
arr=list(map(int,input().split()))   
print('the count is:',check(arr)) 