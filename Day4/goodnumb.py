'''Good numbers:

arr=[35,9,1]

low<high
res=low cube+high cube'''



'''ceil values are used in math function 
print(math.cbrt(35))   use
without cbrt print(math.ceil(35**.3))  use this 
ceil gives approximation for 2.5=3
floor gives exact val 2.5=2'''

'''def find_good_numbers(arr):
    good_numbers = []
    
    for low in arr:
        for high in arr:
            if low < high:
                res = low**3 + high**3
                good_numbers.append((low, high, res))
    
    return good_numbers 

arr = [35, 9, 1]
good_numbers = find_good_numbers(arr)
print(good_numbers)'''

import math
arr=[35,9,1,65,126,133]

count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)
    
    while low<high:
        res=low**3+high**3
        
        if res==ele:
            print(ele)
            count+=1
        low+=1 
print('The count is:',count)        










