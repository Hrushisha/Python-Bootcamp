#arr[1,2,3,4,5]
# k=4
#[4,5,1,2,3]

arr=[1,2,3,4,5]

k=2

first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)

   #here we are using concatenation