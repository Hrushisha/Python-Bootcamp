'''n=4
for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print('*',end=' ')     
    print()'''

'''def print_star_border(rows, cols):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * cols)
        else:
            print('' + ' ' * (cols - 2) + '')

print_star_border(5, 10)'''

n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')    

