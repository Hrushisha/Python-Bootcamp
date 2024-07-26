'''n=2397

m=3

output:592721

if even digit then add with m
if odd digit then multiply with m'''


'''def transform_number(c, m):
    def transform_digit(digit, m):
        if digit % 2 == 0:
            return digit + m
        else:
            return digit * m

    result = 0
    place = 1

    while c > 0:
        digit = c % 10
        transformed = transform_digit(digit, m)
        result += transformed * place
        place *= 10
        c //= 10

    return result'''
n=2397

m=3

n=str(n)
for i in n:
    if int(i)%2==0:
       print(int(i)+m,end='')
    else:
       print(int(i)*m,end='')



'swap two numbers without using a third variable  '




'int a=a+b'

#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 10;
    
    a = a^b; '''a becomes 15'''
    b = a^b; ''' b becomes 5'''
    a = a^b; ''' a becomes 10'''
    
    cout << "a = " << a << ", b = " << b << endl;
    return 0;
}


s='a1b2c'






